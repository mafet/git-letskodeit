from base.basepage import BasePage
import time
import utilities.custom_logger as cl
import logging

class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _home = "HOME"
    _my_courses = "MY COURSES"
    _all_courses = "ALL COURSES"
    _support = "SUPPORT"
    _user_icon = "//div//img[@src= '/images/default-user-profile-pic.png']"
    _sign_in = "SIGN IN"

    def navigateToAllCourses(self):
        self.elementClick(locator=self._all_courses, locatorType="link")

    def navigateToMyCourses(self):
        self.elementClick(locator=self._my_courses, locatorType="link")

    def navigateToHome(self):
        self.elementClick(locator=self._home, locatorType="link")

    def navigateToSupport(self):
        self.elementClick(locator=self._support, locatorType="link")

    def navigateToUserSettings(self):
        userSettingsElement = self.waitForElement(locator=self._user_icon,
                                                  locatorType="xpath", pollFrequency=1)
        self.elementClick(element=userSettingsElement)

    def navigateToSignIn(self):
        self.elementClick(locator=self._sign_in, locatorType="link")

