import warnings

def ignore_deprecation_warning(func):
    """
    This is a decorator which can be used to ignore
    deprecationwarning occurring in a function
    :param func:
    :return:
    """
    def new_func(*args, **kwargs):
        with warnings.catch_warnings():
            warnings.filterwarnings('ignore', category=DeprecationWarning)
            return func(*args, **kwargs)

    new_func.__name__ = func.__name__
    new_func.__doc__ = func.__doc__
    new_func.__dict__.update(func.__dict__)
    return new_func

@ignore_deprecation_warning
def some_function_raising_deprecation_warning():
    warnings.warn('This is a deprecation warning.', category=DeprecationWarning)

class SomeClass:
    @ignore_deprecation_warning
    def some_method_raising_deprecation_warning(self):
        warnings.warn('This is a deprecation warning.', category=DeprecationWarning)


some_function_raising_deprecation_warning()