from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from page_object_utils import ElementContainer


class BingPage:
    """A simple page object that demonstrates the use of element containers."""

    search_box: WebElement = ElementContainer(By.ID, "sb_form_q")
    search_button: WebElement = ElementContainer(By.ID, "search_icon")

    def __init__(self, driver):
        self.driver = driver

    def perform_search(self, term: str) -> ...:
        self.search_box.send_keys(term)
        self.search_button.click()
