import pika

ROUTING_KEY = "contents"
EXCHANGE_NAME = "viewable_exchange"
EXCHANGE_TYPE = "direct"
RABBIT_HOST = "localhost"

connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBIT_HOST))
channel = connection.channel()
channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type=EXCHANGE_TYPE)
# Exclusive is not set, since we want to reuse the queue
result = channel.queue_declare(queue="")
queue_name = result.method.queue
