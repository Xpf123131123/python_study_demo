class Example(object):
    # @apply
    def myattr(self):
        # doc = '''Thi'''
        def fget(self):
            return self._half * 2

        def fset(self, value):
            self._half = value / 2

        def fdel(self):
            del self._half

        return property(**locals())

    myattr = myattr()
