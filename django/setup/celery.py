from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')

APP = Celery('stock')

APP.config_from_object('django.conf:settings', namespace='CELERY')

APP.autodiscover_tasks()

@APP.task(bind=True)
def debug_task(self):
    """
    Debug Task.
    """
    print(f'Request: {self.request!r}')
