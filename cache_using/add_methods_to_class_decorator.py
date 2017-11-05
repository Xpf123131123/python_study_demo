class Foo:
    def __init__(self):
        self.x = 42


def add_method_to(instance):
    def decorator(f):
        import types
        # types.MethodType(method, class)
        f = types.MethodType(f, instance)
        # 添加属性：
        # 参数：
        # 1.要添加属性的对象
        # 2.属性的name
        # 3.属性
        setattr(instance, f.__name__, f)
        return f
    return decorator

foo = Foo()

@add_method_to(foo)
def print_x(self):
    print(self.x)


foo.print_x()