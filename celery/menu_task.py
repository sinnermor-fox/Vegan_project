from app import celery


@celery.task
def my_background_task(arg1, arg2):
    print("I'm celery task")
    result = 'CELERY !'
    return result


task = my_background_task.delay(10, 20)
