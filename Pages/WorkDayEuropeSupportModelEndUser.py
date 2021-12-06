""" Workday europe support model end user page"""

import time

from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from Locators.ui_mapping import Locators
from Pages.BasePage import BasePage
import allure


@allure.severity(allure.severity_level.NORMAL)
class WorkDayEuropeSupportModelEndUser(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get("https://supporttest.condenastint.com/sp")
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

    def select_issue_inquiry(self):
        self.click(Locators.ISSUE_ENQUIRY_WORKDAY_EUROPE_DROPDOWN)
        time.sleep(3)
        self.click(Locators.ISSUE_ENQUIRY_WORKDAY_EUROPE_TEXTBOX)
        time.sleep(5)
        self.enter_text(Locators.ISSUE_ENQUIRY_WORKDAY_EUROPE_TEXTBOX, "Program")
        time.sleep(3)
        self.send_enter(Locators.ISSUE_ENQUIRY_WORKDAY_EUROPE_TEXTBOX)
        # allure.attach(self.driver.get_screenshot_as_png(), name="TESTSS", attachment_type=AttachmentType.PNG)

    def fill_description(self):
        self.click(Locators.DESCRIPTION_WORKDAY_EUROPE_TEXTBOX)
        self.enter_text(Locators.DESCRIPTION_WORKDAY_EUROPE_TEXTBOX, "DESC")
        time.sleep(3)
        self.send_enter(Locators.DESCRIPTION_WORKDAY_EUROPE_TEXTBOX)



    def click_submit(self):
        self.click(Locators.SUBMIT_BUTTON_WORKDAY_EUROPE_BUTTON)
        time.sleep(8)

    def fill_workday_europe_support_model_end_user(self):
        try:
            self.click(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
            self.enter_text(Locators.SEARCH_TEXTBOX_MODULE_END_USER, "Workday Europe Support")
            self.send_enter(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
            self.click(Locators.WORK_DAY_EUROPE_SUPPORT_OPTION)
            self.select_issue_inquiry()
            self.fill_description()
            self.click_submit()

            allure.attach(self.driver.get_screenshot_as_png(), name="Work Day Europe Support",
                      attachment_type=AttachmentType.PNG)

        except:

            allure.attach(self.driver.get_screenshot_as_png(), name="Work Day Europe Support",
                         attachment_type=AttachmentType.PNG)
            assert False




