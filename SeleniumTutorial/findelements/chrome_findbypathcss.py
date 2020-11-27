from selenium import webdriver


class testFind():

    def testMethod(self):
        base_url = "https://letskodeit.teachable.com/pages/practice"
        # Instatiate FF driver
        driver = webdriver.Chrome(executable_path="C://Users//Maria.Misa//workspace_python//drivers//chromedriver")
        # Open the url provided
        driver.get(base_url)
        element_by_xpath = driver.find_element_by_xpath("//*[@id='name1']")

        if element_by_xpath is not None:
            print("We found an element by Xpath")

        element_by_css = driver.find_element_by_css_selector("#displayed-text")

        if element_by_css is not None:
            print("We found an element by CSS")




ff = testFind()
ff.testMethod()