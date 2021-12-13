"""  """
import allure
from allure_commons.types import AttachmentType

""" Request module end user page """

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from Locators.ui_mapping import Locators
from Pages.BasePage import BasePage


@allure.severity(allure.severity_level.NORMAL)
class RequestModuleEndUser(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get("https://supporttest.condenastint.com/sp")
        # time.sleep(3)
        # self.click(Locators.USER_NAME_OKTA_TEXTBOX)
        # self.enter_text(Locators.USER_NAME_OKTA_TEXTBOX, "DIVYA_BALASUBRAMANYA@CONDENAST.COM")
        # time.sleep(3)
        # self.click(Locators.NEXT_OKTA_BUTTON)
        # time.sleep(3)
        # self.click(Locators.PASSWORD_OKTA_TEXTBOX)
        # self.enter_text(Locators.PASSWORD_OKTA_TEXTBOX, "Laptop12$Laptop")
        # time.sleep(3)
        # self.click(Locators.SUBMIT_OKTA_BUTTON)
        # time.sleep(7)
        # self.click(Locators.SEND_PUSH_OKTA_BUTTON)
        # time.sleep(30)

    def select_category(self, category):
        self.click(Locators.CATEGORY_REQUEST_DROPDOWN)
        # time.sleep(5)
        self.click(Locators.CATEGORY_REQUEST_TEXTBOX)
        time.sleep(8)
        self.enter_text(Locators.CATEGORY_REQUEST_TEXTBOX, category)
        time.sleep(3)
        self.send_enter(Locators.CATEGORY_REQUEST_TEXTBOX)

    def choose_urgency(self, urgency):
        self.click(Locators.URGENCY_REQUEST_DROPDOWN)
        self.click(Locators.URGENCY_REQUEST_TEXTBOX)
        time.sleep(3)
        self.enter_text(Locators.URGENCY_REQUEST_TEXTBOX, urgency)
        self.send_enter(Locators.URGENCY_REQUEST_TEXTBOX)
        time.sleep(3)

    def fill_summary(self, summary):
        self.click(Locators.SUMMARY_REQUEST_TEXTBOX)
        self.enter_text(Locators.SUMMARY_REQUEST_TEXTBOX,summary)

    def fill_contact_phone_number(self, phone_number):
        self.click(Locators.CONTACT_NUMBER_REQUEST_TEXTBOX)
        self.enter_text(Locators.CONTACT_NUMBER_REQUEST_TEXTBOX, phone_number)

    def fill_description(self, desc):
        self.click(Locators.DESCRIPTION_REQUEST_TEXTBOX)
        self.enter_text(Locators.DESCRIPTION_REQUEST_TEXTBOX, desc)

    def click_submit(self):
        self.click(Locators.SUBMIT_REQUEST_BUTTON)
        time.sleep(2)

    # def fetch_text(self):
    #     time.sleep(5)
    #     print("Inside request text")
    #     request_number = self.get_element_text(Locators.FETCH_REQUEST_NUMBER)
    #     time.sleep(5)
    #     print("The request number created is", request_number)
    #     time.sleep(8)

    def fill_request_module_end_user(self, category,urgency,summary, contact_number, description):
        try:
            self.click(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
            self.enter_text(Locators.SEARCH_TEXTBOX_MODULE_END_USER, "I need Something")
            self.send_enter(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
            self.click(Locators.I_NEED_SOMETHING_CLICK)

            self.click(Locators.TITLE_I_NEED_SOMETHING)

            self.select_category(category)
            self.choose_urgency(urgency)
            self.fill_summary(summary)
            self.fill_contact_phone_number(contact_number)
            self.fill_description(description)
            self.click_submit()
            # self.fetch_text()
            allure.attach(self.driver.get_screenshot_as_png(), name="I need Something",
                          attachment_type=AttachmentType.PNG)

        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="I need Something",
                          attachment_type=AttachmentType.PNG)
            assert False





