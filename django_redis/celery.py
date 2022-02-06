import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_redis.settings")

app = Celery("django_redis")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")


app.conf.beat_schedule = {
    "check_messages_10s": {
        "task": "chat.tasks.check_messages",
        "schedule": 10.0,
    },
}

# Load task modules from all registered Django apps.
app.autodiscover_tasks()
