from .meta import PageMeta


class Page(metaclass=PageMeta):
    """A base class for pages, similar to Django's Model."""
    def __new__(cls, *args, **kwargs):
        ...

    def __call__(self, *args, **kwargs) -> ...:
        ...
