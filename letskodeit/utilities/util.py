import logging
import random
import string
import time
import traceback
import utilities.custom_logger as cl


class Util():

    log = cl.customLogger(logging.INFO)

    def sleep(self, sec, info=""):
        if info is not None:
            self.log.info("Wait:: " + str(sec) + " seconds for " + info)
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()

    def getAlphaNumeric(self, length, type='letters'):
        alpha_num = ''
        if type == 'lower':
            case = string.ascii_lowercase
        elif type == 'upper':
            case = string.ascii_uppercase
        elif type == 'digits':
            case = string.digits
        elif type == 'mix':
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))

    def getUniqueName(self, charCount=10):
        return self.getAlphaNumeric(charCount, 'lower')

    def getUniqueNameList(self, listSize=5, itemLength=None):
        nameList = []
        for i in range(0, listSize):
            nameList.append(self.getUniqueName(itemLength[i]))
        return nameList


    def verifyTextContains(self, actualText, expectedText):
        self.log.info("Actual text of web page: " + actualText)
        self.log.info("Expected text of web page: " + expectedText)
        if actualText.lower() in expectedText.lower():
            self.log.info("!!!Text contains: PASS!!!")
            return True
        else:
            self.log.info("!!!Text contains: FAIL!!!")
            return False

    def verifyTextMatch(self, actualText, expectedText):
        self.log.info("Actual text of web page: " + actualText)
        self.log.info("Expected text of web page: " + expectedText)
        if actualText.lower() == expectedText.lower():
            self.log.info("!!!Text match: PASS!!!")
            return True
        else:
            self.log.info("!!!Text match: FAIL!!!")
            return False

    def verifyListMatch(self, actualList, expectedList):
        return set(expectedList) == set(actualList)

    def verifyListContains(self, actualList, expectedList):
        for item in expectedList:
            if item not in actualList:
                return False
            else:
                return True
