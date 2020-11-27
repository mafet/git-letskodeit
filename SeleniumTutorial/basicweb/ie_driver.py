from selenium import webdriver

class InternetExplorerWin():
    def testRun(self):
        driver = webdriver.Ie(executable_path="C://Users//Maria.Misa//workspace_python//drivers//IEDriverServer")
        driver.get("http://www.google.com")

ie_browser = InternetExplorerWin()
ie_browser.testRun()