from confluent_kafka import Consumer, KafkaException, KafkaError

# Kafka configuration
conf = {
    'bootstrap.servers': 'localhost:9092',  # Adjust to your Kafka broker address
    'group.id': 'my_group',
    'auto.offset.reset': 'earliest',
}

# Create a Kafka consumer instance
consumer = Consumer(conf)

def consume_messages(topic):
    """Consume messages from the Kafka topic"""
    consumer.subscribe([topic])

    try:
        while True:
            msg = consumer.poll(timeout=1.0)  # Timeout in seconds
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    print(f"End of partition reached {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")
                else:
                    raise KafkaException(msg.error())
            else:
                print(f"Consumed message: {msg.value().decode('utf-8')}")
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

if __name__ == "__main__":
    topic = 'my_topic'
    consume_messages(topic)
