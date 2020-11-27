from selenium import webdriver
from selenium.webdriver.common.by import By

class FindListOfElements():

    def testMethod(self):
        base_url = "https://letskodeit.teachable.com/pages/practice"
        # Instatiate  driver
        driver = webdriver.Chrome(executable_path="C://Users//Maria.Misa//workspace_python//drivers//chromedriver")
        # Open the url provided
        driver.get(base_url)

        elements_by_class =  driver.find_elements_by_class_name("inputs")
        length = len(elements_by_class)

        elements_by_tag = driver.find_elements(By.TAG_NAME, "td")
        length2 = len(elements_by_tag)

        if elements_by_class is not None:
            print("Class: Size of the list is " + str(length))

        if elements_by_tag is not None:
            print("Tag: Size of the list is " + str(length2))



ff = FindListOfElements()
ff.testMethod()