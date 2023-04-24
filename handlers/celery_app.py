from datetime import date

from celery import Celery
from celery.schedules import crontab

from database.session import SessionLocal
from handlers.utils import create_rate

celery = Celery('tasks', broker='redis://localhost:6379')

celery.conf.beat_schedule = {
    'update-rate-every-day': {
        'task': 'handlers.celery_app.create_rate_task',
        'schedule': crontab(minute=0, hour=0),
    },
}


@celery.task
def create_rate_task():
    with SessionLocal() as db:
        create_rate(date.today(), db)
