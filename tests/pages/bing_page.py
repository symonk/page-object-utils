from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from page_object_utils import Page, Relocatable, loaded


class BingPage(Page):
    """A simple page object that demonstrates the use of element containers.
    Each time any of the Relocatable descriptors are accessed they are always
    re-acquired from the underlying driver instance."""

    search_box: WebElement = Relocatable(By.ID, "sb_form_q")
    search_button: WebElement = Relocatable(By.ID, "search_icon")

    @loaded
    def _(self) -> bool:
        """A predicate that determines if the page is loaded and should continue."""
        return self.driver.current_url.startswith("https://2www.bing.com")

    def __init__(self, driver):
        super().__init__(driver)

    def perform_search(self, term: str) -> ...:
        self.search_box.send_keys(term)
        self.search_button.click()
