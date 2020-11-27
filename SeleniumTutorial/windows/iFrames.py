from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SwitchIframe():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(executable_path="C://Users//Maria.Misa//workspace_python//drivers//chromedriver")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(8)
        driver.execute_script("window.scrollBy(0, 1000)")

        #Switch to iframe using ID
        #driver.switch_to.frame("courses-iframe")

        #Switch to iframe using name
        #driver.switch_to.frame("iframe-name")

        #Switch to iframe using numbers
        driver.switch_to.frame(0)


        searchBox = driver.find_element(By.ID, "search-courses")
        searchBox.send_keys("python")
        time.sleep(3)

        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0, -1000)")

        driver.find_element(By.ID, "name").send_keys("Test successful")
        time.sleep(3)


ch = SwitchIframe()
ch.test()