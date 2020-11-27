from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class WindowSize():
    def test(self):
        baseUrl = "https://www.fool.com/"
        driver = webdriver.Chrome(executable_path="C://Users//Maria.Misa//workspace_python//drivers//chromedriver")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(8)
        height = driver.execute_script("return window.innerHeight;")
        width = driver.execute_script("return window.innerWidth;")
        print("Height: " + str(height))
        print("Width: " + str(width))

cc = WindowSize()
cc.test()