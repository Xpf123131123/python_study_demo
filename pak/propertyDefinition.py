import sys

def propget(func):
    locals = sys._getframe(1).f_locals
    print(locals)
    name = func.__name__
    prop = locals.get(name)
    if not isinstance(prop, property):
        prop = property(func, doc=func.__doc__)
    else:
        doc = prop.__doc__ or func.__doc__
        prop = property(func, prop.fset, prop.fdel, doc)
    return prop

def propset(func):
    locals = sys._getframe(1).f_locals
    name = func.__name__
    prop = locals.get(name)
    if not isinstance(prop, property):
        prop = property(None, func, doc=func.__doc__)
    else:
        doc = prop.__doc__ or func.__doc__
        prop = property(prop.fget, func, prop.fdel, doc)
    return prop

def propdel(func):
    locals = sys._getframe(1).f_locals
    name = func.__name__
    prop = locals.get(name)
    if not isinstance(prop, property):
        prop = property(None, None, func, doc=func.__doc__)
    else:
        prop = property(prop.fget, prop.fset, func, prop.__doc__)
    return prop

class Example(object):

    @propget
    def myattr(self):
        print('22222')
        return self._half * 2

    @propset
    def myattr(self, value):
        print('11111')
        self._half = value / 2

    @propdel
    def myattr(self):
        print('33333')
        del self._half

ex = Example()
ex.myattr = 123
print(ex.myattr)
del ex.myattr
