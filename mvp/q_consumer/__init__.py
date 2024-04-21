from .consumer import RabbitConsumer
from mvp.config import RABBIT_HOST, ROUTING_KEY, EXCHANGE_NAME


consumer = RabbitConsumer(
    rabbit_host=RABBIT_HOST,
    routing_key=ROUTING_KEY,
    exchange_name=EXCHANGE_NAME,
)


def main():
    consumer.start_consuming()


__all__ = ("main",)
