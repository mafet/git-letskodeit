import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time

class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _search_box = "//input[@id='search']"
    _search_button = "//button[@type='submit']"
    _course = "//div[@class='zen-course-list']//h4[contains(text(), '{0}')]"
    _enroll_button = "//button[contains(text(), 'Enroll in Course')]"
    _cc_num = "//input[@placeholder='Card Number']"
    _cc_exp = "//input[@placeholder='MM / YY']"
    _cc_cvc = "//input[@placeholder='Security Code']"
    _submit_enroll = "//button[contains(@class,'sp-buy')]"
    _enroll_error_message = "//li[@class ='card-no cvc expiry text-danger']"

    def enterCourseName(self, name):
        self.sendKeys(name, self._search_box, locatorType="xpath")
        self.elementClick(self._search_button, locatorType="xpath")

    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(locator=self._course.format(fullCourseName), locatorType="xpath")

    def enterCardNum(self, num):
        self.switchFrameByIndex(self._cc_num, locatorType="xpath")
        self.sendKeys(num, self._cc_num, locatorType="xpath")
        self.switchToDefaultContent()

    def enterCardExp(self, exp):
        self.switchFrameByIndex(self._cc_exp, locatorType="xpath")
        self.sendKeys(exp, self._cc_exp, locatorType="xpath")
        self.switchToDefaultContent()

    def enterCardCvc(self, cvc):
        self.switchFrameByIndex(self._cc_cvc, locatorType="xpath")
        self.sendKeys(cvc, self._cc_cvc, locatorType="xpath")
        self.switchToDefaultContent()

    def clickEnrollSubmitButton(self):
        self.elementClick(self._enroll_button, locatorType="xpath")

    def enterCreditCardInformation(self, num, exp, cvc):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCvc(cvc)

    def enrollCourse(self, num="", exp="", cvc=""):
        self.clickEnrollSubmitButton()
        self.scrollWindow("down")
        self.enterCreditCardInformation(num, exp, cvc)
        self.elementClick(self._submit_enroll, locatorType="xpath")

    def verifyEnrollFailed(self):
        self.waitForElement(self._enroll_error_message, locatorType="xpath")
        result = self.isElementPresent(self._enroll_error_message, locatorType="xpath")
        return result





