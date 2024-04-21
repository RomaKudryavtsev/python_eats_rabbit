class RabbitConsumer:
    def __init__(self, channel, queue_name):
        self.channel = channel
        self.queue_name = queue_name

        def callback(ch, method, properties, body):
            print(
                f"Available message count: {self.channel.get_waiting_message_count()}"
            )
            print(f" [x] {method.routing_key}:{body}")

        self.callback = callback

    def start_consuming(self):
        # An ack(nowledgement) is sent back by the consumer to tell RabbitMQ that a particular message had been received, processed and that RabbitMQ is free to delete it.
        self.channel.basic_consume(
            queue=self.queue_name,
            on_message_callback=self.callback,
            # This ensures that message is not consumed
            auto_ack=False,
        )
        print(" [*] Waiting for logs. To exit press CTRL+C")
        self.channel.start_consuming()
