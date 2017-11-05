class countCalls(object):
    """Decorator that keeps track of the number
    of times a function is called."""

    __instances = {}

    def __init__(self, f):
        self.__f = f
        self.__numcalls = 0
        countCalls.__instances[f] = self

    def __call__(self, *args, **kwargs):
        self.__numcalls += 1
        return self.__f(*args, **kwargs)

    @staticmethod
    def count(f):
        """

        :param f:
        :return: Return the number of times the function f was called.
        """
        return countCalls.__instances[f].__numcalls

    @staticmethod
    def counts():
        """

        :return: Return a dict of {function: # of calls} for all registered functions.
        """
        return dict([(f, countCalls.count(f)) for f in countCalls.__instances])

