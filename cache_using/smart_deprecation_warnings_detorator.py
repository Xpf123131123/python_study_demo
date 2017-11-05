import warnings
import functools

def deprecated(func):
    """
    This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emitted
    when the function is used.
    """
    @functools.wraps(func)
    def new_func(*args, **kwargs):
        warnings.warn_explicit("Call to deprecated function {}.".format(func.__name__),
                               category=DeprecationWarning, filename=func.__code__.co_filename,
                               lineno=func.__code__.co_firstlineno + 1)
        return func(*args, **kwargs)
    return new_func

@deprecated
def my_func():
    pass

# @other_decorator_must_be_upper
@deprecated
def my_func():
    pass