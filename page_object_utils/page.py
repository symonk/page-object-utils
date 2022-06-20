import inspect
import typing

from selenium.webdriver.remote.webdriver import WebDriver

from .polling import poll


class Page:
    """A Base Page Object."""

    _callbacks: typing.Dict[str, typing.Any] = {}

    def __init_subclass__(cls):
        super().__init_subclass__()
        loaded = next(iter(inspect.getmembers(cls, lambda fn: hasattr(fn, "_loaded"))), None)
        if loaded is not None:
            cls._callbacks["loaded"] = loaded[1]  # Only need the callable.

    def __init__(self, driver: WebDriver) -> None:
        """Register the driver and apply any loaded callbacks."""
        self.driver = driver
        loaded = self._callbacks.get("loaded", None)
        if loaded is not None:
            _ = poll(loaded, self)
