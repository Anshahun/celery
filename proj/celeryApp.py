from celery import Celery
from celery.worker.control import control_command

app = Celery()
app.config_from_object('proj.conf.celeryconfig')

app.conf.update(result_expires=3600, )
res = app.conf.humanize(with_defaults=False, censored=True)

from celery.worker.control import control_command


@control_command(
    args=[('n', int)],
    signature='[N=1]',  # <- used for help on the command-line.
)
def increase_prefetch_count(state, n=1):
    state.consumer.qos.increment_eventually(n)
    return {'ok': 'prefetch count incremented'}

from celery.worker.control import inspect_command

@inspect_command()
def current_prefetch_count(state):
    return {'prefetch_count': state.consumer.qos.value}

if __name__ == '__main__':
    app.start()
