from celery import Celery

app = Celery()
app.config_from_object('proj.conf.celeryconfig')

app.conf.update(result_expires=3600,)
res = app.conf.humanize(with_defaults=False, censored=True)
print(res)
if __name__ == '__main__':
    app.start()