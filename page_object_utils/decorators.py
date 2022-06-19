import functools
from .types import CallableAlias


def ready(fn: CallableAlias) -> CallableAlias:
    """ A decorated method used as a callback to determine if a page is ready.  This method is
    implicitly polled after an instance has been created until it returns True."""
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper

