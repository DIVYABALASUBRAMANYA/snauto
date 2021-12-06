import allure
from allure_commons.types import AttachmentType

from Locators.ui_mapping import Locators
from Pages.BasePage import BasePage
import time


class GlobalSupportEnhancementEndUser(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def fill_urgency(self):
        self.click(Locators.URGENCY_GLOBAL_SUPPORT_PORTAL_ENHANCEMENT_DROPDOWN)
        time.sleep(3)
        self.click(Locators.URGENCY_GLOBAL_SUPPORT_PORTAL_ENHANCEMENT_TEXTBOX)
        time.sleep(3)
        self.enter_text(Locators.URGENCY_GLOBAL_SUPPORT_PORTAL_ENHANCEMENT_TEXTBOX, "High")
        self.send_enter(Locators.URGENCY_GLOBAL_SUPPORT_PORTAL_ENHANCEMENT_TEXTBOX)
        time.sleep(2)

    def fill_date_required(self):
        self.click(Locators.DATE_REQUIRED_TEXTBOX_GLOBAL_SUPPORT_PORTAL_ENHANCEMENT)
        time.sleep(2)
        self.enter_text(Locators.DATE_REQUIRED_TEXTBOX_GLOBAL_SUPPORT_PORTAL_ENHANCEMENT, "2021-10-31")
        self.send_enter(Locators.DATE_REQUIRED_TEXTBOX_GLOBAL_SUPPORT_PORTAL_ENHANCEMENT)
        time.sleep(2)

    def select_enhancement_type(self):
        self.click(Locators.ENHANCEMENT_TYPE_GLOBAL_SUPPORT_PORTAL_ENHANCEMENT_DROPDOWN)
        time.sleep(2)
        self.enter_text(Locators.ENHANCEMENT_TYPE_GLOBAL_SUPPORT_PORTAL_ENHANCEMENT_TEXTBOX, "General Enquiry")
        time.sleep(2)
        self.send_enter(Locators.ENHANCEMENT_TYPE_GLOBAL_SUPPORT_PORTAL_ENHANCEMENT_TEXTBOX)
        time.sleep(3)

    def fill_summary(self):
        self.click(Locators.SUMMARY_GLOBAL_SUPPORT_PORTAL_ENHANCEMENT_TEXTBOX)
        time.sleep(2)
        self.enter_text(Locators.SUMMARY_GLOBAL_SUPPORT_PORTAL_ENHANCEMENT_TEXTBOX, "test")
        time.sleep(3)
        self.send_enter(Locators.SUMMARY_GLOBAL_SUPPORT_PORTAL_ENHANCEMENT_TEXTBOX)
        time.sleep(2)

    def fill_description(self):
        self.click(Locators.DESCRIPTION_GLOBAL_SUPPORT_PORTAL_ENHANCEMENT_TEXTBOX)
        time.sleep(2)
        self.enter_text(Locators.DESCRIPTION_GLOBAL_SUPPORT_PORTAL_ENHANCEMENT_TEXTBOX, "TEST")
        time.sleep(2)
        self.send_enter(Locators.DESCRIPTION_GLOBAL_SUPPORT_PORTAL_ENHANCEMENT_TEXTBOX)

    def click_submit(self):
        self.click(Locators.SUBMIT_GLOBAL_GLOBAL_SUPPORT_PORTAL_ENHANCEMENT_BUTTON)

    def fill_global_support_portal_enhancement_module_end_user(self):
        try:
            self.click(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
            self.enter_text(Locators.SEARCH_TEXTBOX_MODULE_END_USER, "Global Support Portal enhancement")
            self.click(Locators.GLOBAL_SUPPORT_PORTAL_CLICK)

            self.fill_urgency()
            self.fill_date_required()
            self.select_enhancement_type()
            self.fill_summary()
            self.fill_description()
            self.click_submit()
            allure.attach(self.driver.get_screenshot_as_png(), name="Global support portal enhancement",
                          attachment_type=AttachmentType.PNG)

        except:

            allure.attach(self.driver.get_screenshot_as_png(), name="Global support portal enhancement",
                          attachment_type=AttachmentType.PNG)
            assert False

