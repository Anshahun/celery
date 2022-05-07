from celery import Task
from celery.worker.request import Request


class MyRequest(Request):
    'A minimal custom request to log failures and hard time limits.'

    def on_timeout(self, soft, timeout):
        super(MyRequest, self).on_timeout(soft, timeout)
        if not soft:
           print(
               'A hard timeout was enforced for task %s',
               self.task.name
           )

    def on_failure(self, exc_info, send_failed_event=True, return_ok=False):
        print(self.__dict__)
        super().on_failure(
            exc_info,
            send_failed_event=send_failed_event,
            return_ok=return_ok
        )
        print(
            'Failure detected for task %s',
            self.task.name
        )

class MyTask(Task):
    Request = MyRequest  # you can use a FQN 'my.package:MyRequest'
    autoretry_for = (Exception,)
    max_retries = 5
    # exponential backoff
    retry_backoff = True
    # sec
    retry_backoff_max = 20
    # 默认为True,若 full_jitter 是 False，则不是随机选取，
    # 而是取最大的补偿时间，也就可能导致多个任务同时再次执行
    retry_jitter = True