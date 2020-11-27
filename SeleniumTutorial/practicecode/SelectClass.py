from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class SelectClass():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(executable_path="C://Users//Maria.Misa//workspace_python//drivers//chromedriver")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        element = driver.find_element(By.ID, "carselect")
        sel = Select(element)

        sel.select_by_value("benz")
        print("Select Benz by value")
        time.sleep(3)

        sel.select_by_index("2")
        print("Select Honda by index")
        time.sleep(3)

        sel.select_by_visible_text("BMW")
        print("Select BMW by visible text")
        time.sleep(3)

        sel.select_by_index(1)
        print("Select Benz by index")
        time.sleep(3)


ff = SelectClass()
ff.test()