from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class WebDriverFactory():
    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):
        baseUrl = "https://courses.letskodeit.com/"
        if self.browser == "firefox":
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif self.browser == "chrome":
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        elif self.browser == "edge":
            driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
        else:
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)
        return driver
