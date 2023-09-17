import pymongo
from celery import bootsteps
from kombu import Consumer, Queue, Exchange


class ProductImportTask(bootsteps.ConsumerStep):
    """
    Ingests many products into MongoDB.
    """

    my_queue = Queue('product_import', Exchange('main'), 'routing_key')

    def get_consumers(self, channel):
        return [Consumer(channel,
                         queues=[self.my_queue],
                         callbacks=[self.handle_message],
                         accept=['json'])]


    def on_message(self, body, message):
        print("I got a message")
        message.ack()

    def handle_message(self, body, message):
        # NOTE: DO NOT USE THIS IN PRODUCTION. PURELY FOR TESTING
        mongo = pymongo.MongoClient("bW9uZ29kYitzcnY6Ly9hZG1pbjpla3kwUFF5TjNjZDcxV3dZQGNsdXN0ZXIwLmlsbHFoLm1vbmdvZGIubmV0")
        db = mongo.get_database(name="memorymaker")
        db.get_collection(name="test").insert_one(
            {
                "name": "HELLO WORLD"
            }
        )
