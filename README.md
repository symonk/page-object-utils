# page-object-utils

A Lightweight utility library that offers an assortment of page object utilities to make writing
and maintaining selenium code easier.

#### Automatic Relocation on lookup
------------------------------------

No more stale elements, descriptor protocol backed element lookups happen implicitly and automatically
when accessing an element.  This keeps tests more accurate and prevents staleness.

```python
from page_object_utils import ElementContainer
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BingPage:
    """A simple page object that demonstrates the use of element containers."""

    search_box: WebElement = ElementContainer(By.ID, "sb_form_q")
    search_button: WebElement = ElementContainer(By.ID, "search_icon")

    def __init__(self, driver):
        self.driver = driver

    def perform_search(self, term: str) -> ...:
        self.search_box.send_keys(term)
        self.search_button.click()
```
