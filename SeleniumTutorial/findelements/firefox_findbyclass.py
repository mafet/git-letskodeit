from selenium import webdriver


class testFind():

    def testMethod(self):
        base_url = "https://letskodeit.teachable.com/pages/practice"
        # Instatiate  driver
        driver = webdriver.Firefox(executable_path="C://Users//Maria.Misa//workspace_python//drivers//geckodriver")
        # Open the url provided
        driver.get(base_url)

        element_by_class_name = driver.find_element_by_class_name("displayed-class")
        element_by_class_name.send_keys("Test Element")
        if element_by_class_name is not None:
            print("We found an element by class name")

        element_by_tag_name = driver.find_element_by_tag_name("a")
        text = element_by_tag_name.text
        if element_by_tag_name is not None:
            print("We found an element by tag name" + text)




ff = testFind()
ff.testMethod()