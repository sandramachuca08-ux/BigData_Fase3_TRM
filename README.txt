PROYECTO BIG DATA - TAREA 3 
Procesamiento de datos con Apache Spark y Kafka

DESCRIPCION:
El proyecto utiliza informaciòn històrica de la Tasa Representativa del Mercado (TRM) de Colombia para realizar procesamiento por lotes y procesamiento en tiempo real.

HERRAMIENTAS UTILIZADAS:
-Ubuntu 22.04.5
-Python 3
-Apache Spark 3.5.6
-Apache Kafka 3.9.2
-PySpark
-Kafka-Python

ARCHIVOS:
-rows.csv: conjunto de datos historico de la TRM.
-procesamiento_batch.py: procesamiento por lotes.
-resultados_batch.txt: resultados del procesamiento por lotes.
-productor_trm.py: envìo de datos simulados a kafka.
-consumidor_trm.py: recepciòn y procesamiento de datos con Spark Streaming.

EJECUCIÒN DEL PROCESAMIENTO POR LOTES:
1. Abrir la terminal-
2. Ingresar a la carpeta del proyecto: 
   cd /home/vboxuser/BigData_Fase3
3. Ejecutar
   python3 procesamiento_batch.py

EJECUCIÒN EN TIEMPO REAL:
1. Iniciar zookeeper.
2. Iniciar el servidor kafka.
3. Ejecutar el productor de datos TRM.
4. Ejecutar el consumidor mediante Spark Streaming.

CONCLUSIÒN:
El proyecto permite anàlizar datos històricos de la TRM mediante Apache Sparky de mostrar el flujo de datos en tiempo real utilizando Apache kafka y Spark Streaming.
