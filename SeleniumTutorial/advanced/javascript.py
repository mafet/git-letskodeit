from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Javascript():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(executable_path="C://Users//Maria.Misa//workspace_python//drivers//chromedriver")
        driver.execute_script("window.location = 'https://letskodeit.teachable.com/p/practice';")
        driver.implicitly_wait(3)

        element = driver.execute_script("return document.getElementById('name');")
        element.send_keys("Test")
        driver.implicitly_wait(5)


cc = Javascript()
cc.test()