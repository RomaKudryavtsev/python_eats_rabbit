import pika

ROUTING_KEY = "contents"
EXCHANGE_NAME = "viewable_exchange"
EXCHANGE_TYPE = "direct"
RABBIT_HOST = "localhost"

CONNECTION = pika.BlockingConnection(pika.ConnectionParameters(host=RABBIT_HOST))
CHANNEL = CONNECTION.channel()
CHANNEL.exchange_declare(exchange=EXCHANGE_NAME, exchange_type=EXCHANGE_TYPE)
# Exclusive is not set, since we want to reuse the queue
result = CHANNEL.queue_declare(queue="")
QUEUE_NAME = result.method.queue
CHANNEL.queue_bind(
    exchange=EXCHANGE_NAME,
    queue=QUEUE_NAME,
    routing_key=ROUTING_KEY,
)
