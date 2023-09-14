import logging
import sys


class FtmTaskQueueException(BaseException):
    """
    The base exception class that each exception variation will inherit from.
    """

    _log_level = logging.Logger
    _message = ""
    _log_error = True
    _log_file_loc = ""

    def __init__(self, message=None, logger=None):
        if logger is not None:
            self._logger = logger
        else:
            self._logger = logging.getLogger("FtmTaskQueueException")
        self._message = message
        self._logger.error(msg=message)
        super().__init__()
        super().with_traceback(__tb=sys.exception().__traceback__)

    def _write_log_to_file(self):
        with open(self._log_file_loc, mode='w') as _out_log:
            _out_log.write(str(self.__traceback__))

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


class UndefinedMessageAckException(FtmTaskQueueException):
    def __init__(self):
        super().__init__()


class ResourceLockedException(FtmTaskQueueException):

    def __init__(self):
        super().__init__()
