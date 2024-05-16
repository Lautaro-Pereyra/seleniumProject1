import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pages.magento_page import MagentoPage


@pytest.fixture(scope="session")
def browser():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://magento.softwaretestingboard.com/")
    yield driver
    driver.quit()


@pytest.fixture
def magento_page(browser):
    return MagentoPage(browser)
