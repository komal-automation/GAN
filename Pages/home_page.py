from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.base_page import BasePage


class HomePage(BasePage):
    """By locatores - OR"""
    JOIN_NOW = (By.CSS_SELECTOR, "a.newUser")

    """constructor of the class"""

    def __init__(self, driver):
        super().__init__(driver)
        #self.driver.get(TestData.BASE_URL)

    """Page Actions Home page"""

    """this is used to get the page title"""
    def get_login_page_title(self, title):
        return self.get_title(title)

    """this is used to click on Join Now link button"""
    def goto_registration(self):
        self.do_click(self.JOIN_NOW)