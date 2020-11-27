from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class PopUp():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(executable_path="C://Users//Maria.Misa//workspace_python//drivers//chromedriver")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(8)
        alertButton = driver.find_element(By.ID, "alertbtn")
        confirmButton = driver.find_element(By.ID, "confirmbtn")
        alertButton.click()
        time.sleep(3)

        alertModal = driver.switch_to.alert
        alertModal.accept()
        confirmButton.click()
        time.sleep(3)
        confirmModal = driver.switch_to.alert
        confirmModal.dismiss()


ch = PopUp()
ch.test()
