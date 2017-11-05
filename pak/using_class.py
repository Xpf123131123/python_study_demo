# encoding=UTF-8

a = '12313123123'
print(globals())
# class testClass:
#     def __init__(self, name):
#         self.name = name
#
#     def __getitem__(self, item):
#
#         return self.name
#
#
# test = testClass('xpf')
#
# print(test['name'])



def enhanced(meth):
    def new(self, y):
        print("I am enhanced")
        return meth(self, y)
    return new

def anch(pl):

    print(pl)
    def doSomethingBefore(self, y):
        print('kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
        return pl(self, y)
    return doSomethingBefore
    # def enhanced(meth):
    #     def new(self, y):
    #         print("I am enhanced")
    #         return meth(self, y)
    #     return new

#
class C:
    @classmethod
    def foo(cls, y):
        print('classmethod', cls, y)
    # foo = classmethod(foo)

    @anch
    def bar(self, x):
        print("some method says:", x)

    def bar2(self, x):
        print("some method says:", x)

    def bar1(self, x):
        print('I am enhanced')
        self.bar2(x)
    # bar = enhanced(bar)

c = C()
c.bar(10)
c.bar1(13)
# c.bar(10)
C.foo(15)


def arg_sayer(what):
    def what_sayer(meth):
        print(meth)
        def new(self, *args, **kws):
            print(what)
            return meth(self, *args, **kws)
        return new
    return what_sayer

def FooMaker(word):
    class Foo(object):
        @arg_sayer(word)
        def say(self): pass
    return Foo()

foo1 = FooMaker('this')
foo2 = FooMaker('that')
# foo1.say()
# foo2.say()
print(type(foo1))
# foo1.say()
print(type(foo2))
# foo2.say()

