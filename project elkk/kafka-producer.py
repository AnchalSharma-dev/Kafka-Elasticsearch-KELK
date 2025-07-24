from kafka import KafkaProducer
import json
import random
import time
from datetime import datetime

# Connect to Kafka broker running in Docker
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

log_levels = ["INFO", "DEBUG", "WARN", "ERROR"]
users = ["anchal", "rohit", "simran", "alex", "deepak", "batman", "robin"]
messages = [
    "User logged in", "User logged out", "File uploaded", "Permission denied",
    "Payment processed", "Connection timeout", "Database updated"
]

# Generate 5000 events
for i in range(5000):
    event = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "level": random.choice(log_levels),
        "user": random.choice(users),
        "message": random.choice(messages)
    }
    producer.send("test-topic", event)

    if i % 100 == 0:
        print(f"Sent {i} logs...")

    time.sleep(0.10)  # simulate natural log generation

producer.flush()
print("Finished sending logs.")
