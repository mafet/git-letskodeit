from selenium import webdriver
from selenium.webdriver.common.by import By

class ImplicitWaitDemo():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/"
        driver = webdriver.Chrome(executable_path="C://Users//Maria.Misa//workspace_python//drivers//chromedriver")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)


        loginLink = driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
        loginLink.click()

ff = ImplicitWaitDemo()
ff.test()
