from selenium.webdriver.common.by import By

from browser import Browser

class Contact_Page(Browser):
    NAME_CONTACT_FORM= (By.NAME, 'fullName')
    EMAIL_CONTACT_FORM=(By.ID, "contact_email")

    def contact_form(self):
        self.driver.find_element(*self.NAME_CONTACT_FORM).send_keys("Catalina")
        self.driver.find_element(*self.EMAIL_CONTACT_FORM).send_keys("natalia@gmail.com")
        self.driver.find_element(By.CSS_SELECTOR, 'div[class="mb-4"] label[class="Form-checkbox flex items-center  "]:first-of-type span[class="inline-block"]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'select[name="type"]').select_by_visible_text("Informatii generale")
        self.driver.find_element(By.CSS_SELECTOR, 'select[name="detail"]').select_by_visible_text(" neconformitate caracteristici")
        self.driver.find_element(By.CSS_SELECTOR, 'select[name="additionalDetail"]').select_by_visible_text("Altele")
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="terms_and_conditions"]').click()
        self.driver.find_element(By.LINK_TEXT, "Aplica")
        assert self.driver.current_url == "https://altex.ro/contact/"


