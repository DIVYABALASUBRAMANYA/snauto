import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from Locators.ui_mapping import Locators
from Pages.BasePage import BasePage
from PILTools import Image


class IncidentEndUser(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def choose_category(self):
        self.click(Locators.CATEGORY)
        self.click(Locators.CATEGORY_SEARCH_BOX)
        time.sleep(5)
        self.enter_text(Locators.CATEGORY_SEARCH_BOX, "Finance")
        time.sleep(3)
        self.send_enter(Locators.CATEGORY_SEARCH_BOX)

    def choose_urgency(self):
        self.click(Locators.URGENCY)
        self.click(Locators.URGENCY_SEARCH_BOX)
        time.sleep(3)
        self.enter_text(Locators.URGENCY_SEARCH_BOX, "High")
        self.send_enter(Locators.URGENCY_SEARCH_BOX)
        time.sleep(3)

    def fill_summary(self):
        self.click(Locators.SUMMARY_TEXTBOX)
        self.enter_text(Locators.SUMMARY_TEXTBOX,"TEST")
        time.sleep(3)

    def fill_contact_phone_number(self):
        self.click(Locators.CONTACT_PHONE_NUMBER_TEXTBOX)
        self.enter_text(Locators.CONTACT_PHONE_NUMBER_TEXTBOX, "1234")
        time.sleep(3)

    def fill_description(self):
        self.click(Locators.DESCRIPTION_TEXTBOX)
        self.enter_text(Locators.DESCRIPTION_TEXTBOX, "DESC")
        time.sleep(3)

    def click_submit(self):
        self.click(Locators.SUBMIT_BTN)
        time.sleep(8)






    # def test_fun(self):
    #     self.click(Locators.TEST)
    #     self.enter_text(Locators.TEST, "shoes")


    # def setUserName(self, username):
    #     self.driver.find_element_by_id(self.textbox_loginid).clear()
    #     self.driver.find_element_by_id(self.textbox_loginid).send_keys(username)
    #
    # def clicknext(self):
    #     self.driver.find_element_by_id(self.nextbutton).click()
    #
    # def setPassword(self, password):
    #     self.driver.find_element_by_class_name(self.textbox_loginps).clear()
    #     self.driver.find_element_by_class_name(self.textbox_loginps).send_keys(password)
    #
    # def clicklogin(self):
    #     self.driver.find_element_by_css_selector(self.loginbutton).click()
    #
    # def clickPush(self):
    #     self.driver.find_element_by_xpath(self.pushbutton).click()

    def fill_incident_end_user_form(self):
        self.click(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
        self.enter_text(Locators.SEARCH_TEXTBOX_MODULE_END_USER, "Something is broken")
        self.send_enter(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
        self.click(Locators.INCIDENT_MODULE_OPTION)
        print("inside page")
        self.choose_category()
        self.choose_urgency()
        self.fill_summary()
        self.fill_contact_phone_number()
        self.fill_description()
        self.click_submit()

