from setup.celery import APP

@APP.task
def hello_world():
    print("Hello World")