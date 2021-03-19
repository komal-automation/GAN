from selenium import webdriver
from Pages.registration_page import RegistrationPage
from Pages.home_page import HomePage


"""this is used to list of all the pages."""
"""this is included in fixcture class, no need to import in each page."""
class GANPages:
    """Constructor of the class"""
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.home  = HomePage(driver)
        self.registration = RegistrationPage(driver)

    """this is used to redirect / go to specific page"""
    def go_to(self, url: str):
        return self.driver.get(url)




