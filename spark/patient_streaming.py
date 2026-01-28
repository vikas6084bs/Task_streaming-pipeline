from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, IntegerType, DoubleType, LongType

spark = SparkSession.builder \
    .appName("PatientAlertStreaming") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

schema = StructType([
    StructField("patient_id", IntegerType()),
    StructField("heart_rate", IntegerType()),
    StructField("bp_systolic", IntegerType()),
    StructField("bp_diastolic", IntegerType()),
    StructField("oxygen", IntegerType()),
    StructField("temperature", DoubleType()),
    StructField("timestamp", LongType())
])

# Read vitals
raw_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "patient_vitals") \
    .option("startingOffsets", "latest") \
    .load()

json_df = raw_df.selectExpr("CAST(value AS STRING) as json")

vitals_df = json_df.select(from_json(col("json"), schema).alias("data")).select("data.*")

# ALERT RULES
alerts_df = vitals_df.filter(
    (col("heart_rate") > 120) |
    (col("oxygen") < 90) |
    (col("temperature") > 102) |
    (col("bp_systolic") > 170)
)

# Convert alerts to JSON
alerts_json = alerts_df.selectExpr(
    "to_json(struct(*)) AS value"
)

# Write alerts
query = alerts_json.writeStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("topic", "patient_alerts") \
    .option("checkpointLocation", "C:/tmp/patient_alerts_checkpoint") \
    .start()

query.awaitTermination()
