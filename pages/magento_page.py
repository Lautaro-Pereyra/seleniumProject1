from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from .base_page import BasePage


class MagentoPage(BasePage):
    ## SIZE ##
    SIZE_XS = (By.ID, "option-label-size-143-item-166")
    SIZE_S = (By.ID, "option-label-size-143-item-167")
    SIZE_M = (By.ID, "option-label-size-143-item-168")
    SIZE_L = (By.ID, "option-label-size-143-item-169")
    SIZE_XL = (By.ID, "option-label-size-143-item-170")

    ## COLOR ##
    COLOR_BLUE = (By.ID, "option-label-color-93-item-50")
    COLOR_ORANGE = (By.ID, "option-label-color-93-item-56")
    COLOR_PURPLE = (By.ID, "option-label-color-93-item-57")



    ## BUTTON ##
    CONTAINER_BUTTON = (By.CLASS_NAME, "product-item")
    BUTTON_CART = (By.XPATH, "//li[1]//div[1]//div[1]//div[4]//div[1]//div[1]//form[1]//button[1]//span[1]")



    def navigate_magento(self):
        self.navigate_to(
            "https://magento.softwaretestingboard.com/")


    def find_button_add_to_cart(self, locator):
        element = self.wait_for_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()
