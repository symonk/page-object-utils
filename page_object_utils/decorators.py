from .types import CallableAlias


def loaded(fn: CallableAlias) -> CallableAlias:
    """A decorated method used as a callback to determine if a page is ready.  This method is
    implicitly polled after an instance has been created until it returns True."""
    fn._loaded = True  # type: ignore
    return fn
