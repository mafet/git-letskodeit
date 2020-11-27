from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Get():
    def getText(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(executable_path="C://Users//Maria.Misa//workspace_python//drivers//chromedriver")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        textElement = driver.find_element_by_id("opentab")
        print("This is the text: " + textElement.text)
        time.sleep(3)
        driver.quit()

    def getAttribute(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(executable_path="C://Users//Maria.Misa//workspace_python//drivers//chromedriver")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        textElement = driver.find_element_by_id("alertbtn")
        result = textElement.get_attribute("class")
        print("This is the attribute: " + result)
        time.sleep(3)
        driver.quit()

ff = Get()
ff.getText()
ff.getAttribute()


