"""
线程锁 装饰器
"""

def synchronized(lock):
    """Synchronization decorator."""

    def wrap(f):
        def new_function(*args, **kwargs):
            lock.acquire()
            try:
                return f(*args, **kwargs)
            finally:
                lock.release()
        return new_function
    return wrap

# example
from threading import Lock
my_lock = Lock()

@synchronized(my_lock)
def criticall(*args):
    pass

