import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cut_link.settings')

app = Celery('cut_link')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'update-db-and-clean-cache-every-hour': {
        'task': 'shortener.tasks.update_db_and_clean_cache',
        'schedule': crontab()
    },
    'remove-unused-links-every-day': {
        'task': 'shortener.tasks.remove-unused-links',
        'schedule': crontab(minute=0, hour=0)
    },
}
