from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

spark = SparkSession.builder.appName("ConsumidorTRMStreaming").getOrCreate()

spark.sparkContext.setLogLevel("WARN")

esquema = StructType([
    StructField("fecha", StringType(), True),
    StructField("trm", DoubleType(), True),
    StructField("timestamp", DoubleType(), True)
])

flujo = (
    spark.readStream.format("kafka")
    .option("kafka.bootstrap.servers", "localhost:9092")
    .option("subscribe", "trm_data")
    .option("startingOffsets", "latest")
    .load()
)
datos = flujo.select(
    from_json(col("value").cast("string"), esquema).alias("dato")
).select("dato.*")

consulta = (
    datos.writeStream
    .outputMode("append")
    .format("console")
    .option("truncate", "false")
    .start()
)
consulta.awaitTermination()
