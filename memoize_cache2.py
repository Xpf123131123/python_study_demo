class memoize(dict):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        return self[args]

    def __missing__(self, key):
        result = self[key] = self.func(*key)
        return result

@memoize
def foo(a, b):
    return a * b

# foo(2, 4)
print(foo(2, 4))
print(foo)
