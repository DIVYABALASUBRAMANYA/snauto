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
from TestCase.BaseTestCase import Test_Base_Test_Case


class IncidentItilAgent(BasePage,Test_Base_Test_Case):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_value_on_global_search(self):
        time.sleep(10)
        self.click(Locators.ITIL_GLOBAL_SEARCH_ICON)
        time.sleep(5)
        self.click(Locators.ITIL_GLOBAL_SEARCH_TEXT_BOX)
        time.sleep(7)
        self.enter_text(Locators.ITIL_GLOBAL_SEARCH_TEXT_BOX, "INC0074281")
        time.sleep(10)
        self.send_enter(Locators.ITIL_GLOBAL_SEARCH_TEXT_BOX)
        time.sleep(8)

    def choose_category(self):
        self.click(Locators.ITIL_INCIDENT_CATEGORY)
        self.select_dropdown_by_value(Locators.ITIL_INCIDENT_CATEGORY, "Database")

    def fill_assignment_group(self):
        self.click(Locators.INCIDENT_ASSIGNMENT_GROUP)
        self.enter_text(Locators.INCIDENT_ASSIGNMENT_GROUP, "GLB-Global Support-US")
        self.send_enter(Locators.INCIDENT_ASSIGNMENT_GROUP)

    def fill_assigned_to(self):
        self.click(Locators.ITIL_INCIDENT_ASIGNEE)
        time.sleep(3)
        self.enter_text(Locators.ITIL_INCIDENT_ASIGNEE, "Paula Tinney")
        time.sleep(3)
        self.send_enter(Locators.ITIL_INCIDENT_ASIGNEE)
        # self.take_screenshot()

    def click_update_btn(self):
        self.click(Locators.ITIL_INCIDENT_UPDATE_BTN)
        time.sleep(3)

    def fill_office(self):
        time.sleep(10)
        self.click(Locators.ITIL_INCIDENT_OFFICE)
        time.sleep(2)
        self.enter_text(Locators.ITIL_INCIDENT_OFFICE, "Unites States")
        time.sleep(3)
        self.send_enter(Locators.ITIL_INCIDENT_OFFICE)
        time.sleep(3)

    def fill_itil_incident_form(self):
        print("Inside itil")
        self.enter_value_on_global_search()
        self.switch_frame("gsft_main")
        self.fill_assigned_to()
        self.fill_office()
        # self.choose_category()
        # self.fill_assignment_group()

        self.click_update_btn()
