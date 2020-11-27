from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class HiddenElements():
    def test(self):
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(executable_path="C://Users//Maria.Misa//workspace_python//drivers//chromedriver")
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(4)
        hiddenText = driver.find_element_by_id("displayed-text")
        textBoxState = hiddenText.is_displayed()
        print("Is text box visible?" + str(textBoxState))
        time.sleep(3)

        #click hide
        driver.find_element_by_id("hide-textbox").click()
        textBoxState = hiddenText.is_displayed()
        print("Is text box visible after clicking hide?" + str(textBoxState))
        time.sleep(3)

        #click show
        driver.find_element_by_id("show-textbox").click()
        textBoxState = hiddenText.is_displayed()
        print("Is text box visible after clicking hide?" + str(textBoxState))
        time.sleep(3)

        driver.quit()



    def testExpedia(self):
        baseURL = "https://www.expedia.com"
        driver = webdriver.Chrome(executable_path="C://Users//Maria.Misa//workspace_python//drivers//chromedriver")
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(4)
        flightTab = driver.find_element_by_id("tab-flight-tab-hp")
        flightTab.click()
        time.sleep(3)
        dropdownElement = driver.find_element_by_id("flight-age-select-1-hp-flight")
        elementState = dropdownElement.is_displayed()
        print("Expedia: Is dropdown visible?" + str(elementState))

ff = HiddenElements()
ff.test()
ff.testExpedia()