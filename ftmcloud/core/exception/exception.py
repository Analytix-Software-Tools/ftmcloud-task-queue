class FtmTaskQueueException(Exception):
    """
    The base exception class that each exception variation will inherit from.
    """
    def __init__(self):
        pass

    def log(self):
        pass
    

class InvalidConfigException(FtmTaskQueueException):
    
    def __init__(self):
        super().__init__()


class MessageBrokerException(FtmTaskQueueException):
    pass


class BackendException(FtmTaskQueueException):
    pass


class InvalidTaskTypeException(FtmTaskQueueException):
    pass
