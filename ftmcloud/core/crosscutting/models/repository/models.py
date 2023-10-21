from pymongo import WriteConcern, ReadPreference
from pymongo.read_concern import ReadConcern

from ftmcloud.core.db.db import MongoDBSingleton


class MongoRepository:
    """
    Used to access database operations safely across threads.
    """

    _collection = None

    def __init__(self, collection):
        self._collection = collection
        self._mongo_db_singleton = MongoDBSingleton()

    def execute_query(
            self,
            callback,
            write_concern=None,
            read_concern=None,
            read_preference=ReadPreference.PRIMARY,
    ):
        """ Wraps query in a transaction to allow for atomic access to modification of
        collections.

        :return:
        """

        if write_concern is None:
            write_concern = WriteConcern("majority", wtimeout=1000)
        if read_concern is None:
            read_concern = ReadConcern("local")

        with self._mongo_db_singleton.start_session() as session:
            session.with_transaction(
                callback,
                read_concern=read_concern,
                write_concern=write_concern,
                read_preference=ReadPreference.PRIMARY,
            )
