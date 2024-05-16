import pytest
from pages.magento_page import MagentoPage


def test_click_en_size(magento_page):
    magento_page.click_size()
