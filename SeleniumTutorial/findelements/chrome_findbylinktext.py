from selenium import webdriver


class testFind():

    def testMethod(self):
        base_url = "https://www.yahoo.com/"
        # Instatiate  driver
        driver = webdriver.Chrome(executable_path="C://Users//Maria.Misa//workspace_python//drivers//chromedriver")
        # Open the url provided
        driver.get(base_url)

        element_by_link_txt = driver.find_element_by_link_text("Entertainment")

        if element_by_link_txt is not None:
            print("We found an element by link text")

        element_by_partial_txt = driver.find_element_by_partial_link_text("Finan")

        if element_by_partial_txt is not None:
            print("We found an element by partial link text")




ff = testFind()
ff.testMethod()