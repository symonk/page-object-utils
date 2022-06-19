import typing

from selenium.webdriver.remote.webdriver import ShadowRoot
from selenium.webdriver.remote.webelement import WebElement

FindTypeAlias = typing.Union[WebElement, typing.List[WebElement], ShadowRoot, typing.List[ShadowRoot]]
