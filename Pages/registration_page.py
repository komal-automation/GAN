from Pages.base_page import BasePage
from selenium.webdriver.common.by import By

from Utilities.customLogger import LogGen


class RegistrationPage(BasePage):
    logger = LogGen.loggen()

    """By locatores - OR"""
    PAGE_HEADING = (By.XPATH, "//legend[contains(text(), 'About you')]")
    NEW_USER = (By.CSS_SELECTOR, "a.newUser")
    TITLE = (By.ID, "title")
    FIRST_NAME = (By.ID, "forename")
    LAST_NAME = (By.NAME, "map(lastName)")
    TERM = (By.NAME, "map(terms)")
    JOIN_NOW = (By.ID, "form")
    DATE_OF_BIRTH_ERROR = (By.CSS_SELECTOR, "label[for='dob']")

    """constructor of the class"""
    def __init__(self, driver):
        super().__init__(driver)

    """this is used to get the page title"""
    def get_page_heading(self):
        return self.get_element_text(self.PAGE_HEADING)

    """this is used to get the registration message"""
    def get_user_dob_validation_message(self):
        msg = ""
        if self.is_visible(self.DATE_OF_BIRTH_ERROR):
           msg = self.get_element_text(self.DATE_OF_BIRTH_ERROR)
        return msg

    """this is used to do user's registration"""
    def do_registration(self, title, fname, lname):
        self.logger.info("Filling Title column with " + title)
        self.get_item_from_select(self.TITLE, title)
        self.do_send_keys(self.FIRST_NAME, fname)
        self.do_send_keys(self.LAST_NAME, lname)
        self.logger.info("Check the tickbox for age 18 validity")
        self.do_click(self.TERM)
        self.logger.info("Clicking on the Join now button")
        self.do_click(self.JOIN_NOW)
        self.wait_for_page_load()
        self.logger.info("checking DOB required field validation")
        msg = self.get_user_dob_validation_message()
        return msg