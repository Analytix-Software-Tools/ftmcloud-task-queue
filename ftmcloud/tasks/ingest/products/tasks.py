import pymongo
from celery import bootsteps
from kombu import Consumer, Queue, Exchange

from ftmcloud.core.crosscutting.models.tasks.task import MongoJSONConsumerTask


class ProductImportTask(bootsteps.ConsumerStep):
    """
    Ingests many products into MongoDB.
    """

    queue = Queue('celery', Exchange('celery'), 'celery')

    def get_consumers(self, channel):
        return [Consumer(channel,
                         queues=[self.queue],
                         callbacks=[self.handle_message],
                         accept=['json'])]

    def handle_message(self, body, message):
        # NOTE: DO NOT USE THIS IN PRODUCTION. PURELY FOR TESTING
        mongo = pymongo.MongoClient(
            "mongodb+srv://admin:eky0PQyN3cd71WwY@cluster0.illqh.mongodb.net/")
        db = mongo.get_database(name="memorymaker")
        db.get_collection(name="test").insert_one(
            {
                "messageContent": body
            }
        )
        message.ack()


class ProductTask(MongoJSONConsumerTask):

    def handle_message(self, body, message):
        print(body)
