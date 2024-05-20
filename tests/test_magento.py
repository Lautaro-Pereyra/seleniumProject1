import time

import pytest



@pytest.mark.magento
def test_click_en_size(magento_page):
    magento_page.navigate_magento()
    magento_page.click(magento_page.SIZE_XS)


@pytest.mark.magento
def test_click_en_color(magento_page):
    magento_page.click(magento_page.COLOR_BLUE)


@pytest.mark.magento
def test_find_and_button_add_to_cart(magento_page):
    magento_page.find_button_add_to_cart(magento_page.CONTAINER_BUTTON)
    time.sleep(5)


@pytest.mark.magento
def test_click_button_cart(magento_page):
    magento_page.click(magento_page.BUTTON_CART)
    time.sleep(5)
