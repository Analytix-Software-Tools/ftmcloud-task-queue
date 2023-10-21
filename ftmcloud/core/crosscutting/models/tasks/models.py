import json

from celery import Task, bootsteps
from kombu import Connection, Exchange, Queue, Consumer
from ftmcloud.core.config.config import config
from ftmcloud.core.db.db import MongoDBSingleton
from ftmcloud.core.exception.exception import UndefinedMessageAckException


class BaseTask(bootsteps.ConsumerStep):
    """
    Represents a base task that wraps the default Celery task.
    """
    name = "base-task"
    _queue_name = "celery"
    _exchange_name = "celery"
    _routing_key = "celery"

    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseTask.
        :param args: additional args to pass to base Task class
        :param kwargs: additional kwargs to pass to base Task class
        """
        super().__init__(*args, **kwargs)
        self.connection = Connection(config.BROKER_URI)

    def get_consumers(self, channel):
        return [Consumer(channel,
                         queues=[self._queue_name],
                         callbacks=[self.handle_message],
                         accept=['json'])]

    def run(self):
        exchange = Exchange(self._exchange_name, type='direct')
        queue = Queue(self._queue_name, exchange=exchange, routing_key=self._routing_key)

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
        self.connection.close()


class JsonConsumerTask(BaseTask):
    """
    Represents a type of task that enforces the task consumer be a JSON.
    """

    def __init__(self, *args, **kwargs):
        """ Initialize a new JsonConsumerTask.

        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)

    def process_message(self, body, message):
        """ Enforce the body of the message be a JSON.

        :param body:
        :param message:
        :return:
        """
        try:
            body = json.loads(body)
            self.handle_message(body=body, message=message)
        except json.JSONDecodeError as E:
            pass
        message.ack()


class MongoJSONConsumerTask(JsonConsumerTask):
    """
    Represents a type of class which persists a Mongo database connection and consumes JSON
    content from the message body.
    """
    _db = MongoDBSingleton()


class PipelineTask(Task):
    """
    Represents a sequence of tasks to be completed.
    """

    def __init__(self):
        pass


class MongoPipelineTask(PipelineTask):
    """
    Pipeline task that manages mongo database interactions.
    """
    pass
