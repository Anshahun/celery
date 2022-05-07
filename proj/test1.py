import os

from celery.canvas import Signature
from celery.utils.log import get_logger

from proj.tasks import add, mul, dump_context, retry_test, retry_inherit, \
    ignore_test, init_task, error_handler, hello

logger = get_logger(__name__)

def on_raw_message22(body):
    print(body)

if __name__ == '__main__':
    print(add.name)
    print(mul.name)
    #dump_context.delay(1,2, argsrepr='asasd')
    #add.apply_async((1,2),argsrepr='(<secret-x>, <secret-y>)')
    #retry_test.delay()
    #retry_inherit.delay()
    #res = ignore_test.delay()
    #print(res.get(timeout=3))
    #init_task.delay()
    #link_error 只应用于apply_async方法，对link内的异常无效
    #add.apply_async((2, 3), link=add.s(None), link_error=error_handler.s())
    res = hello.apply_async(args=(1,1),expires=5,countdown=1,time_limit=2)
    print(res.get(on_message=on_raw_message22, propagate=False))
    #logger.warning("help me!")
    #s = add.signature((1,2),countdown=3)
    #res = s.apply_async(link=reset_buffers.si())
    #print(res.get())