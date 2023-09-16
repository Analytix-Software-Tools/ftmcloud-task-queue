import pymongo

from ftmcloud.core.crosscutting.models.tasks.task import BaseTask
from pymongo import MongoClient


class ProductImportTask(BaseTask):
    """
    Ingests many products into MongoDB.
    """

    def __init__(self):
        super().__init__(name="product_import", exchange_name="", queue="product_import", routing_key="")

    def handle_message(self, body, message):
        # NOTE: DO NOT USE THIS IN PRODUCTION. PURELY FOR TESTING
        mongo = pymongo.MongoClient("bW9uZ29kYitzcnY6Ly9hZG1pbjpla3kwUFF5TjNjZDcxV3dZQGNsdXN0ZXIwLmlsbHFoLm1vbmdvZGIubmV0")
        db = mongo.get_database(name="memorymaker")
        db.get_collection(name="test").insert_one(
            {
                "name": "HELLO WORLD"
            }
        )
