from celery import shared_task
from celery.utils.log import get_task_logger
from time import sleep
from .celery.inform_using_mail import send_mail_to

sleeplogger = get_task_logger(__name__)

@shared_task(name='my_first_task')
def my_first_task(duration):
    subject= 'Celery'
    message= 'https://medium.com/@juwelariful1/send-mail-in-django-with-gmail-and-smtp-include-celery-and-gmail-configuration-4b07ae4f8542     https://medium.com/swlh/asynchronous-task-with-django-celery-redis-and-production-using-supervisor-ef920725da03'
    receiver= 'yogitakothadia@gmail.com'
    is_task_completed= False
    error=''
    try:
        sleep(duration)
        is_task_completed= True
    except Exception as err:
        error= str(err)
        sleeplogger.error(error)
    if is_task_completed:
        send_mail_to(subject,message,receiver)
    else:
        send_mail_to(subject,error,receiver)
    return('first_task_done')