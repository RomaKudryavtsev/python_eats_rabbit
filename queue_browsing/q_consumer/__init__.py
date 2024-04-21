from .consumer import RabbitConsumer
from queue_browsing.config import CHANNEL, QUEUE_NAME


consumer = RabbitConsumer(
    channel=CHANNEL,
    queue_name=QUEUE_NAME,
)


def main():
    consumer.start_consuming()

__all__ = ("main",)