# page-object-utils

A Lightweight utility library that offers an assortment of page object utilities to make writing
and maintaining selenium code easier.

Page Object Utils is currently in very early alpha, it is not fit for use - please refrain from opening
issues as at present most things are placeholder and or dummy implementations.


#### Automatic Relocation on lookup
------------------------------------
No more stale elements, descriptor protocol backed element lookups happen implicitly and automatically
when accessing an element.  This keeps tests more accurate and prevents staleness.

```python
from page_object_utils import Relocatable
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BingPage:
    """A simple page object that demonstrates the use of element containers."""

    search_box: WebElement = Relocatable(By.ID, "sb_form_q")
    search_button: WebElement = Relocatable(By.ID, "search_icon")

    def __init__(self, driver):
        self.driver = driver

    def perform_search(self, term: str) -> ...:
        self.search_box.send_keys(term)
        self.search_button.click()
```

-----

#### Built in Page Readiness
-----------------------------

Automatically wait until a page has met some sort of readiness predicate, simply
decorate any method with `@ready`.  Let's build on the previous example.  Here we
mark our page object with `@Page` this registers the page with page-object-utils
as a user defined page object and we decorate a method with `@ready`.  page-object
utils will wait until this predicate is true automatically before continuing:

```python
from page_object_utils import Relocatable
from page_object_utils import Page
from page_object_utils import ready
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


@Page
class BingPage:
    """A simple page object that demonstrates the use of element containers."""

    search_box: WebElement = Relocatable(By.ID, "sb_form_q")
    search_button: WebElement = Relocatable(By.ID, "search_icon")

    @ready
    def _(self) -> bool:
        """Any predicate you desire."""
        return self.driver.url == "https://www.bing.com"

    def __init__(self, driver):
        self.driver = driver

    def perform_search(self, term: str) -> ...:
        self.search_box.send_keys(term)
        self.search_button.click()
```
