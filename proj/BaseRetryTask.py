import celery

from proj.Custom import MyRequest


class BaseTaskWithRetry(celery.Task):
    autoretry_for = (Exception,)
    max_retries = 5
    # exponential backoff
    retry_backoff = True
    # sec
    retry_backoff_max = 20
    # 默认为True,若 full_jitter 是 False，则不是随机选取，
    # 而是取最大的补偿时间，也就可能导致多个任务同时再次执行
    retry_jitter = True
    Request=MyRequest
    serializer='pickle'


    # default_retry_delay =20


    @property
    def cache(self):
        if self._cache is None:
            print('make cache')
            self._cache = ['a', 'b', 'c']
        return self._cache
