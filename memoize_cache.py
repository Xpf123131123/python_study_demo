import collections
import functools

# 缓存
class memoized(object):

    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        # isinstance 判断元素是不是某种类型
        if not isinstance(args, collections.Hashable):
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value
    # 展示给开发人员当前类的信息 __str__
    def __repr__(self):
        '''Return the function's docstring.'''
        return self.func.__doc__

    def __get__(self, instance, owner):
        '''Support instance methods.'''
        return functools.partial(self.__call__, instance)

@memoized
def fibonacci(n):
    "Return the nth fibonacci number."
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(30))
