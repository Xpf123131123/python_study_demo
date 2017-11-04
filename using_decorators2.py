class myDecorator(object):
    def __init__(self, f):
        print("inside mtDecorator.__init__()")
        self.func = f
        # f()

    def __call__(self, *args, **kwargs):
        print("Entering", self.func.__name__)
        self.func(*args, **kwargs)
        print("Exited", self.func.__name__)

@myDecorator
def aFunction(*args, **kwargs):
    print("inside aFunction")

print("Finished decorating aFunction")

aFunction(1, 2, 3, l = 1, m = 2)

