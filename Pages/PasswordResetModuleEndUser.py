import allure
from allure_commons.types import AttachmentType

from Locators.ui_mapping import Locators
from Pages.BasePage import BasePage
import time


@allure.severity(allure.severity_level.NORMAL)
class PasswordResetModuleEndUser(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def fill_caller(self, caller):
        if caller is None:
            pass
        else:
            self.click(Locators.CALLER_PASSWORD_RESET)
            time.sleep(3)
            self.click(Locators.CALLER_PASSWORD_RESET_TEXTBOX)
            time.sleep(3)
            self.enter_text(Locators.CALLER_PASSWORD_RESET_TEXTBOX, caller)
            time.sleep(3)
            self.send_enter(Locators.CALLER_PASSWORD_RESET_TEXTBOX)
            time.sleep(3)

    def fill_application_name(self, application_name):
        if application_name is None:
            pass
        else:
            self.enter_text(Locators.APPLICATION_NAME_PASSWORD_REST_TEXTBOX, application_name)
            self.send_enter(Locators.APPLICATION_NAME_PASSWORD_REST_TEXTBOX)

    def fill_summary(self, summary):
        self.click(Locators.SUMMARY_PASSWORD_RESET_TEXTBOX)
        self.enter_text(Locators.SUMMARY_PASSWORD_RESET_TEXTBOX, summary)
        self.send_enter(Locators.SUMMARY_PASSWORD_RESET_TEXTBOX)

    def fill_description(self, description):
        if description is None:
            pass
        else:
            self.click(Locators.DESCRIPTION_PASSWORD_RESET_TEXTBOX)
            self.enter_text(Locators.DESCRIPTION_PASSWORD_RESET_TEXTBOX, description)
            self.send_enter(Locators.DESCRIPTION_PASSWORD_RESET_TEXTBOX)

    def click_submit(self):
        self.click(Locators.SUBMIT_PASSWORD_RESET_BUTTON)
        time.sleep(5)

    def fill_password_reset_fields_end_user(self, caller, application, summary, description):
        try:
            self.click(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
            self.enter_text(Locators.SEARCH_TEXTBOX_MODULE_END_USER, "Password Reset")
            self.send_enter(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
            self.click(Locators.PASSWORD_RESET_MODULE_CLICK)
            time.sleep(5)

            self.fill_caller(caller)
            self.fill_application_name(application)
            self.fill_summary(summary)
            self.fill_description(description)
            self.click_submit()
            allure.attach(self.driver.get_screenshot_as_png(), name="Password Reset",
                          attachment_type=AttachmentType.PNG)

        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="Password Reset",
                          attachment_type=AttachmentType.PNG)
            assert False




