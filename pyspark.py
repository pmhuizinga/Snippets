# Libraries
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.functions import current_date, current_timestamp

# Read from SQL endpoint
df = spark.sql("SELECT * FROM BRONZE_LH.AFAS_BI_Medewerker_Functie LIMIT 1000")
display(df)

#JSON to dataframe
df = spark.createDataFrame(Row(**x) for x in results_list)

# Add columns with current date
df = df.withColumn("load_date",current_date()).withColumn("load_timestamp",current_timestamp())

# Write dataframe to delta table
# option("overwriteschema") is tbv eventuele nieuwe/andere kolommen.
df.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(delta_table_path) 

