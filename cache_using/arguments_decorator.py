import functools, inspect

def decorator(func):
    ''' Allow to use decorator either with arguments or not '''

    def isFuncArg(*args, **kw):
        return len(args) == 1 and len(kw) == 0 and \
               (inspect.isfunction(args[0]) or isinstance(args[0], type))

    if isinstance(func, type):
        def class_wrapper(*args, **kw):
            if isFuncArg(*args, **kw):
                return func()(*args, **kw)
            return func(*args, **kw)
        class_wrapper.__name__ = func.__name__
        class_wrapper.__module__ = func.__module__
        return class_wrapper

    @functools.wraps(func)
    def func_wrapper(*args, **kw):
        if isFuncArg(*args, **kw):
            return func(*args, **kw)

        def functor(userFunc):
            return func(userFunc, *args, **kw)

        return functor
    return func_wrapper



@decorator
def apply(func, *args, **kw):
    return func(*args, **kw)

@decorator
class apply:
    def __init__(self, *args, **kw):
        self.args = args
        self.kw = kw

    def __call__(self, func):
        return func(*self.args, **self.kw)


@apply
def test():
    return 'test'

@apply(2, 3)
def test(a, b):
    return a + b

assert test is 5

# print(test)
@decorator
def my_property(getter, *, setter=None, deleter=None,doc=None):
    return property(getter, setter, deleter, doc)
