import contextlib
import time
import typing

from .exceptions import PageNeverReadyException
from .types import CallableAlias


def poll(
    predicate: CallableAlias,
    *args,
    total: float = 30.00,
    ignoring: typing.Iterable[typing.Type[Exception]] = (),
    **kwargs
):
    """Poll some predicate ignoring exceptions for a duration, until it evaluates to True."""
    now = time.time()
    finish = now + total
    while time.time() < finish:
        with contextlib.suppress(*ignoring):
            result = predicate(*args, **kwargs)
            if result is True:
                return
    raise PageNeverReadyException("Page failed to be in it's `loaded` state.")
