#!/bin/sh

# Wait until Kafka broker is available
echo "Waiting for Kafka broker at $KAFKA_BROKER_URL..."

while ! nc -z broker 9092; do
  sleep 0.5
done

echo "Kafka broker is available. Starting the app..."
exec python app.py