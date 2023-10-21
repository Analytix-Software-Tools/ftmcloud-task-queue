import os
from datetime import datetime

from ftmcloud.core.app.app import TaskQueueApplication
import sys

from celery import Celery
from ftmcloud.core.config.config import config
from ftmcloud.tasks.ingest.products.tasks import ProductTask

app = Celery('ftmcloud.tasks', broker=config.BROKER_URI, backend=config.BACKEND_URI)
app.conf.update(
    task_serializer='json',
    accept_content=['json'],  # Ignore other content
    result_serializer='json',
    timezone='Europe/Oslo',
    enable_utc=True,
)
# app.select_queues(queues=["product_import", "celery"])
app.steps['consumer'].add(ProductTask)


app.start(argv=sys.argv[1:])
