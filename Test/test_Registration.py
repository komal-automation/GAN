from Test.base_test import BaseTest
from Config.config import TestData
from Utilities.customLogger import LogGen


class Test_Registration(BaseTest):
    logger = LogGen.loggen()

    def test_registration_nav(self):
        self.logger.info("***** Test Navigation to Join page *****")
        self.logger.info("Loading Site home page")
        self.pages.go_to(TestData.BASE_URL)
        self.logger.info("Navigating to Join/Registation page")
        self.pages.home.goto_registration()
        self.logger.info("Fetching Join/Registation page About section heading")
        page_heading = self.pages.registration.get_page_heading()
        self.logger.info("Test Pass/Fail:" + page_heading)
        assert page_heading == 'About you'

    def test_register_new_user(self):
        self.logger.info("***** Test User registration *****")
        self.logger.info("Loading Site home page")
        self.pages.go_to(TestData.BASE_URL)
        self.logger.info("Navigating to Join/Registation page")
        self.pages.home.goto_registration()
        self.logger.info("Now filling User data in the About me section")
        status_msg = self.user_registration()

        assert status_msg == TestData.REQUIRED_FIELD_MESSAGE

    def _test_register_existing_user(self):
        self.pages.home.goto_myaccount()
        self.pages.signIn.goto_register()
        status_msg = self.user_registration()
        assert status_msg == TestData.REQUIRED_FIELD_MESSAGE

    def user_registration(self):
        status_msg = self.pages.registration.do_registration(TestData.NEW_USER_TITLE, TestData.NEW_USER_FNAME, TestData.NEW_USER_LNAME)
        return status_msg

