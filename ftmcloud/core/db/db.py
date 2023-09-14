from pymongo import MongoClient
from ftmcloud.core.config.config import config
from ftmcloud.core.crosscutting.models.singleton.singleton import Singleton


class MongoDBSingleton(Singleton):
    """
    Represents a MongoDB singleton to limit the number of open connections to one
    connection pool.
    """
    mongo_instance = None

    def __new__(cls, *args, **kwargs):
        cls.mongo_instance = MongoClient(config.MONGO_URI)
        super(MongoDBSingleton, cls).__new__(cls, *args, **kwargs)
