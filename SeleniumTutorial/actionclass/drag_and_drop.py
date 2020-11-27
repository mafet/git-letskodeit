from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import *
import time

class DragAndDrop():
    def test(self):
        baseUrl = "https://jqueryui.com/droppable/"
        driver = webdriver.Chrome(executable_path="C://Users//Maria.Misa//workspace_python//drivers//chromedriver")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(8)
        driver.switch_to.frame(0)
        fromElement = driver.find_element(By.ID, "draggable")
        toElement = driver.find_element(By.ID, "droppable")
        try:
            actions = ActionChains(driver)
            #actions.drag_and_drop(fromElement, toElement).perform()
            actions.click_and_hold(fromElement).move_to_element(toElement).release().perform()
            time.sleep(3)
            print("Drag and drop successful")
        except:
            print("Action failed")

ch = DragAndDrop()
ch.test()