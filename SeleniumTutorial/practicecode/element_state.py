from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ElementState():
    def test(self):
        baseURL = "https://www.google.com/"
        driver = webdriver.Chrome(executable_path="C://Users//Maria.Misa//workspace_python//drivers//chromedriver")
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(15)

        e1 = driver.find_element(By.NAME, "q")
        e1State = e1.is_enabled()
        print("E1 is enabled?" + str(e1State))
        e2 = driver.find_element(By.NAME, "iflsig")
        e2State = e2.is_enabled()
        print("E2 is enabled?" + str(e2State))


es = ElementState()
es.test()



