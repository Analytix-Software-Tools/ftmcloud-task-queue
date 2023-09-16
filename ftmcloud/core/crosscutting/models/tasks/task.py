from celery import Task
from kombu import Connection, Exchange, Queue
from ftmcloud.core.config.config import config
from ftmcloud.core.exception.exception import UndefinedMessageAckException


class BaseTask(Task):
    """
    Represents a base task that wraps the default Celery task.
    """
    name = "base-task"
    _queue_name = None
    _exchange_name = None
    _routing_key = None

    def __init__(self, name, queue, exchange_name, routing_key, *args, **kwargs):
        """
        Initialize a new BaseTask.
        :param name: the name of the task
        :param queue: the queue to subscribe to
        :param exchange_name: the name of the exchange
        :param routing_key: the routing key
        :param args: additional args to pass to base Task class
        :param kwargs: additional kwargs to pass to base Task class
        """
        super().__init__(*args, **kwargs)
        # Define the connection to the RabbitMQ broker in the constructor
        self.name = name
        self._queue_name = queue
        self._exchange_name = exchange_name
        self._routing_key = routing_key
        self.connection = Connection(config.BROKER_URI)

    def run(self):
        # Declare the exchange and queue you want to bind to
        exchange = Exchange(self._exchange_name, type='direct')
        queue = Queue(self._queue_name, exchange=exchange, routing_key='my_routing_key')

        # Create a consumer
        consumer = self.connection.Consumer(queue)
        consumer.register_callback(self.process_message)

        # Start consuming messages
        with consumer:
            while True:
                self.connection.drain_events()

    def handle_message(self, body, message):
        raise UndefinedMessageAckException()

    def process_message(self, body, message):
        # Handle the received message here, raise exception if undefined
        self.handle_message(body=body, message=message)
        message.ack()

    def __del__(self):
        # Close the connection when the task is destroyed
        self.connection.close()


class PipelineTask(Task):
    """
    Represents a sequence of tasks to be completed.
    """

    def __init__(self):
        pass


class TaskPipeline:
    """
    Represents a pipeline for a sequence of tasks to be completed with
    producer-consumer logic.
    """

    task_pipeline = []

    def __init__(self, task_pipeline):
        self.task_pipeline = task_pipeline
