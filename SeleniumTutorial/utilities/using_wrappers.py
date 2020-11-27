from selenium import webdriver
from utilities.handy_wrappers import HandyWrappers
import time

class UsingWrappers():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(executable_path="C://Users//Maria.Misa//workspace_python//drivers//chromedriver")
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)
        driver.get(baseUrl)

        textField1 = hw.getElement("name")
        textField1.send_keys("test")
        time.sleep(3)

        textField2 = hw.getElement("//input[@id ='name']", locatorType="xpath")
        textField2.clear()

ff = UsingWrappers()
ff.test()