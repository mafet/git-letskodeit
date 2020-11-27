from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
from traceback import print_stack

class TestStatus(SeleniumDriver):
    log = cl.customLogger(logging.INFO)
    def __init__(self, driver):
        super(TestStatus, self).__init__(driver)
        self.resultList = []

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("### Verification Successful ### " + resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.info("### Verification Failed ### " + resultMessage)
                    self.screenShot(resultMessage)
            else:
                self.resultList.append("FAIL")
                self.log.info("### Verification Failed ### " + resultMessage)
                self.screenShot(resultMessage)
        except:
            self.resultList.append("FAIL")
            self.log.info("!!! Exception Occurred !!!" + resultMessage)
            self.screenShot(resultMessage)
            print_stack()


    def mark(self, result, resultMessage):
        """
        Mark the result of the verification point in a test case
        """
        self.setResult(result, resultMessage)

    def markFinal(self, testName, result, resultMessage):
        self.setResult(result, resultMessage)
        if "FAIL" in self.resultList:
            self.log.error(testName + " test failed")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(testName + " was successful")
            self.resultList.clear()
            assert True == True