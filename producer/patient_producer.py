import json
import time
import random
from confluent_kafka import Producer

conf = {
    "bootstrap.servers": "localhost:9092"
}

producer = Producer(conf)

patient_ids = [101, 102, 103, 104, 105]

while True:
    data = {
        "patient_id": random.choice(patient_ids),
        "heart_rate": random.randint(55, 140),
        "bp_systolic": random.randint(90, 190),
        "bp_diastolic": random.randint(60, 120),
        "oxygen": random.randint(85, 100),
        "temperature": round(random.uniform(97.0, 104.0), 1),
        "timestamp": int(time.time())
    }

    producer.produce(
        "patient_vitals",
        value=json.dumps(data)
    )

    producer.flush()
    print("Sent:", data)
    time.sleep(2)
