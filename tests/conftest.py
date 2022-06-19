import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager

from .pages.bing_page import BingPage


@pytest.fixture
def chrome_webdriver() -> ChromeDriver:
    """A simple fixture that injects a local chrome driver, this automatically handles service acquisition."""
    with ChromeDriver(service=ChromeService(executable_path=ChromeDriverManager().install())) as driver:
        yield driver


@pytest.fixture
def bing_page(chrome_webdriver) -> BingPage:
    """A simple fixture that yields a Bing page object after navigating to the page."""
    chrome_webdriver.get("https://www.bing.com")
    return BingPage(chrome_webdriver)
