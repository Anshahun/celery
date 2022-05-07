from tasks import add
from celery import Celery

if __name__ == '__main__':
    result: object = add.delay(4,4)
    print(result.get(timeout=1))