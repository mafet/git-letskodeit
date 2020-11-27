from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class ExpilictWaitDemo():
    def test(self):
        baseUrl = "https://www.booking.com/"
        driver = webdriver.Chrome(executable_path="C://Users//Maria.Misa//workspace_python//drivers//chromedriver")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        driver.find_element(By.ID, "LandingAirBookingSearchForm_originationAirportCode").send_keys("LAX")
        driver.find_element(By.NAME, "flights.0.endLocation").send_keys("NYC")
        driver.find_element(By.ID, "flight-date-range-0").click()
        dateToSelect = driver.find_element(By.XPATH,
                                           "//div[@aria-label='September 14, 2020']")
        dateToSelect.click()
        datetoSelect2 = driver.find_element(By.XPATH,
                                           "//div[@aria-label='September 19, 2020']")
        datetoSelect2.click()
        driver.find_element(By.XPATH, "//button[@data-testid='FLIGHTS_SUBMIT_BUTTON']").click()
        wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                                               ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='stops-0-checkbox-0']")))
        element.click()
        time.sleep(2)
        driver.quit()

ff = ExpilictWaitDemo()
ff.test()