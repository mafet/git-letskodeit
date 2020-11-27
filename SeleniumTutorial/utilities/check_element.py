from selenium import webdriver
from utilities.handy_wrappers import HandyWrappers
from selenium.webdriver.common.by import By
import time

class UsingWrappers():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(executable_path="C://Users//Maria.Misa//workspace_python//drivers//chromedriver")
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)
        driver.get(baseUrl)

        elementResult = hw.isElementPresent("name", By.ID)
        print(str(elementResult))

        elementResult2 = hw.checkElementsPresent("//input[@id ='namess']", By.XPATH)
        print(str(elementResult2))

ff = UsingWrappers()
ff.test()