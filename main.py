from celery import Celery
import os

BROKER_URI = os.environ.get("CELERY_BROKER_URL", "redis://redis:6379/0")
RESULT_BACKEND_URI = os.environ.get("CELERY_RESULT_BACKEND", "redis://redis:6379/0")

app = Celery(
    'worker',
    broker=BROKER_URI,
    result=RESULT_BACKEND_URI
)


@app.task
def name():
    print("milan")