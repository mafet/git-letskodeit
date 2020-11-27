from selenium import webdriver
from selenium.webdriver.common.by import By

class FindElement():
    def testFinder(self):
        base_url = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Chrome(executable_path="C://Users//Maria.Misa//workspace_python//drivers//chromedriver")
        driver.get(base_url)
        element = driver.find_element_by_xpath("//*[@id='product']//tr//td[contains(text(), 'Python')]//following-sibling::td")
        text = element.text
        if element is not None:
            print("Price of Python Class is " + text)

test = FindElement()
test.testFinder()