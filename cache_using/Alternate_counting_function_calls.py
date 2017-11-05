class countcalls(object):
    """
    Decorator that keeps track of the number of times a function is called.
    """
    __instances = {}

    def __init__(self, f):
        self.__f = f
        self.__numcalls = 0
        countcalls.__instances[f] = self

    def __call__(self, *args, **kwargs):
        self.__numcalls += 1
        return self.__f(*args, **kwargs)

    def count(self):
        """

        :return: Return the number of times the function f was called.
        """
        return countcalls.__instances[self.__f].__numcalls

    @staticmethod
    def counts():
        """

        :return: Return a dict of {function: # of calls} for all registered functions.
        """
        return dict([(f.__name__, countcalls.__instances[f].__numcalls) for f in countcalls.__instances])

@countcalls
def f():
    print("f called")

@countcalls
def g():
    print("g called")

f()
print(f)
f()
f()

f1 = f
# print(f1)

print(f.count())
assert f.count() is 3

assert f1.count() is 3







