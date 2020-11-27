from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import *
import time

class Sliders():
    def test(self):
        baseUrl = "https://jqueryui.com/slider/"
        driver = webdriver.Chrome(executable_path="C://Users//Maria.Misa//workspace_python//drivers//chromedriver")
        driver.maximize_window()
        driver.implicitly_wait(8)
        driver.get(baseUrl)
        driver.switch_to.frame(0)

        element = driver.find_element(By.XPATH, "//div[@id='slider']//span")
        time.sleep(3)
        try:
            actions = ActionChains(driver)
            actions.drag_and_drop_by_offset(element, 200, 0).perform()
            print("Sliding element is successful")
            time.sleep(3)
        except:
            print("Action failed")

ch = Sliders()
ch.test()