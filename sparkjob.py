from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SparkSession

# Initialize SparkContext
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Specify the S3 URI for the CSV file
s3_input_uri = "s3://smartphone-data/smartphones%2B-%2Bsmartphones.csv"

# Read data from CSV file in S3
df = spark.read.format("csv") \
    .option("header", "true") \
    .load(s3_input_uri)

# Specify the output folder for Parquet files
output_folder = "Parquet-format-data"

# Convert data to Parquet format and write to S3
s3_output_uri = f"s3://smartphone-data/{output_folder}/"
df.write.format("parquet") \
    .mode("overwrite") \
    .save(s3_output_uri)

# Stop the SparkSession
spark.stop()
