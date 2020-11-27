from selenium import webdriver

class BrowserInteractions():
    def test(self):
        base_url = "https://letskodeit.teachable.com/pages/practice"
        # Instatiate  driver
        driver = webdriver.Chrome(executable_path="C://Users//Maria.Misa//workspace_python//drivers//chromedriver")

        #Maximize window
        driver.maximize_window()

        driver.get(base_url)

        #retrieve title of page
        title = driver.title
        print("Page title is" + str(title))
        #retrieve current url
        current_url = driver.current_url
        print("Current url is " + current_url)
        # browser refresh
        driver.refresh()
        print("1st refresh")
        # browser refresh another way
        driver.get(driver.current_url)
        print("2nd refresh")
        #open another url
        driver.get("https://letskodeit.teachable.com/p/terms")
        current_url = driver.current_url
        print("Open link:" + current_url)
        #browser back
        driver.back()
        current_url = driver.current_url
        print("Went one step back:" + current_url)
        #browser forward
        driver.forward()
        current_url = driver.current_url
        print("Went one step forward:" + current_url)
        #show page source
        page_source = driver.page_source
        print(page_source)
        #close browser
        driver.quit()

bi = BrowserInteractions()
bi.test()