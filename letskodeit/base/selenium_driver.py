from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging
import time
import os

class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)
    def __init__(self, driver):
        self.driver = driver

    def screenShot(self, resultMessage):
        """Takes screenshot of current web page"""
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "..\\screenshots\\"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)
        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot saved to directory: " + destinationFile)
        except:
            self.log.error("### Exception occurred when taking screenshot" )
            print_stack()

    def getTitle(self):
        return self.driver.title

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "name":
            return By.NAME
        else:
            self.log.info("locator type is not supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType =self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element Found with locator: " + locator +
                          " and locator type: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator +
                          " and locator type: " + locatorType)
        return element

    def getElementList(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.log.info("Element list found with locator " + locator +
                          " and locator type " + locatorType)
        except:
            self.log.info("Element not found  with locator " + locator +
                          " and locator type " + locatorType)
        return element


    def elementClick(self, locator="", locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator +
                          " and locator type:" + locatorType )
        except:
            self.log.info("Cannot click on the element")
            print_stack()

    def sendKeys(self, data, locator, locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Send keys on element with locator: " + data +
                          " and locator type:" + locatorType)
        except:
            self.log.info("Cannot send keys on the element")
            print_stack()

    def getText(self, locator="", locatorType="id", element=None, info=""):
        try:
            if locator:
                self.log.debug("In locator condition")
                element = self.getElement(locator, locatorType)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            elif len(text) != 0:
                self.log.info("Getting text on the element " + info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text


    def isElementPresent(self, locator, locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                print("Element found")
                return True
            else:
                return False
        except:
            print("Element not found")
            return False

    def isELementDisplayed(self, locator="", locatorType="id", element=None):
        isDisplayed = False
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed with locator " + locator +
                              " and locator type: " + locatorType)
            else:
                self.log.info("Element is NOT displayed with locator " + locator +
                              " and locator type: " + locatorType)
            return isDisplayed
        except:
            print("Element not found")
            return False

    def checkElementsPresent(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element(s) found")
                return True
            else:
                self.log.info("No element found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def waitForElement(self, locator, locatorType="id",
                               timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType,
                                                             locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element

    def getElementAttributeValue(self, attribute, element=None, locator="", locatorType=""):
        if locator:
            element = self.getElement(locator=locator, locatorType=locatorType)
        value = element.get_attribute(attribute)
        return value

    def isEnabled(self, locator, locatorType="id", info=""):
        element = self.getElement(locator=locator, locatorType=locatorType)
        enabled = False
        try:
            attributeValue = self.getElementAttributeValue(element=element, attribute="disabled")
            if attributeValue is not None:
                enabled = element.is_enabled()
            else:
                value = self.getElementAttributeValue(element=element, attribute="class")
                self.log.info("Attirbute Value from Application Web UI ---> :: " + value)
                enable = not ("disbled" in value)
            if enabled:
                self.log.info("Element :: " + info + "is enabled")
            else:
                self.log.info("Element :: " + info + "is not enabled")
        except:
            self.log.error("Element :: " + info + " state could not be found")
        return enabled

    def scrollWindow(self, direction="up"):
        if direction == "up":
            self.driver.execute_script("window.scrollBy(0, -1000);")
        elif direction == "down":
            self.driver.execute_script("window.scrollBy(0, 1000);")

    def switchToiFrame(self, id="", name="", index=0):
        if id:
            self.driver.switch_to.frame(id)
        elif name:
            self.driver.switch_to.frame(name)
        else:
            self.driver.switch_to.frame(index)


    def switchToDefaultContent(self):
        self.driver.switch_to.default_content()


    def switchFrameByIndex(self, locator="", locatorType="xpath"):
        result = False
        try:
            iframe_list = self.getElementList("//iframe", locatorType="xpath")
            self.log.info("Length of iframe list: ")
            self.log.info(str(len(iframe_list)))
            for i in range(len(iframe_list)):
                self.switchToiFrame(index=iframe_list[i])
                result = self.isElementPresent(locator, locatorType)
                if result:
                    self.log.info("Found in iframe index" + str(i))
                    break
                self.switchToDefaultContent()
            return result
        except:
            self.log.info("Iframe not found")
            return result


