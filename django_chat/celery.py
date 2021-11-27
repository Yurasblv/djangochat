import os
from celery.schedules import crontab
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_chat.settings')
app = Celery('django_chat')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
