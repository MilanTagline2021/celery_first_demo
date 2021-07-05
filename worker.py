import os
import time

from celery import Celery


BROKER_URI = os.environ.get("CELERY_BROKER_URL", "redis://redis:6379/0")
RESULT_BACKEND_URI = os.environ.get("CELERY_RESULT_BACKEND", "redis://redis:6379/0")
app = Celery(
    'worker',
    broker=BROKER_URI,
    result=RESULT_BACKEND_URI,
    include=['main']
)

app.conf.beat_schedule = {
    'add-every-10-seconds': {
        'task': 'main.name',
        'schedule': 10
    },
}

