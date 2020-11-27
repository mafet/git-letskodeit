from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class RadioButtonsAndCheckboxes():
    def test(self):
        self.baseUrl = "https://letskodeit.teachable.com/p/practice"
        self.driver = webdriver.Chrome(executable_path="C://Users//Maria.Misa//workspace_python//drivers//chromedriver")
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)
        self.driver.implicitly_wait(15)

        bmw = self.driver.find_element(By.ID, "bmwradio")
        bmw.click()
        time.sleep(3)


        benz = self.driver.find_element(By.ID, "benzradio")
        benz.click()
        time.sleep(3)


        honda = self.driver.find_element(By.ID, "hondaradio")
        honda.click()
        time.sleep(3)

        print("Is Honda selected?" + str(honda.is_selected()))
        print("Is Benz selected?" + str(benz.is_selected()))
        print("Is BMW selected?" + str(bmw.is_selected()))

        benz.click()
        print("Is Benz selected?" + str(benz.is_selected()))
        time.sleep(3)



    def checkBox(self):
        bmwcheck = self.driver.find_element(By.ID, "bmwcheck")
        bmwcheck.click()
        time.sleep(3)
        hnd = self.driver.find_element(By.ID, "hondacheck")
        hnd.click()
        time.sleep(3)
        benzcheck = self.driver.find_element(By.ID, "benzcheck")
        time.sleep(3)

        print("Is BMW checkbox selected? " + str(bmwcheck.is_selected()))
        print("Is Honda checkbox selected? " + str(hnd.is_selected()))
        print("Is Benz checkbox selected? " + str(benzcheck.is_selected()))






ff = RadioButtonsAndCheckboxes()
ff.test()
ff.checkBox()
