import allure
from allure_commons.types import AttachmentType

from Locators.ui_mapping import Locators
from Pages.BasePage import BasePage
import time


class PasswordResetModuleEndUser(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def fill_application_name(self):
        self.enter_text(Locators.APPLICATION_NAME_PASSWORD_REST_TEXTBOX, "okta")
        time.sleep(3)
        self.send_enter(Locators.APPLICATION_NAME_PASSWORD_REST_TEXTBOX)

    def fill_summary(self):
        self.enter_text(Locators.SUMMARY_PASSWORD_RESET_TEXTBOX, "TEST SUMMARY")
        time.sleep(3)
        self.send_enter(Locators.SUMMARY_PASSWORD_RESET_TEXTBOX)

    def fill_description(self):
        self.enter_text(Locators.DESCRIPTION_PASSWORD_RESET_TEXTBOX, "Description")
        time.sleep(3)
        self.send_enter(Locators.DESCRIPTION_PASSWORD_RESET_TEXTBOX)

    def click_submit(self):
        self.click(Locators.SUBMIT_PASSWORD_RESET_BUTTON)
        time.sleep(5)

    def fill_password_reset_fields_end_user(self):
        try:
            self.click(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
            self.enter_text(Locators.SEARCH_TEXTBOX_MODULE_END_USER, "Password Reset")
            self.send_enter(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
            self.click(Locators.PASSWORD_RESET_MODULE_CLICK)
            time.sleep(5)
            self.fill_application_name()
            self.fill_summary()
            self.fill_description()
            self.click_submit()
            allure.attach(self.driver.get_screenshot_as_png(), name="Password Reset",
                          attachment_type=AttachmentType.PNG)

        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="Password Reset",
                          attachment_type=AttachmentType.PNG)
            assert False




