from selenium import webdriver

class FindByIDName():

    def testMethod(self):
        base_url = "https://letskodeit.teachable.com/pages/practice"
        #Instatiate FF driver
        driver = webdriver.Firefox(executable_path="C://Users//Maria.Misa//workspace_python//drivers//geckodriver")
        # Open the url provided
        driver.get(base_url)
        element_by_id = driver.find_element_by_id("name")

        if element_by_id is not None:
            print("We found an element by ID")

        element_by_name = driver.find_element_by_name("show-hide")

        if element_by_name is not None:
            print("We found an element by name")
        driver.get("https://yahoo.com")
        driver.find_element_by_id("header-profile-menu")

        
ff = FindByIDName()
ff.testMethod()