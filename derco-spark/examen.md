Baby names - Reloading from URL

https://dbc-63674b0c-784d.cloud.databricks.com/?o=4310762918993197#notebook/3480212120491645/command/3480212120491646


Baby names - Not reload from web

https://dbc-63674b0c-784d.cloud.databricks.com/?o=4310762918993197#notebook/3480212120491647/command/902023380303670

CSV Parsing

https://dbc-63674b0c-784d.cloud.databricks.com/?o=4310762918993197#notebook/3811593202085616/command/4385597734810635

Log Analyzer

https://dbc-63674b0c-784d.cloud.databricks.com/?o=4310762918993197#notebook/902023380303675/command/902023380303682

```scala
val data = """Row-Key-001, K1, 10, A2, 20, K3, 30, B4, 42, K5, 19, C20, 20
     | Row-Key-002, X1, 20, Y6, 10, Z15, 35, X16, 42
     | Row-Key-003, L4, 30, M10, 5, N12, 38, O14, 41, P13, 8"""

val rdd = sc.parallelize(data.split("\n"))
val rdd1 = rdd.map(l => l.trim.split(","))

val df = rdd1.toDF()
val df1 = df.select((0 until 13).map(i => col("value")(i).alias(s"col$i")): _*)
val df1 = df.select((0 until 13).map(i => col("value")(i)): _*)
val df1 = df.select((0 until 13).map(i => col("value")(i)): _*)
```