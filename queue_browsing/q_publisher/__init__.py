from queue_browsing.config import connection, channel, ROUTING_KEY, EXCHANGE_NAME


publisher = RabbitPublisher(
    connection=connection,
    channel=channel,
    routing_key=ROUTING_KEY,
    exchange_name=EXCHANGE_NAME,
)
