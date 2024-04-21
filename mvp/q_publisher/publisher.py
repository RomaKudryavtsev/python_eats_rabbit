import json
import pika
from dataclasses import asdict
from mvp.model import QueueMsg


def serialize_to_queue_msg(msg: QueueMsg):
    return json.dumps(asdict(msg))


class RabbitPublisher:
    def __init__(self, rabbit_host, routing_key, exchange_name):
        self.rabbit_host = rabbit_host
        self.routing_key = routing_key
        self.exchange_name = exchange_name

    def publish(self, msg: QueueMsg):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.rabbit_host)
        )
        channel = connection.channel()
        channel.exchange_declare(exchange=self.exchange_name, exchange_type="direct")
        with connection:
            queue_msg = serialize_to_queue_msg(msg=msg)
            channel.basic_publish(
                exchange=self.exchange_name,
                routing_key=self.routing_key,
                body=queue_msg,
            )
            print(f" [x] Message sent: {str(queue_msg)}")
