from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import *
import time

class MouseOver():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(executable_path="C://Users//Maria.Misa//workspace_python//drivers//chromedriver")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(8)
        driver.execute_script("window.scrollBy(0,600);")
        time.sleep(3)
        element = driver.find_element(By.ID, "mousehover")
        itemToClickLocator = "//div[@class='mouse-hover-content']//a[text()= 'Top']"

        try:
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            print("Mouse hover over element")
            time.sleep(3)
            link = driver.find_element(By.XPATH, itemToClickLocator)
            actions.move_to_element(link).click().perform()
            time.sleep(3)
            print("Item clicked")
        except:
            print("Failed to click item")



ch = MouseOver()
ch.test()