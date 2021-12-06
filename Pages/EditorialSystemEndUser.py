import allure
from allure_commons.types import AttachmentType

from Locators.ui_mapping import Locators
from Pages.BasePage import BasePage
import time


@allure.severity(allure.severity_level.NORMAL)
class EditorialSystemModuleEndUser(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def fill_office(self):
        self.click(Locators.OFFICE_EDITORIAL_SYSTEMS)
        time.sleep(3)
        self.click(Locators.OFFICE_EDITORIAL_SYSTEMS_TEXTBOX)
        time.sleep(3)
        self.enter_text(Locators.OFFICE_EDITORIAL_SYSTEMS_TEXTBOX, "1WTC NY")
        time.sleep(3)
        self.send_enter(Locators.OFFICE_EDITORIAL_SYSTEMS_TEXTBOX)
        time.sleep(3)

    def fill_affected_user(self):
        self.click(Locators.AFFECTED_USER_EDITORIAL_SYSTEMS)
        time.sleep(2)
        self.click(Locators.AFFECTED_USER_EDITORIAL_SYSTEMS_TEXTBOX)
        self.enter_text(Locators.AFFECTED_USER_EDITORIAL_SYSTEMS_TEXTBOX, "Hari Sreekumaran")
        time.sleep(3)
        self.send_enter(Locators.AFFECTED_USER_EDITORIAL_SYSTEMS_TEXTBOX)

    def choose_urgency(self):
        self.click(Locators.URGENCY_EDITORIAL_SYSTEMS)
        time.sleep(2)
        self.click(Locators.URGENCY_EDITORIAL_SYSTEMS_TEXTBOX)
        time.sleep(2)
        self.enter_text(Locators.URGENCY_EDITORIAL_SYSTEMS_TEXTBOX, "High")
        self.send_enter(Locators.URGENCY_EDITORIAL_SYSTEMS_TEXTBOX)
        time.sleep(3)

    def fill_editorial_platform(self):
        self.click(Locators.EDITORIAL_PLATFORM_EDITORIAL_SYSTEMS)
        self.click(Locators.EDITORIAL_PLATFORM_EDITORIAL_SYSTEMS_TEXTBOX)
        time.sleep(2)
        self.enter_text(Locators.EDITORIAL_PLATFORM_EDITORIAL_SYSTEMS_TEXTBOX, "DAM")
        time.sleep(3)
        self.send_enter(Locators.EDITORIAL_PLATFORM_EDITORIAL_SYSTEMS_TEXTBOX)
        time.sleep(7)

    def fill_issue_type(self):
        self.click(Locators.ISSUE_TYPE_EDITORIAL_SYSTEMS)
        self.click(Locators.ISSUE_TYPE_EDITORIAL_SYSTEMS_TEXTBOX)
        time.sleep(3)
        self.enter_text(Locators.ISSUE_TYPE_EDITORIAL_SYSTEMS_TEXTBOX, "Video")
        self.send_enter(Locators.ISSUE_TYPE_EDITORIAL_SYSTEMS_TEXTBOX)
        time.sleep(3)

    def fill_device(self):
        self.click(Locators.DEVICE_EDITORIAL_SYSTEMS)
        self.click(Locators.DEVICE_EDITORIAL_SYSTEMS_TEXTBOX)
        time.sleep(2)
        self.enter_text(Locators.DEVICE_EDITORIAL_SYSTEMS_TEXTBOX, "Desktop")
        self.send_enter(Locators.DEVICE_EDITORIAL_SYSTEMS_TEXTBOX)

    def fill_operating_system(self):
        self.click(Locators.OPERATING_SYSTEM_EDITORIAL_SYSTEMS)
        self.click(Locators.OPERATING_SYSTEM_EDITORIAL_SYSTEMS_TEXTBOX)
        time.sleep(2)
        self.enter_text(Locators.OPERATING_SYSTEM_EDITORIAL_SYSTEMS_TEXTBOX, "Mac")
        self.send_enter(Locators.OPERATING_SYSTEM_EDITORIAL_SYSTEMS_TEXTBOX)
        time.sleep(5)

    def fill_browser(self):
        self.click(Locators.BROWSER_EDITORIAL_SYSTEMS)
        self.click(Locators.BROWSER_EDITORIAL_SYSTEMS_TEXTBOX)
        time.sleep(2)
        self.enter_text(Locators.BROWSER_EDITORIAL_SYSTEMS_TEXTBOX, "Chrome")
        time.sleep(3)
        self.send_enter(Locators.BROWSER_EDITORIAL_SYSTEMS_TEXTBOX)
        time.sleep(3)

    def fill_summary(self):
        self.enter_text(Locators.SUMMARY_EDITORIAL_SYSTEMS_TEXTBOX, "TEST SUMMARY")
        self.send_enter(Locators.SUMMARY_EDITORIAL_SYSTEMS_TEXTBOX)

    def fill_description(self):
        self.enter_text(Locators.DESCRIPTION_EDITORIAL_SYSTEMS_TEXTBOX, "Description")
        self.send_enter(Locators.DESCRIPTION_EDITORIAL_SYSTEMS_TEXTBOX)

    def click_submit(self):
        self.click(Locators.SUBMIT_BUTTON_EDITORIAL_SYSTEMS)
        self.is_visible(Locators.START_EDITIORIAL_SYSTEMS_INCIDENT)

    def fill_editorial_systems_module_end_user(self):
        try:
            self.click(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
            self.enter_text(Locators.SEARCH_TEXTBOX_MODULE_END_USER, "Editorial Systems Incident")
            time.sleep(3)
            self.send_enter(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
            time.sleep(2)
            self.click(Locators.EDITORIAL_SYSTEMS_CLICK)

            self.is_visible(Locators.EDITORIAL_SYSTEMS_TITLE)

            time.sleep(3)
            self.fill_affected_user()
            self.fill_office()
            self.choose_urgency()
            self.fill_editorial_platform()
            self.fill_issue_type()
            self.fill_device()

            self.fill_operating_system()
            self.fill_browser()
            self.fill_summary()
            self.fill_description()
            self.click_submit()

            allure.attach(self.driver.get_screenshot_as_png(), name="Editorial System ",attachment_type=AttachmentType.PNG)

        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="Editorial System ",
                          attachment_type=AttachmentType.PNG)
            assert False



