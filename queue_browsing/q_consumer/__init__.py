from .consumer import RabbitConsumer
from queue_browsing.config import CHANNEL, queue_name


consumer = RabbitConsumer(
    channel=CHANNEL,
    queue_name=queue_name,
)

consumer.start_consuming()
