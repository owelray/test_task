import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'reset_upvotes_every_midnight': {
        'task': 'test_task.upvotes_reset',
        'schedule': crontab(minute=0, hour=0),  # triggers daily at midnight
    },
}
