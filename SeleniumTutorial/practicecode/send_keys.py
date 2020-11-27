from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ClickAndSendKeys():
    def test(self):
        base_url = "https://www.fool.com/"
        driver = webdriver.Chrome(executable_path="C://Users//Maria.Misa//workspace_python//drivers//chromedriver")
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(10)
        loginLink = driver.find_element(By.XPATH, "//div[@id='login-menu-item']")
        loginLink.click()
        time.sleep(4)
        emailField = driver.find_element(By.ID, "usernameOrEmail")
        emailField.send_keys("email test")
        time.sleep(4)

        passField = driver.find_element(By.ID, "password")
        passField.send_keys("password test")
        time.sleep(4)

        emailField.clear()
        emailField.send_keys("email test2")
        time.sleep(4)


ff = ClickAndSendKeys()
ff.test()