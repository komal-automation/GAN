from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from Utilities.customLogger import LogGen

"""This class is the parent of all pages"""
"""it contains all the generic methods and the utilities for all the pages"""


class BasePage:
    logger = LogGen.loggen()

    """Constructor of the class"""
    def __init__(self, driver):
        self.driver = driver
        self.delay = 15

    """this is used to click the element"""
    def do_click(self, by_locator):
        wait = WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located(by_locator))
        self.driver.find_element(*by_locator).click()

    """this is used to enter the value for the element"""
    def do_send_keys(self, by_locator, text):
        element = WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located(by_locator))
        element.clear()
        element.send_keys(text)

    """this is used to get the element text"""
    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located(by_locator))
        return element.text

    """this will check weather element is visible or not"""
    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    """this is used to get the page title"""
    def get_title(self,title):
        WebDriverWait(self.driver, self.delay).until(EC.title_is,'title')
        return self.driver.title

    """this is used to wait for page load"""
    def wait_for_page_load(self):
        WebDriverWait(self.driver, self.delay).until(EC.url_changes)

    """this is used to get the object of the element"""
    def get_element(self, by_locator):
        element = WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located(by_locator))
        return element

    def get_item_from_select(self, by_locator, select_text):
        element = WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located(by_locator))
        Select(element).select_by_visible_text(select_text)
        self.driver.find_element(*by_locator).click()