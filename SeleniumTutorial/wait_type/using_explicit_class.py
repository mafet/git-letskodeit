from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ExpilictWaitDemo():
    def test(self):
        baseUrl = "https://www.booking.com/"
        driver = webdriver.Chrome(executable_path="C://Users//Maria.Misa//workspace_python//drivers//chromedriver")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        driver.find_element(By.NAME, "login_button").click()
        driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("LAX")
        driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("NYC")
        driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("12/12/2020")
        returnDate = driver.find_element(By.ID, "flight-returning-hp-flight")
        returnDate.clear()
        returnDate.send_keys("12/15/2020")
        driver.find_element(By.XPATH, "//form[@id='gcw-flights-form-hp-flight']//span[contains(text(), 'Search')]").click()


        wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                                               ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.ID, "Nonstop-stop-flights-checkbox")))
        element.click()
        time.sleep(2)
        driver.quit()

ff = ExpilictWaitDemo()
ff.test()
















