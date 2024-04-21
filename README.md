# Python integration with RabbitMQ

## Install latest RabbitMQ 3.13
<pre>docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management</pre>

## Run MVP
- Run consumer: <pre>python -m mvp.run_consumer</pre>
- Run publisher: <pre>python -m mvp.run_publisher</pre>

## Run examples
<pre>python .\publish_subscribe\emit_logs.ps {args}</pre>

## Sources
- <a>https://www.rabbitmq.com/tutorials/tutorial-five-python</a>
- <a>https://gist.github.com/pilate/4025942</a>
- <a>https://stackoverflow.com/questions/54505150/pika-rabbitmq-get-all-messages-from-the-queue-without-consuming-them</a>
- <a>https://stackoverflow.com/questions/4700292/using-rabbitmq-is-there-a-way-to-look-at-the-queue-contents-without-a-dequeue-op</a>
- <a>https://stackoverflow.com/questions/54866975/get-message-from-rabbitmq-without-consuming</a>