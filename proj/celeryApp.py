from celery import Celery
from kombu import Exchange, Queue
app = Celery()
app.config_from_object('proj.conf.celeryconfig')

app.conf.update(result_expires=3600, )
res = app.conf.humanize(with_defaults=False, censored=True)
app.conf.task_routes = [
    {'proj.tasks.test': {'queue': 'test'}},
    {'proj.tasks.*': {'queue': 'mul','routing_key': 'video.compress'}}
]

app.conf.task_queues = (
    #Queue('test',  Exchange('media'),   routing_key='proj.tasks.test'),
    Queue('mul',  Exchange('media',type='direct'),   routing_key='proj.tasks.mul'),
    #Queue('images',  Exchange('media'),   routing_key='media.image'),
)

if __name__ == '__main__':
    app.start()
