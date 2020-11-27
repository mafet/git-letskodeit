from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class DynamicXpath():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/"
        driver = webdriver.Chrome(executable_path="C://Users//Maria.Misa//workspace_python//drivers//chromedriver")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        #go to view all courses
        driver.find_element(By.XPATH, "//a[@href = '/courses']").click()
        time.sleep(3)

        #put text in search box
        searchBox = driver.find_element(By.ID, "search-courses")
        searchBox.send_keys("JavaScript")
        time.sleep(3)

        #select course
        _course = "//div[contains(@class, 'course-listing-title') and contains(text(), '{0}')]"
        _courseLocator = _course.format("JavaScript for beginners")

        courseElement = driver.find_element(By.XPATH, _courseLocator)
        courseElement.click()
        time.sleep(3)


ff = DynamicXpath()
ff.test()




