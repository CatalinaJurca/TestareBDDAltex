from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


from browser import Browser
class Home_Page(Browser):
    # CONTACT_BUTTON = (By.LINK_TEXT, "Formular de contact")
    # ACCEPT_COOKIES = (By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')
    ACCEPT_COOKIES = (By.XPATH,"//div[@id='CybotCookiebotDialogBodyButtonsWrapper']//button[@id='CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll']")
    def navigate_to_homepage(self):
        self.driver.get("https://www.altex.ro/")
    def accept_cookies(self):
        # WebDriverWait(self.driver, 15).until(EC.element_located_to_be_selected(self.ACCEPT_COOKIES))
        self.driver.find_element(*self.ACCEPT_COOKIES).click()
        # self.driver.execute_script("arguments[0].click()",self.ACCEPT_COOKIES)
        # self.driver.execute_script("document.getElementById('CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll').click()")
    def click_contact(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(By.LINK_TEXT, "Formular de contact").click()
