from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Screenshots():
    def test(self):
        baseUrl = "https://www.fool.com/"
        driver = webdriver.Chrome(executable_path="C://Users//Maria.Misa//workspace_python//drivers//chromedriver")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        driver.find_element(By.ID, "login-menu-item").click()
        time.sleep(5)
        driver.find_element(By.ID, "usernameOrEmail").send_keys("user123")
        driver.find_element(By.ID, "password").send_keys("pass123")
        driver.find_element(By.ID, "btn-login").click()
        time.sleep(10)
        self.takeScreenshots(driver)

    def takeScreenshots(self, driver):
        fileName = "test" + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "C:\\Users\\Maria.Misa\\Documents\\"
        destinationFileName = screenshotDirectory + fileName

        try:
            driver.save_screenshot(destinationFileName)
            print("Screenshot saved to directory " + destinationFileName)
        except NotADirectoryError:
            print("Invalid Directory")

ff = Screenshots()
ff.test()
