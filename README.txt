Proyecto Big Data Fase 3 – Análisis de la TRM en Colombia

Descripción del proyecto

Este proyecto tiene como finalidad aplicar herramientas y tecnologías Big Data para el procesamiento y análisis de información relacionada con la Tasa Representativa del Mercado (TRM) en Colombia.

Se implementaron procesos de procesamiento por lotes (Batch) y procesamiento de datos en tiempo real (Streaming), utilizando Python, Apache Spark y Apache Kafka.

Objetivo

Desarrollar una solución Big Data que permita procesar información histórica y simular la transmisión y recepción continua de datos de la TRM.

Herramientas utilizadas

- Python.
- Apache Spark.
- PySpark.
- Apache Kafka.
- Spark Structured Streaming.
- Ubuntu Linux.
- GitHub.

Archivos del proyecto

- `procesamiento_batch.py`: procesamiento de datos históricos mediante Spark.
- `productor_trm.py`: generación y envío de datos simulados a Kafka.
- `consumidor_trm.py`: recepción y procesamiento de datos mediante Spark Streaming.
- `rows.csv`: archivo de datos utilizado para el procesamiento.
- `resultados_batch.txt`: archivo con resultados del procesamiento.

Funcionamiento

El proyecto integra tres etapas:

1. Procesamiento histórico de datos mediante Batch.
2. Generación y transmisión de registros de la TRM mediante Kafka.
3. Recepción y visualización de datos en tiempo real mediante Spark Streaming.

Autor

Sandra Margarita Rodriguez Machuca

Repositorio

https://github.com/sandramachuca08-ux/BigData_Fase3_TRM
