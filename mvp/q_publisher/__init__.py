import asyncio
from mvp.config import ROUTING_KEY, EXCHANGE_NAME, RABBIT_HOST
from mvp.model import QueueContent, QueueMsg, ProcessingStatus
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


async def simulate_on_start():
    set_contents()
    for content in contents:
        msg = QueueMsg(status=ProcessingStatus.START, content=content)
        publisher.publish(msg)


async def simulate_on_finish():
    for content in contents:
        msg = QueueMsg(status=ProcessingStatus.FINISH, content=content)
        publisher.publish(msg)


async def main():
    start_task = asyncio.create_task(simulate_on_start())
    finish_task = asyncio.create_task(simulate_on_finish())
    await start_task
    await finish_task


__all__ = ("main",)
