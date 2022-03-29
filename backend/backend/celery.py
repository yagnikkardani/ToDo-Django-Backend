from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from todo.tasks import my_first_task

os.environ.setdefault('DJANGO_SETTINGS_MODULE','backend.settings')
app = Celery('backend')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
my_first_task.delay(2)
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))