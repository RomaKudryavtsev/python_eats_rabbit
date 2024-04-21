import time
from queue_browsing.config import ROUTING_KEY, EXCHANGE_NAME, RABBIT_HOST
from queue_browsing.model import QueueContent, QueueMsg, ProcessingStatus
from .publisher import RabbitPublisher


contents = []


def set_contents():
    for i in range(0, 10):
        contents.append(QueueContent(user_id=i, username=f"user_{i}"))


publisher = RabbitPublisher(
    rabbit_host=RABBIT_HOST,
    routing_key=ROUTING_KEY,
    exchange_name=EXCHANGE_NAME,
)


def main():
    set_contents()
    for content in contents:
        msg = QueueMsg(status=ProcessingStatus.START, content=content)
        publisher.publish(msg)
    time.sleep(5)
    for content in contents:
        msg = QueueMsg(status=ProcessingStatus.FINISH, content=content)
        publisher.publish(msg)


__all__ = ("main",)
