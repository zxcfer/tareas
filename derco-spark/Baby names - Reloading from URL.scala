// Databricks notebook source
import org.apache.spark.sql.{DataFrame, SQLContext, SparkSession}

def GetUrlContentJson(url: String): DataFrame ={
    val result = scala.io.Source.fromURL(url).mkString
    val jsonResponseOneLine = result.toString().stripLineEnd    
    val jsonRdd = spark.sparkContext.parallelize(jsonResponseOneLine :: Nil)
    val jsonDf = spark.read.json(spark.createDataset(jsonRdd))
    return jsonDf
}
val df = GetUrlContentJson("https://health.data.ny.gov/api/views/jxy9-yhdk/rows.json?accessType=DOWNLOAD")
df.show()

// COMMAND ----------

import org.apache.spark.sql.functions.{explode, split}
import org.apache.spark.sql.functions.{col}

val explode_df = df.select(explode(col("data")))
val df2 = explode_df.select((0 until 13).map(i => col("col")(i).alias(s"col$i")): _*)
                    .toDF("sid","id","position","created_at","created_meta","updated_at","updated_meta","meta","year","firstname","county","sex","count")
df2.show(7, false)

// COMMAND ----------

// MAGIC %md
// MAGIC ## Query example

// COMMAND ----------

df2.createOrReplaceTempView("datax")
val df3 = spark.sql("select * from datax where county = 'BRONX'")
df3.show(7, false)

// COMMAND ----------

val df4 = spark.sql("select * from datax where meta <> '{ }'")
df4.show(5, false)

// COMMAND ----------

// MAGIC %sql
// MAGIC select temp5.year, totalfirst, letter from (
// MAGIC   select year, totalfirst, letter from (
// MAGIC   Select sum(total) as totalfirst, letter, year from (
// MAGIC     select substr(firstname, 0, 1) as letter, count as total, year from datax) as temp3
// MAGIC     group by year, letter
// MAGIC     order by year, totalfirst DESC
// MAGIC   ) as temp4
// MAGIC ) as temp5
// MAGIC left join (
// MAGIC select year, max(totalfirst) as finaltotal from (
// MAGIC Select sum(total) as totalfirst, letter, year from (
// MAGIC   select substr(firstname, 0, 1) as letter, count as total, year from datax) as temp1
// MAGIC   group by year, letter
// MAGIC   order by year, totalfirst DESC
// MAGIC ) as temp2
// MAGIC group by year
// MAGIC order by year, finaltotal DESC
// MAGIC ) as temp6
// MAGIC where temp5.year = temp6.year and temp5.totalfirst = temp6.finaltotal 
// MAGIC order by year
