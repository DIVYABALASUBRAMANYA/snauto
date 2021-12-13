import allure
from allure_commons.types import AttachmentType

from Locators.ui_mapping import Locators
from Pages.BasePage import BasePage
import time


@allure.severity(allure.severity_level.NORMAL)
class EditorialSystemModuleEndUser(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def fill_caller(self, caller):
        if caller is None:
            pass
        else:
            self.click(Locators.CALLER_EDITORIAL_SYSTEMS)
            time.sleep(3)
            self.click(Locators.CALLER_EDITORIAL_SYSTEMS_TEXTBOX)
            time.sleep(3)
            self.enter_text(Locators.CALLER_EDITORIAL_SYSTEMS_TEXTBOX, caller)
            time.sleep(3)
            self.send_enter(Locators.CALLER_EDITORIAL_SYSTEMS_TEXTBOX)
            time.sleep(3)

    def fill_office(self, office):
        self.click(Locators.OFFICE_EDITORIAL_SYSTEMS)
        time.sleep(3)
        self.click(Locators.OFFICE_EDITORIAL_SYSTEMS_TEXTBOX)
        time.sleep(3)
        self.enter_text(Locators.OFFICE_EDITORIAL_SYSTEMS_TEXTBOX, office)
        time.sleep(3)
        self.send_enter(Locators.OFFICE_EDITORIAL_SYSTEMS_TEXTBOX)
        time.sleep(3)

    def fill_affected_user(self, affected_user):
        if affected_user is None:
            pass
        else:
            self.click(Locators.AFFECTED_USER_EDITORIAL_SYSTEMS)
            time.sleep(2)
            self.click(Locators.AFFECTED_USER_EDITORIAL_SYSTEMS_TEXTBOX)
            self.enter_text(Locators.AFFECTED_USER_EDITORIAL_SYSTEMS_TEXTBOX, affected_user)
            time.sleep(3)
            self.send_enter(Locators.AFFECTED_USER_EDITORIAL_SYSTEMS_TEXTBOX)

    def choose_urgency(self, urgency):
        if urgency is None:
            pass
        else:
            self.click(Locators.URGENCY_EDITORIAL_SYSTEMS)
            time.sleep(2)
            self.click(Locators.URGENCY_EDITORIAL_SYSTEMS_TEXTBOX)
            time.sleep(2)
            self.enter_text(Locators.URGENCY_EDITORIAL_SYSTEMS_TEXTBOX, urgency)
            self.send_enter(Locators.URGENCY_EDITORIAL_SYSTEMS_TEXTBOX)
            time.sleep(3)

    def fill_editorial_platform(self, platform):
        self.click(Locators.EDITORIAL_PLATFORM_EDITORIAL_SYSTEMS)
        self.click(Locators.EDITORIAL_PLATFORM_EDITORIAL_SYSTEMS_TEXTBOX)
        time.sleep(2)
        self.enter_text(Locators.EDITORIAL_PLATFORM_EDITORIAL_SYSTEMS_TEXTBOX, platform)
        time.sleep(3)
        self.send_enter(Locators.EDITORIAL_PLATFORM_EDITORIAL_SYSTEMS_TEXTBOX)
        time.sleep(5)

    def fill_issue_type(self, issue_type):
        self.click(Locators.ISSUE_TYPE_EDITORIAL_SYSTEMS)
        self.click(Locators.ISSUE_TYPE_EDITORIAL_SYSTEMS_TEXTBOX)
        time.sleep(3)
        self.enter_text(Locators.ISSUE_TYPE_EDITORIAL_SYSTEMS_TEXTBOX, issue_type)
        self.send_enter(Locators.ISSUE_TYPE_EDITORIAL_SYSTEMS_TEXTBOX)
        time.sleep(3)

    def fill_device(self, device):
        if device is None:
            pass
        else:
            self.click(Locators.DEVICE_EDITORIAL_SYSTEMS)
            self.click(Locators.DEVICE_EDITORIAL_SYSTEMS_TEXTBOX)
            time.sleep(2)
            self.enter_text(Locators.DEVICE_EDITORIAL_SYSTEMS_TEXTBOX, device)
            self.send_enter(Locators.DEVICE_EDITORIAL_SYSTEMS_TEXTBOX)

    def fill_operating_system(self, operating_system):
        if operating_system is None:
            pass
        else:
            self.click(Locators.OPERATING_SYSTEM_EDITORIAL_SYSTEMS)
            self.click(Locators.OPERATING_SYSTEM_EDITORIAL_SYSTEMS_TEXTBOX)
            time.sleep(2)
            self.enter_text(Locators.OPERATING_SYSTEM_EDITORIAL_SYSTEMS_TEXTBOX, operating_system)
            self.send_enter(Locators.OPERATING_SYSTEM_EDITORIAL_SYSTEMS_TEXTBOX)
            time.sleep(5)

    def fill_browser(self, browser):
        if browser is None:
            pass
        else:
            self.click(Locators.BROWSER_EDITORIAL_SYSTEMS)
            self.click(Locators.BROWSER_EDITORIAL_SYSTEMS_TEXTBOX)
            time.sleep(2)
            self.enter_text(Locators.BROWSER_EDITORIAL_SYSTEMS_TEXTBOX, browser)
            time.sleep(3)
            self.send_enter(Locators.BROWSER_EDITORIAL_SYSTEMS_TEXTBOX)
            time.sleep(3)

    def fill_summary(self, summary):
        self.enter_text(Locators.SUMMARY_EDITORIAL_SYSTEMS_TEXTBOX, summary )
        self.send_enter(Locators.SUMMARY_EDITORIAL_SYSTEMS_TEXTBOX)

    def fill_description(self, description):
        self.enter_text(Locators.DESCRIPTION_EDITORIAL_SYSTEMS_TEXTBOX, description)
        self.send_enter(Locators.DESCRIPTION_EDITORIAL_SYSTEMS_TEXTBOX)

    def click_submit(self):
        self.click(Locators.SUBMIT_BUTTON_EDITORIAL_SYSTEMS)
        self.is_visible(Locators.START_EDITIORIAL_SYSTEMS_INCIDENT)

    def fill_editorial_systems_module_end_user(self, caller,office, affected_user, urgency,editorial_platform, issue_type , device, operating_system, browser,summary,description):
        try:
            self.click(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
            self.enter_text(Locators.SEARCH_TEXTBOX_MODULE_END_USER, "Editorial Systems Incident")
            time.sleep(3)
            self.send_enter(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
            time.sleep(2)
            self.click(Locators.EDITORIAL_SYSTEMS_CLICK)

            self.is_visible(Locators.EDITORIAL_SYSTEMS_TITLE)

            time.sleep(3)

            self.fill_caller(caller)
            self.fill_office(office)
            self.fill_affected_user(affected_user)
            self.choose_urgency(urgency)
            self.fill_editorial_platform(editorial_platform)
            self.fill_issue_type(issue_type)
            self.fill_device(device)

            self.fill_operating_system(operating_system)
            self.fill_browser(browser)
            self.fill_summary(summary)
            self.fill_description(description)
            self.click_submit()

            allure.attach(self.driver.get_screenshot_as_png(), name="Editorial System ",attachment_type=AttachmentType.PNG)

        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="Editorial System ",
                          attachment_type=AttachmentType.PNG)
            assert False



