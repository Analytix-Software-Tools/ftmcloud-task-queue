from celery import Celery

from ftmcloud.core.config.config import BaseConfig
from ftmcloud.core.exception.exception import InvalidConfigException


class TaskQueueApplication(Celery):
    """
    Performs initialization of the base application as well as any additional configuration
    necessary. Wraps the celery application.
    """

    def __init__(self, options=None, config=BaseConfig()):
        """
        Initialize a new instance of the application.

        :param options: the options
        :param config: the config
        """
        if not isinstance(config, BaseConfig):
            raise InvalidConfigException()
        super().__init__(
            broker=config.BROKER_URI,
            backend=config.BACKEND_URI
        )
        self.autodiscover_tasks(
            packages=['ftmcloud.tasks']
        )
