from functools import partial

from selenium.webdriver.common.by import By


class Relocatable:
    """"""

    def __init__(self, by: By, locator: str, many: bool = False) -> None:
        self.locatable = (by, locator)
        self.many = many
        self.transport = None

    def __set_name__(self, owner, name):
        """Allow multiple attributes within the owner class to use instances"""
        self.private_name = f"_{name}"

    def __get__(self, instance, owner):
        """Retreive a single element."""
        if self.transport is None:
            transport = getattr(instance, "driver", None)
            if transport is None:
                raise AttributeError(f"No Such Attribute: `driver` in {instance.__class__.__name__}")
            self.transport = transport
        fn = self.transport.find_elements if self.many is True else self.transport.find_element
        return fn(*self.locatable)

    def __set__(self, obj, value):
        setattr(obj, self.private_name, value)


find = Relocatable
find_all = partial(find, many=True)
