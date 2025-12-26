import os
from celery import Celery

os.environ.setdefault('Django_SETINGS_MODULE', 'config.settings')

app = Celery('config')
app.config_from_object('django.config:settings', namespace='CELERY')
app.autodiscover_tasks()
