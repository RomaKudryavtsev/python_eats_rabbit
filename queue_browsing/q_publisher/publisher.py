import json
from dataclasses import asdict
from queue_browsing.model import QueueContent


def serialize_to_queue_msg(content: QueueContent):
    return json.dumps(asdict(content))


class RabbitPublisher:
    def __init__(self, connection, channel, routing_key, exchange_name):
        self.connection = connection
        self.channel = channel
        self.routing_key = routing_key
        self.exchange_name = exchange_name

    def publish(self, msg_content: QueueContent):
        msg = serialize_to_queue_msg(msg_content)
        self.channel.basic_publish(
            exchange=self.exchange_name,
            routing_key=self.routing_key,
            body=msg,
        )
        print(f" [x] Sent {self.routing_key}:{msg}")
        # self.connection.close()
