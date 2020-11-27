from selenium import webdriver

class RunFFTests():

    def testMethod(self):
        #Instatiate FF driver
        driver = webdriver.Firefox()
        # Open the url provided
        driver.get("http://wwww.google.com")

ff = RunFFTests()
ff.testMethod()