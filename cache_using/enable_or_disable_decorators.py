def unchanged(func):
    "This decorator doesn't add any behavior"
    return func

def disabled(func):
    "This decorator disables the provided function, and does nothing"
    def empty_func(*args, **kwargs):
        pass
    return empty_func

enabled = unchanged

GLOBAL_ENAZBLE_FLAG = True

state = enabled if GLOBAL_ENAZBLE_FLAG else disabled

@state
def special_function_foo():
    print("function was enabled")

