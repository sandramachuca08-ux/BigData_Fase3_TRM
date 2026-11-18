
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
spark = SparkSession.builder.appName("Analisis_TRM_Batch").getOrCreate()
print("PROYECTO BIG DATA - ANALISIS HOSTORICO DE LA TRM")
df = spark.read.csv("rows.csv", header=True, inferSchema=True)

print("ESTRUCTURA DE LOS DATOS")
df.printSchema()
print("PRIMEROS REGISTROS")
df.show(10, truncate=False)
print("RESUMEN ESTADISTICO")
df.select("VALOR").describe().show()
print("REGISTROS CON TRM MAYOR A 5000 PESOS")
df.filter(F.col("VALOR") > 5000).show()
print("VALORES MAS ALTOS DE LA TRM")
df.orderBy(F.col("VALOR").desc()).select("VALOR", "VIGENCIADESDE", "VIGENCIAHASTA").show(10, truncate=False)
spark.stop()


