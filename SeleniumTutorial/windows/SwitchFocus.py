from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SwitchFocus():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(executable_path="C://Users//Maria.Misa//workspace_python//drivers//chromedriver")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(8)
        parentHandle = driver.current_window_handle
        print("Parent handle: " + parentHandle)

        #Locate element and click to open new window
        driver.find_element(By.ID, "openwindow").click()
        time.sleep(2)

        #Find handles after opening new window
        handles = driver.window_handles

        #Switch windows
        for handle in handles:
            print("Handle: " + handle)
            if handle not in parentHandle:
                driver.switch_to.window(handle)
                print("Switched to: " + handle)
                # Find element and send keys in search box
                searchBox = driver.find_element(By.ID, "search-courses")
                searchBox.send_keys("Python")
                time.sleep(3)
                driver.close()
                break

        #Switch to parent handle
        driver.switch_to.window(parentHandle)
        driver.find_element(By.ID, "name").send_keys("test successful")
        time.sleep(3)

ch = SwitchFocus()
ch.test()