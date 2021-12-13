import allure
from allure_commons.types import AttachmentType

from Locators.ui_mapping import Locators
from Pages.BasePage import BasePage
import time


class AccessModuleEndUser(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def fill_application_required(self, application_required):
        self.click(Locators.APPLICATION_REQUIRED_ACCESS_TEXTBOX)
        self.enter_text(Locators.APPLICATION_REQUIRED_ACCESS_TEXTBOX, application_required)
        self.send_enter(Locators.APPLICATION_REQUIRED_ACCESS_TEXTBOX)

    def fill_summary(self, summary):
        self.click(Locators.SUMMARY_ACCESS_TEXTBOX)
        self.enter_text(Locators.SUMMARY_ACCESS_TEXTBOX, summary)
        self.send_enter(Locators.SUMMARY_ACCESS_TEXTBOX)

    def fill_description(self, description):
        self.click(Locators.DESCRIPTION_ACCESS_TEXTBOX)
        self.enter_text(Locators.DESCRIPTION_ACCESS_TEXTBOX, description)
        self.send_enter(Locators.DESCRIPTION_ACCESS_TEXTBOX)

    def click_submit(self):
        self.click(Locators.SUBMIT_ACCESS_BUTTON)
        time.sleep(5)

    def fill_access_module_end_user(self, application_required, summary, description):
        try:
            self.click(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
            self.enter_text(Locators.SEARCH_TEXTBOX_MODULE_END_USER, "ACCESS")
            self.send_enter(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
            self.click(Locators.ACCESS_CLICK)
            time.sleep(5)

            self.is_visible(Locators.TITLE_ACCESS)

            self.fill_application_required(application_required)
            self.fill_summary(summary)
            self.fill_description(description)
            self.click_submit()
            allure.attach(self.driver.get_screenshot_as_png(), name="Access Module",
                          attachment_type=AttachmentType.PNG)


        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="Access Module",
                          attachment_type=AttachmentType.PNG)
            assert False
