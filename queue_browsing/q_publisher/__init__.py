import random
from queue_browsing.config import (
    CONNECTION,
    CHANNEL,
    ROUTING_KEY,
    EXCHANGE_NAME,
)
from queue_browsing.model import QueueContent
from .publisher import RabbitPublisher


contents = []


def set_contents():
    for i in range(0, 10):
        contents.append(QueueContent(user_id=i, username=f"user_{i}"))


def get_rnd_content():
    return random.choice(contents)


publisher = RabbitPublisher(
    connection=CONNECTION,
    channel=CHANNEL,
    routing_key=ROUTING_KEY,
    exchange_name=EXCHANGE_NAME,
)


def main():
    set_contents()
    for _ in range(5):
        publisher.publish(get_rnd_content())


if __name__ == "__main__":
    main()
