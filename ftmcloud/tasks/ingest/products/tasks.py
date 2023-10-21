import pymongo
from celery import bootsteps
from kombu import Consumer, Queue, Exchange

from ftmcloud.core.crosscutting.models.tasks.models import MongoJSONConsumerTask


class ProductTask(MongoJSONConsumerTask):
    """
    Product task testing insertion of a document.
    """

    name = "product_task"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle_message(self, body, message):
        db = self._db.get_database('memorymaker')
        db.get_collection('test').insert_one(
            {
                "the product TASK": "it worked"
            }
        )
