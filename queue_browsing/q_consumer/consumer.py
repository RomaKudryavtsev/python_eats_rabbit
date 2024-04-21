import json
import pika
from queue_browsing.model import QueueMsg, ProcessingStatus


class RabbitConsumer:
    def __init__(self, rabbit_host, routing_key, exchange_name):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbit_host)
        )
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange=exchange_name, exchange_type="direct")
        # Exclusive is not set, since we want to reuse the queue
        result = self.channel.queue_declare(queue="")
        self.queue_name = result.method.queue
        self.channel.queue_bind(
            exchange=exchange_name,
            queue=self.queue_name,
            routing_key=routing_key,
        )
        self.queue_state = []

        def callback(ch, method, properties, body):
            json_message = json.loads(body)
            msg_received = QueueMsg(**json_message)
            print(f" [x] {method.routing_key}:{msg_received}")
            if msg_received.status == ProcessingStatus.START:
                self.queue_state.append(msg_received.content)
            else:
                self.queue_state.remove(msg_received.content)
            print(f"Current state: {str(self.queue_state)}")

        self.callback = callback

    def start_consuming(self):
        self.channel.basic_consume(
            queue=self.queue_name,
            on_message_callback=self.callback,
            auto_ack=True,
        )
        print(" [*] Waiting for messages. To exit press CTRL+C")
        self.channel.start_consuming()
