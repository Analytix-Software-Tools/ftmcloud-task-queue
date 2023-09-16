from ftmcloud.core.app.app import TaskQueueApplication
import sys

from celery import Celery
from ftmcloud.core.config.config import config

app = Celery('ftmcloud.tasks', broker=config.BROKER_URI, backend=config.BACKEND_URI)
app.conf.update(
    task_serializer='json',
    accept_content=['json'],  # Ignore other content
    result_serializer='json',
    timezone='Europe/Oslo',
    enable_utc=True,
)


@app.task(serializer='json', name='my_task_is_here', queue="product_import")
def task1(arg1):
    print(arg1)


app.start(argv=sys.argv[1:])
