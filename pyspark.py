from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, LongType
from awsglue.transforms import ApplyMapping

# Initialize SparkContext
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Create dynamic frame from CSV file in S3
S3bucket_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={"quoteChar": '"', "withHeader": True, "separator": ","},
    connection_type="s3",
    format="csv",
    connection_options={
        "paths": ["s3://smartphone-data/smartphones - smartphones.csv"],
        "recurse": True,
    },
    transformation_ctx="S3bucket_node1",
)

# Schema definition
schema = StructType([
    StructField("model", StringType(), True),
    StructField("price", StringType(), True),
    StructField("rating", LongType(), True),
    StructField("sim", StringType(), True),
    StructField("processor", StringType(), True),
    StructField("ram", StringType(), True),
    StructField("battery", StringType(), True),
    StructField("display", StringType(), True),
    StructField("camera", StringType(), True),
    StructField("card", StringType(), True),
    StructField("os", StringType(), True)
])

# Apply schema to dynamic frame
df = ApplyMapping.apply(frame=S3bucket_node1, mappings=[
    ("model", "string", "model", "string"),
    ("price", "string", "price", "string"),
    ("rating", "long", "rating", "long"),
    ("sim", "string", "sim", "string"),
    ("processor", "string", "processor", "string"),
    ("ram", "string", "ram", "string"),
    ("battery", "string", "battery", "string"),
    ("display", "string", "display", "string"),
    ("camera", "string", "camera", "string"),
    ("card", "string", "card", "string"),
    ("os", "string", "os", "string")
])

# Specify the S3 path for the Parquet output
output_path = "s3://smartphone-data/parquet_formatted_dataset/"

# Get the sink
s3_parquet_sink = glueContext.getSink(
    path=output_path,
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=[],
    compression="snappy",
    enableUpdateCatalog=True,
    transformation_ctx="S3Parquetsave_node3"
)

# Set catalog info
s3_parquet_sink.setCatalogInfo(
    catalogDatabase="smartphone-database",
    catalogTableName="smartphone_parquet_data"
)

# Set format to glueparquet
s3_parquet_sink.setFormat("glueparquet")

# Write DataFrame to S3 in Parquet format
s3_parquet_sink.writeFrame(df)
