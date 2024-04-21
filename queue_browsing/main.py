import pika
import random
from .config import RABBIT_HOST, EXCHANGE_NAME, EXCHANGE_TYPE, ROUTING_KEY
from .q_publisher.publisher import RabbitPublisher
from .q_consumer.consumer import RabbitConsumer
from .model import QueueContent

contents = []


def set_contents():
    for i in range(0, 10):
        contents.append(QueueContent(user_id=i, username=f"user_{i}"))


def get_rnd_content():
    return random.choice(contents)


connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBIT_HOST))
channel = connection.channel()
channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type=EXCHANGE_TYPE)
# Exclusive is not set, since we want to reuse the queue
result = channel.queue_declare(queue="")
queue_name = result.method.queue

publisher = RabbitPublisher(
    connection=connection,
    channel=channel,
    routing_key=ROUTING_KEY,
    exchange_name=EXCHANGE_NAME,
)
consumer = RabbitConsumer(
    channel=channel,
    queue_name=queue_name,
)


def main():
    set_contents()
    channel.queue_bind(
        exchange=EXCHANGE_NAME,
        queue=queue_name,
        routing_key=ROUTING_KEY,
    )
    for _ in range(5):
        publisher.publish(get_rnd_content())
    consumer.start_consuming()
