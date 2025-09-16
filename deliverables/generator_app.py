# generator/app.py
import json
import os
from kafka import KafkaProducer
from time import sleep
from transactions import create_random_transaction

KAFKA_BROKER_URL = os.environ.get("KAFKA_BROKER_URL")
TRANSACTIONS_TOPIC = os.environ.get("TRANSACTIONS_TOPIC")
TRANSACTIONS_PER_SECOND = float(os.environ.get("TRANSACTIONS_PER_SECOND"))
SLEEP_TIME = 1 / TRANSACTIONS_PER_SECOND

def stop_requested():
    return os.environ.get("STOP_FLAG", "false").lower() == "true"

if __name__ == "__main__":
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER_URL,
        # Encode all values as JSON
        value_serializer=lambda value: json.dumps(value).encode(),
    )
    while not stop_requested():
        transaction: dict = create_random_transaction()
        message: str = json.dumps(transaction)
        producer.send(TRANSACTIONS_TOPIC, value=transaction)
        print("Producing transaction:", transaction) # Debug
        sleep(SLEEP_TIME)