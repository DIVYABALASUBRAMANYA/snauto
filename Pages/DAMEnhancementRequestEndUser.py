import allure
from allure_commons.types import AttachmentType

from Locators.ui_mapping import Locators
from Pages.BasePage import BasePage
import time


@allure.severity(allure.severity_level.NORMAL)
class DAMEnhancementRequestModuleEndUser(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def fill_requested_for(self, requested_for):
        if requested_for is None:
            pass
        else:
            self.click(Locators.REQUESTED_FOR_DAM_ENHANCEMENT_REQUEST)
            self.click(Locators.REQUESTED_FOR_DAM_ENHANCEMENT_REQUEST_TEXTBOX)
            time.sleep(3)
            self.enter_text(Locators.REQUESTED_FOR_DAM_ENHANCEMENT_REQUEST_TEXTBOX, requested_for)
            time.sleep(5)
            self.send_enter(Locators.REQUESTED_FOR_DAM_ENHANCEMENT_REQUEST_TEXTBOX)
            time.sleep(5)

    def fill_office(self, office):
        self.click(Locators.OFFICE_DAM_ENHANCEMENT_REQUEST)
        self.click(Locators.OFFICE_DAM_ENHANCEMENT_REQUEST_TEXTBOX)
        time.sleep(3)
        self.enter_text(Locators.OFFICE_DAM_ENHANCEMENT_REQUEST_TEXTBOX, office)
        time.sleep(5)
        self.send_enter(Locators.OFFICE_DAM_ENHANCEMENT_REQUEST_TEXTBOX)
        time.sleep(5)

    def choose_urgency(self, urgency):
        if urgency is None:
            pass
        else:
            self.click(Locators.URGENCY_DAM_ENHANCEMENT_REQUEST)
            self.click(Locators.URGENCY_DAM_ENHANCEMENT_REQUEST_TEXTBOX)
            time.sleep(3)
            self.enter_text(Locators.URGENCY_DAM_ENHANCEMENT_REQUEST_TEXTBOX, urgency)
            self.send_enter(Locators.URGENCY_DAM_ENHANCEMENT_REQUEST_TEXTBOX)
            time.sleep(3)

    def choose_dam_platform(self, DAM_platform):
        self.click(Locators.DAM_PLATFORM_DAM_ENHANCEMENT_REQUEST)
        self.click(Locators.DAM_PLATFORM_DAM_ENHANCEMENT_REQUEST_TEXTBOX)
        self.enter_text(Locators.DAM_PLATFORM_DAM_ENHANCEMENT_REQUEST_TEXTBOX, DAM_platform)
        time.sleep(3)
        self.send_enter(Locators.DAM_PLATFORM_DAM_ENHANCEMENT_REQUEST_TEXTBOX)

    def choose_editorial_role(self, role):
        self.click(Locators.EDITORIAL_ROLE_DAM_ENHANCEMENT_REQUEST)
        self.click(Locators.EDITORIAL_ROLE_DAM_ENHANCEMENT_REQUEST_TEXTBOX)
        self.enter_text(Locators.EDITORIAL_ROLE_DAM_ENHANCEMENT_REQUEST_TEXTBOX, role)
        time.sleep(3)
        self.send_enter(Locators.EDITORIAL_ROLE_DAM_ENHANCEMENT_REQUEST_TEXTBOX)

    def choose_brand(self, brand):
        if brand is None:
            pass
        else:
            self.click(Locators.BRAND_DAM_ENHANCEMENT_REQUEST)
            self.click(Locators.BRAND_DAM_ENHANCEMENT_REQUEST_TEXTBOX)
            self.enter_text(Locators.BRAND_DAM_ENHANCEMENT_REQUEST_TEXTBOX, brand)
            time.sleep(3)
            self.send_enter(Locators.BRAND_DAM_ENHANCEMENT_REQUEST_TEXTBOX)

    def fill_summary(self, summary):
        self.click(Locators.SUMMARY_DAM_ENHANCEMENT_REQUEST_TEXTBOX)
        self.enter_text(Locators.SUMMARY_DAM_ENHANCEMENT_REQUEST_TEXTBOX, summary)
        self.send_enter(Locators.SUMMARY_DAM_ENHANCEMENT_REQUEST_TEXTBOX)

    def fill_business_description(self, desc):
        self.click(Locators.BUSINESS_JUSTIFICATION_DAM_ENHANCEMENT_REQUEST_TEXTBOX)
        self.enter_text(Locators.BUSINESS_JUSTIFICATION_DAM_ENHANCEMENT_REQUEST_TEXTBOX, desc)
        self.send_enter(Locators.BUSINESS_JUSTIFICATION_DAM_ENHANCEMENT_REQUEST_TEXTBOX)

    def fill_use_case(self, use_case):
        self.click(Locators.USE_CASE_DAM_ENHANCEMENT_REQUEST_TEXTBOX)
        self.enter_text(Locators.USE_CASE_DAM_ENHANCEMENT_REQUEST_TEXTBOX, use_case)
        self.send_enter(Locators.USE_CASE_DAM_ENHANCEMENT_REQUEST_TEXTBOX)

    def click_submit(self):
        self.click(Locators.SUBMIT_DAM_ENHANCEMENT_REQUEST_TEXTBOX)
        time.sleep(5)

    def fill_dam_enhancement_request_end_user(self, requested_for, office, urgency, DAM_Platform,editorial_role, Brand, Summary, Business_justification, use_case):
        try:
            self.click(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
            self.enter_text(Locators.SEARCH_TEXTBOX_MODULE_END_USER, " DAM Enhancement Request")
            self.send_enter(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
            self.click(Locators.DAM_ENHANCEMENT_REQUEST_CLICK)
            time.sleep(5)

            self.is_visible(Locators.DAM_ENHANCEMENT_REQUEST_TITLE)

            self.fill_requested_for(requested_for)
            self.fill_office(office)
            self.choose_urgency(urgency)
            self.choose_dam_platform(DAM_Platform)
            self.choose_editorial_role(editorial_role)
            self.choose_brand(Brand)
            self.fill_summary(Summary)
            self.fill_business_description(Business_justification)
            self.fill_use_case(use_case)
            self.click_submit()
            allure.attach(self.driver.get_screenshot_as_png(), name="DAM Enhancement request",
                         attachment_type=AttachmentType.PNG)

        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="DAM Enhancement request ",
                          attachment_type=AttachmentType.PNG)
            assert False




