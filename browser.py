from seleniumbase import Driver

class Browser():

    driver=Driver(browser='edge')
    driver.maximize_window()
    driver.set_page_load_timeout(15) # pentru driver.get()
    driver.implicitly_wait(15) # pentru driver.find_element()

    def close_browser(self):
        self.driver.quit()