// Databricks notebook source
// MAGIC %md
// MAGIC # CSV Parsing

// COMMAND ----------

val full_csv = sc.parallelize(Array(
"col_1, col_2, col_3",
"1, ABC, Foo1",
"2, ABCD, Foo2",
"3, ABCDE, Foo3",
"4, ABCDEF, Foo4",
"5, DEF, Foo5",
"6, DEFGHI, Foo6",
"7, GHI, Foo7",
"8, GHIJKL, Foo8",
"9, JKLMNO, Foo9",
"10, MNO, Foo10"))


// COMMAND ----------



// COMMAND ----------

// MAGIC %md
// MAGIC ## Question #1: CSV Header Rows

// COMMAND ----------

import org.apache.spark.sql.types.{StructType, StructField, StringType, IntegerType};
import org.apache.spark.sql.functions.{explode, split}
import org.apache.spark.sql.functions.{col}

val header = full_csv.first()

// remove header row
val csvDataRdd = full_csv.filter(l =>  l != header)
val tempdf = csvDataRdd.toDF()
tempdf.show

// COMMAND ----------

// MAGIC %md
// MAGIC ## Question #2: SparkSQL Dataframes

// COMMAND ----------

// val df = csvDataRdd.toDF()
// val df2 = df.withColumn("value", split($"value", ","))
// val df3 = df2.select((0 until 3).map(i => col("value")(i).alias(s"col$i")): _*).toDF("id","A","B")

val rowRdd = csvDataRdd.map(l => l.split(", "))
val df = rowRdd.toDF()

// schema created from manually
// val csvSchema = StructType(Seq(
//     StructField("col_1", StringType, true),
//     StructField("col_2", StringType, true),
//     StructField("col_3", StringType, true)
//   ))

// schema created programatically from header text (csv)
val csvSchema = StructType(header.split(",").map(col_header => StructField(col_header.trim(), StringType)))

val x = rowRdd.map(r => Row(r(0), r(1), r(2)))
val xdf = spark.createDataFrame(x, csvSchema)
xdf.show()
