from kafka import KafkaProducer
import json
import time
from datetime import datetime

productor = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda x: json.dumps(x).encode("utf-8")
)

print("Productor TRM iniciado correctamente")

while True:
       dato={
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "trm": 3850.50,
        "timestamp": time.time()
}
       productor.send("trm_data",dato)
       print("Dato enviado:", dato)
       time.sleep(5)



