# Databricks notebook source
# MAGIC %md
# MAGIC ## Read and parse Log File
# MAGIC
# MAGIC Apache access log line example
# MAGIC
# MAGIC ```
# MAGIC 13.66.139.0 - - [19/Dec/2020:13:57:26 +0100] "GET /index.php?option=com_phocagallery&view=category&id=1:almhuette-raith&Itemid=53 HTTP/1.1" 200 32653 "-" "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)" "-"
# MAGIC ```

# COMMAND ----------

# MAGIC %scala
# MAGIC import java.net.URL
# MAGIC import java.io.File
# MAGIC import org.apache.commons.io.FileUtils
# MAGIC  
# MAGIC val tmpFile = new File("/tmp/access.log")
# MAGIC //FileUtils.copyURLToFile(new URL("https://raw.githubusercontent.com/bdbaraban/holberton-system_engineering-devops/master/0x04-loops_conditions_and_parsing/apache-access.log"), tmpFile)
# MAGIC FileUtils.copyURLToFile(new URL("https://gist.githubusercontent.com/zxcfer/5518d2976a19889e9594ee3923612717/raw/9b1ac12041eda8e23378b01ad0554e93d89e0450/accesslog"), tmpFile)

# COMMAND ----------

import re
from pyspark.sql import Row

APACHE_ACCESS_LOG_PATTERN = '^(\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})\] "(\S+) (\S+) (\S+)" (\d{3}) (\d+)'

# Parse to dictionary
def parse_apache_log_line(logline):
    try:
        match = re.search(APACHE_ACCESS_LOG_PATTERN, logline)
        if match is None:
            # Optionally, you can change this to just ignore if each line of data is not critical.
            # For this example, we want to ensure that the format is consistent.
            raise Exception("Invalid logline: %s" % logline)
        return Row(
            ipAddress    = match.group(1),
            clientIdentd = match.group(2),
            userId       = match.group(3),
            dateTime     = match.group(4),
            method       = match.group(5),
            endpoint     = match.group(6),
            protocol     = match.group(7),
            responseCode = int(match.group(8)),
            trail        = match.group(9)
            )
    except:
        print('err')
        

raw_log_files = sc.textFile("file:/tmp/access.log")
raw_log_files.count()

parsed_log_files = raw_log_files.map(parse_apache_log_line)
df = parsed_log_files.toDF()
df.show(10)

df.createOrReplaceTempView ("log_data")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Statistics

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT count(*) as total, responseCode FROM log_data group by responseCode

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC ## Create Stats

# COMMAND ----------


