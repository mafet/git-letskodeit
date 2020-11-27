from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ListOfElements():
    def test(self):
        base_url = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Chrome(executable_path="C://Users//Maria.Misa//workspace_python//drivers//chromedriver")
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(10)

        radioButtonsList = driver.find_elements(By.XPATH, "//input[contains(@type,'checkbox') and contains(@name, 'cars')]")
        size = len(radioButtonsList)
        print("Size of list is " + str(size))

        for radioButton in radioButtonsList:
            isSelected = radioButton.is_selected()
            if not isSelected:
                radioButton.click()
                time.sleep(3)


ff = ListOfElements()
ff.test()
