from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from selenium_annotate import find


# Todo: Use a local page; this reliant upon a real website is lackluster but ok for now.
class BingPage:

    search_box: WebElement = find(By.ID, "sb_form_q")
    search_button: WebElement = find(By.ID, "search_icon")

    def __init__(self, driver):
        self.driver = driver

    def perform_search(self, term: str) -> ...:
        """Everytime a find descriptor is accessed it will use the underlying webdriver
        (or element and subsequently its parent driver) to relocate the element automatically.
        This helps to erradicate staleness and other issues

        This is a trivial example; blindly calling other raw selenium methods without creating
        robust reusable code around them can cause other problems.
        """
        self.search_box.send_keys(term)
        self.search_button.click()
