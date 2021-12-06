import allure
from allure_commons.types import AttachmentType

from Locators.ui_mapping import Locators
from Pages.BasePage import BasePage
import time


class DAMEnhancementRequestModuleEndUser(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def choose_urgency(self):
        self.click(Locators.URGENCY_DAM_ENHANCEMENT_REQUEST)
        self.click(Locators.URGENCY_DAM_ENHANCEMENT_REQUEST_TEXTBOX)
        time.sleep(3)
        self.enter_text(Locators.URGENCY_DAM_ENHANCEMENT_REQUEST_TEXTBOX, "High")
        self.send_enter(Locators.URGENCY_DAM_ENHANCEMENT_REQUEST_TEXTBOX)
        time.sleep(3)

    def choose_dam_platform(self):
        self.click(Locators.DAM_PLATFORM_DAM_ENHANCEMENT_REQUEST)
        self.click(Locators.DAM_PLATFORM_DAM_ENHANCEMENT_REQUEST_TEXTBOX)
        self.enter_text(Locators.DAM_PLATFORM_DAM_ENHANCEMENT_REQUEST_TEXTBOX, "OKTA")
        time.sleep(3)
        self.send_enter(Locators.DAM_PLATFORM_DAM_ENHANCEMENT_REQUEST_TEXTBOX)

    def choose_editorial_role(self):
        self.click(Locators.EDITORIAL_ROLE_DAM_ENHANCEMENT_REQUEST)
        self.click(Locators.EDITORIAL_ROLE_DAM_ENHANCEMENT_REQUEST_TEXTBOX)
        self.enter_text(Locators.EDITORIAL_ROLE_DAM_ENHANCEMENT_REQUEST_TEXTBOX, "OKTA")
        time.sleep(3)
        self.send_enter(Locators.EDITORIAL_ROLE_DAM_ENHANCEMENT_REQUEST_TEXTBOX)

    def choose_brand(self):
        self.click(Locators.BRAND_DAM_ENHANCEMENT_REQUEST)
        self.click(Locators.BRAND_DAM_ENHANCEMENT_REQUEST_TEXTBOX)
        self.enter_text(Locators.BRAND_DAM_ENHANCEMENT_REQUEST_TEXTBOX, "OKTA")
        time.sleep(3)
        self.send_enter(Locators.BRAND_DAM_ENHANCEMENT_REQUEST_TEXTBOX)

    def fill_summary(self):
        self.click(Locators.SUMMARY_DAM_ENHANCEMENT_REQUEST_TEXTBOX)
        self.enter_text(Locators.SUMMARY_DAM_ENHANCEMENT_REQUEST_TEXTBOX, "DESC")
        time.sleep(3)
        self.send_enter(Locators.SUMMARY_DAM_ENHANCEMENT_REQUEST_TEXTBOX)

    def fill_business_description(self):
        self.click(Locators.BUSINESS_JUSTIFICATION_DAM_ENHANCEMENT_REQUEST_TEXTBOX)
        self.enter_text(Locators.BUSINESS_JUSTIFICATION_DAM_ENHANCEMENT_REQUEST_TEXTBOX, "DESC")
        time.sleep(3)
        self.send_enter(Locators.BUSINESS_JUSTIFICATION_DAM_ENHANCEMENT_REQUEST_TEXTBOX)

    def fill_use_case(self):
        self.click(Locators.USE_CASE_DAM_ENHANCEMENT_REQUEST_TEXTBOX)
        self.enter_text(Locators.USE_CASE_DAM_ENHANCEMENT_REQUEST_TEXTBOX, "DESC")
        time.sleep(3)
        self.send_enter(Locators.USE_CASE_DAM_ENHANCEMENT_REQUEST_TEXTBOX)

    def click_submit(self):
        self.click(Locators.SUBMIT_DAM_ENHANCEMENT_REQUEST_TEXTBOX)
        time.sleep(5)

    def fill_dam_enhancement_request_end_user(self):
        try:
            self.click(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
            self.enter_text(Locators.SEARCH_TEXTBOX_MODULE_END_USER, "PRINTER ISSUE")
            self.send_enter(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
            self.click(Locators.ACCESS_CLICK)
            time.sleep(5)

            self.choose_urgency()
            self.choose_dam_platform()
            self.choose_editorial_role()
            self.choose_brand()
            self.fill_summary()
            self.fill_business_description()
            self.fill_use_case()
            self.click_submit()
            allure.attach(self.driver.get_screenshot_as_png(), name="DAM Enhancement request",
                         attachment_type=AttachmentType.PNG)

        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="DAM Enhancement request ",
                          attachment_type=AttachmentType.PNG)
            assert False




