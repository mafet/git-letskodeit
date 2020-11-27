from selenium import webdriver
import time

class ChromeDriverWin():

    def testRun(self):
        driver = webdriver.Chrome(executable_path="C:\\Users\\Maria.Misa\\workspace_python\\drivers\\chromedriver.exe")
        driver.get("https://www.google.com")
        time.sleep(20)

cd = ChromeDriverWin()
cd.testRun()