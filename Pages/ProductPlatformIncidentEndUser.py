""" Product Platform incident end user page """

import time

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from Locators.ui_mapping import Locators
from Pages.BasePage import BasePage


class ProductPlatformIncidentEndUser(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://supporttest.condenastint.com/sp")
        self.click(Locators.USER_NAME_OKTA_TEXTBOX)
        self.enter_text(Locators.USER_NAME_OKTA_TEXTBOX, "DIVYA_BALASUBRAMANYA@CONDENAST.COM")
        time.sleep(3)
        self.click(Locators.NEXT_OKTA_BUTTON)
        time.sleep(3)
        self.click(Locators.PASSWORD_OKTA_TEXTBOX)
        self.enter_text(Locators.PASSWORD_OKTA_TEXTBOX, "Laptop12$Laptop")
        time.sleep(3)
        self.click(Locators.SUBMIT_OKTA_BUTTON)
        time.sleep(7)
        self.click(Locators.SEND_PUSH_OKTA_BUTTON)
        time.sleep(30)

    def select_product(self):
        self.click(Locators.PRODUCT_PRODUCT_PLATFORM)
        # time.sleep(5)
        self.click(Locators.PRODUCT_PRODUCT_PLATFORM_TEXTBOX)
        time.sleep(8)
        self.enter_text(Locators.PRODUCT_PRODUCT_PLATFORM_TEXTBOX, "archdigest.com")
        time.sleep(3)
        self.send_enter(Locators.PRODUCT_PRODUCT_PLATFORM_TEXTBOX)

    def select_sub_product(self):
        self.click(Locators.SUB_PRODUCT_PRODUCT_PLATFORM)
        # time.sleep(5)
        self.click(Locators.SUB_PRODUCT_PRODUCT_PLATFORM_TEXTBOX)
        time.sleep(8)
        self.enter_text(Locators.SUB_PRODUCT_PRODUCT_PLATFORM_TEXTBOX, "Encore")
        time.sleep(3)
        self.send_enter(Locators.SUB_PRODUCT_PRODUCT_PLATFORM_TEXTBOX)

    def choose_urgency(self):
        self.click(Locators.URGENCY_PRODUCT_PLATOFORM)
        self.click(Locators.URGENCY_PRODUCT_PLATOFORM_SEARCH_BOX)
        time.sleep(3)
        self.enter_text(Locators.URGENCY_PRODUCT_PLATOFORM_SEARCH_BOX, "High")
        self.send_enter(Locators.URGENCY_PRODUCT_PLATOFORM_SEARCH_BOX)
        time.sleep(3)

    def choose_incident_type(self):
        self.click(Locators.INCIDENT_TYPE_PRODUCT_PLATFORM)
        self.click(Locators.INCIDENT_TYPE_PRODUCT_PLATFORM_TEXTBOX)
        time.sleep(5)
        self.enter_text(Locators.INCIDENT_TYPE_PRODUCT_PLATFORM_TEXTBOX, "Other")
        time.sleep(5)
        self.send_enter(Locators.INCIDENT_TYPE_PRODUCT_PLATFORM_TEXTBOX)
        time.sleep(3)

    def select_device(self):
        self.click(Locators.DEVICE_PRODUCT_PLATFORM_DROPDOWN)
        # self.click(Locators.DEVICE_PRODUCT_PLATFORM_TEXTBOX)
        time.sleep(3)
        self.select_dropdown_by_value(Locators.DEVICE_PRODUCT_PLATFORM_TEXTBOX, "Laptop")

        # self.enter_text(Locators.DEVICE_PRODUCT_PLATFORM_DROPDOWN, "Laptop")
        self.send_enter(Locators.DEVICE_PRODUCT_PLATFORM_DROPDOWN)
        time.sleep(3)

    def select_operating_system(self):
        self.click(Locators.OPERATING_SYSTEM_PLATFORM)
        self.click(Locators.OPERATING_SYSTEM_PLATFORM_TEXTBOX)
        time.sleep(3)
        self.enter_text(Locators.OPERATING_SYSTEM_PLATFORM_TEXTBOX, "Mac")
        self.send_enter(Locators.OPERATING_SYSTEM_PLATFORM_TEXTBOX)
        time.sleep(3)

    def select_browser(self):
        self.click(Locators.BROWSER_PRODUCT_PLATFORM)
        self.click(Locators.BROWSER_PRODUCT_PLATFORM_TEXTBOX)
        time.sleep(3)
        self.enter_text(Locators.BROWSER_PRODUCT_PLATFORM_TEXTBOX, "Mac")
        self.send_enter(Locators.BROWSER_PRODUCT_PLATFORM_TEXTBOX)
        time.sleep(3)

    def fill_description(self):
        self.click(Locators.DESCRIPTION_PRODUCT_PLATFORM_TEXTBOX)
        self.enter_text(Locators.DESCRIPTION_PRODUCT_PLATFORM_TEXTBOX, "DESC")
        time.sleep(3)

    def click_submit(self):
        self.click(Locators.SUBMIT_PRODUCT_PLATFORM)
        time.sleep(8)

    def fill_product_platform_incident_end_user(self):
        try:
            self.click(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
            self.enter_text(Locators.SEARCH_TEXTBOX_MODULE_END_USER, "Product Platform Incident")
            self.send_enter(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
            self.click(Locators.PRODUCT_PLATFORM_INCIDENT_CLICK)
            self.select_product()
            self.select_sub_product()
            self.choose_urgency()
            self.choose_incident_type()
            self.select_device()
            self.select_operating_system()
            self.select_browser()
            self.fill_description()
            self.click_submit()
            allure.attach(self.driver.get_screenshot_as_png(), name="Product Platform Incident",
                      attachment_type=AttachmentType.PNG)

        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="Product Platform Incident",
                          attachment_type=AttachmentType.PNG)
            assert False

