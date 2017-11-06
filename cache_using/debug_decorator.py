import sys

WHAT_TO_DEBUG = set(['io', 'core'])

class debug:
    def __init__(self, aspects=None):
        self.aspects = set(aspects)

    def __call__(self, f):
        if self.aspects & WHAT_TO_DEBUG:
            def newf(*args, **kwargs):
                print(sys.stderr, f.__name__, args, kwargs)
                f_result = f(*args, **kwargs)
                print(sys.stderr, f.__name__, "returned", f_result)
                return f_result
            newf.__doc__ = f.__doc__
            return newf
        else:
            return f

@debug(['io'])
def prn(x):
    print(x)

@debug(['core'])
def mult(x, y):
    return x * y

# print()
mult(2, 2)

prn(10)
