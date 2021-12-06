""" Login credentials for ServiceNow """

from Locators.ui_mapping import Locators
import time
from Pages.BasePage import BasePage


class LoginCred(BasePage):

    def login_cred(self):
        self.click(Locators.USER_NAME_OKTA_TEXTBOX)
        self.enter_text(Locators.USER_NAME_OKTA_TEXTBOX, "DIVYA_BALASUBRAMANYA@CONDENAST.COM")
        time.sleep(3)
        # driver.implicitwait()
        self.click(Locators.NEXT_OKTA_BUTTON)
        time.sleep(3)
        self.click(Locators.PASSWORD_OKTA_TEXTBOX)
        self.enter_text(Locators.PASSWORD_OKTA_TEXTBOX, "Laptop12$Laptop")
        time.sleep(3)
        self.click(Locators.SUBMIT_OKTA_BUTTON)
        time.sleep(7)
        self.click(Locators.SEND_PUSH_OKTA_BUTTON)
