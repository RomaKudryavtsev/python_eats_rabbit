from .consumer import RabbitConsumer
from queue_browsing.config import channel, queue_name


consumer = RabbitConsumer(
    channel=channel,
    queue_name=queue_name,
)
