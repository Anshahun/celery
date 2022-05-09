from celery import Celery
from celery.schedules import crontab

from .celeryApp import app


# app.conf.beat_schedule = {
# Executes every Monday morning at 7:30 a.m.
# 'add-every-monday-morning': {
#    'task': 'proj.schtasks.add',
#    'schedule': crontab(minute='*/1'),
#    'args': (16, 16),
# },
# }

@app.task
def test(arg):
    print(arg)


@app.task
def add(x, y):
    z = x + y
    print(z)

#添加括号
@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(minute='*/1'),
        test.s('Happy Mondays!'),
    )
