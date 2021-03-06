def dump_args(func):
    ""
    argnames = func.func_code.co_varnames[:func.func_code.co_argcount]
    fname = func.func_name

    def echo_func(*args, **kwargs):
        print(fname, ":", ",".join(
            '%s=%r' % entry for entry in zip(argnames, args) + kwargs.items()
        ))
        return func(*args, **kwargs)

    return echo_func

@dump_args
def f1(a, b, c):
    print(a + b + c)


