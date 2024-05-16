from selenium.webdriver.common.by import By
from .base_page import BasePage


class MagentoPage(BasePage):
    SELECT_SIZE = (By.ID, "option-label-size-143-item-166")

    def click_size(self):
        select_size = self.wait_for_element(self.SELECT_SIZE)
        select_size.click()
