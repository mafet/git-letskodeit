from selenium import webdriver
from selenium.webdriver.common.by import By

class Find():
    def FindProject(self):
        base_url = 'https://dhtmlx.com/docs/products/dhtmlxGrid/'
        driver = webdriver.Chrome(executable_path="C://Users//Maria.Misa//workspace_python//drivers//chromedriver")
        driver.get(base_url)
        element = driver.find_element_by_xpath("//td[@class='lt-td f' and contains(text(), 'Developers')]//following-sibling::td[3]")
        text = element.text
        if element is not None:
            print("Number of Developers for Enterprise is " + text)

ff = Find()
ff.FindProject()
