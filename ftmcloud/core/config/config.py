import base64
import os


class BaseConfig:
    """
    The base (default) configuration.
    """

    REDIS_URI_ENCODED = os.environ['REDIS_URI_ENCODED'] if 'REDIS_URI_ENCODED' in os.environ else ''
    REDIS_URI = base64.b64decode(REDIS_URI_ENCODED)
    BACKEND_URI = REDIS_URI

    RABBITMQ_URI_ENCODED = os.environ['RABBITMQ_URI_ENCODED'] if 'RABBITMQ_URI_ENCODED' in os.environ else ''
    RABBITMQ_URI = base64.b64decode(RABBITMQ_URI_ENCODED)
    BROKER_URI = RABBITMQ_URI

