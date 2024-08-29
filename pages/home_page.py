from selenium.webdriver.common.by import By

from browser import Browser
class Home_Page(Browser):
    CONTACT_BUTTON = (By.LINK_TEXT, "Contact")
    # ACCEPT_COOKIES = (By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')
    def navigate_to_homepage(self):
        self.driver.get("https://www.altex.ro/")
        self.driver.find_element(By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll').click()
    # def accept_coockies(self):
    #     self.driver.find_element(*self.ACCEPT_COOKIES).click()
    def click_contact(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(*self.CONTACT_BUTTON).click()
