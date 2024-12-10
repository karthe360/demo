from confluent_kafka import Producer
import json

# Kafka configuration
conf = {
    'bootstrap.servers': 'localhost:9092',  # Adjust to your Kafka broker address
}

# Create a Kafka producer instance
producer = Producer(conf)

def delivery_report(err, msg):
    """Called once for each message produced to indicate delivery result"""
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

def produce_message(topic, message):
    """Produce a message to the Kafka topic"""
    producer.produce(topic, json.dumps(message), callback=delivery_report)
    producer.flush()

if __name__ == "__main__":
    topic = 'my_topic'
    message = {"key": "value"}
    produce_message(topic, message)
