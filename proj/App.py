from celery import Celery

if __name__ == '__main__':
    app = Celery()
    app.config_from_object('proj.conf.celeryconfig')
    res = app.conf.humanize(with_defaults=False, censored=True)
    print(res)