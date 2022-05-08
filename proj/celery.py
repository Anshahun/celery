from celery import Celery

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
    return {'ok': 'prefetch count incremented'}

from celery.worker.control import inspect_command

@inspect_command(alias='dump_conf',)
def current_prefetch_count(state):
    return {'prefetch_count': 1}

@inspect_command()
def report2(state):
    """Information about Celery installation for bug reports."""
    return {'1':1}

if __name__ == '__main__':
    app.start()
