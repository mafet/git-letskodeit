from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ScollingElement():
    def test(self):
        baseUrl = "https://www.fool.com/"
        driver = webdriver.Chrome(executable_path="C://Users//Maria.Misa//workspace_python//drivers//chromedriver")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(8)
        #Scroll down
        driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(3)
        #Scroll up
        driver.execute_script("window.scrollBy(0, -500);")
        time.sleep(3)
        #Scroll element into view
        scrollElement = driver.find_element(By.ID, "tile-hti")
        driver.execute_script("arguments[0].scrollIntoView(true);", scrollElement)
        time.sleep(3)
        driver.execute_script("window.scrollBy(0, -150);")
        time.sleep(3)
        #Native way to scroll to element
        driver.execute_script("window.scrollBy(0, -800);")
        location = scrollElement.location_once_scrolled_into_view
        time.sleep(3)
        print(location)


cc = ScollingElement()
cc.test()