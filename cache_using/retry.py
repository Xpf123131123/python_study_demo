import time
import math

def retry(tries, delay=3, backoff=2):
    '''Retries a function or method until it returns True.

    delay sets the initial delay in seconds, and backoff sets the factor by which
    the delay should lengthen after each failure. backoff must be greater than 1,
    or else it isn't really a backoff. tries must be at least 0, and delay
    greater than 0.
    '''
    if backoff <= 1:
        raise ValueError('backoff must be greater than 1')
    tries = math.floor(tries)
    if tries < 0:
        raise ValueError('tries must be 0 or greater')
    if delay <= 0:
        raise ValueError('delay must be greater than 0')

    def deco_retry(f):
        def f_retry(*args, **kwargs):
            # make mutable
            mtries, mdelay = tries, delay

            rv = f(*args, **kwargs)
            while mtries > 0:
                if rv is True:
                    return True
                mtries -= 1
                time.sleep(mdelay)
                mdelay *= backoff

                rv = f(*args, **kwargs)
            return False
        return f_retry
    return deco_retry
