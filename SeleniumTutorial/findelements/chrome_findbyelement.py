from selenium import webdriver
from selenium.webdriver.common.by import By

class testFind():

    def testMethod(self):
        base_url = "https://letskodeit.teachable.com/pages/practice"
        # Instatiate  driver
        driver = webdriver.Chrome(executable_path="C://Users//Maria.Misa//workspace_python//drivers//chromedriver")
        # Open the url provided
        driver.get(base_url)

        find_by_id = driver.find_element(By.ID, "name")
        find_by_xpath = driver.find_element(By.XPATH, "//*[@id='displayed-text']")
        find_by_linktxt = driver.find_element(By.LINK_TEXT, "Terms of Use")

        if find_by_id is not None:
            print("We found an element by id")

        if find_by_xpath is not None:
            print("We found an element by xpath")

        if find_by_linktxt is not None:
            print("We found an element by partial link text")


ff = testFind()
ff.testMethod()