import allure
from allure_commons.types import AttachmentType

from Locators.ui_mapping import Locators
from Pages.BasePage import BasePage
import time


class AccessModuleEndUser(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def fill_printer_issue(self):
        self.click(Locators.PRINTER_ISSUE_PRINTER_ISSUE)
        self.click(Locators.PRINTER_ISSUE_PRINTER_ISSUE_TEXTBOX)
        self.enter_text(Locators.PRINTER_ISSUE_PRINTER_ISSUE_TEXTBOX, "OKTA")
        time.sleep(3)
        self.send_enter(Locators.PRINTER_ISSUE_PRINTER_ISSUE_TEXTBOX)

    def fill_printer_id(self):
        self.click(Locators.PRINTER_ID_PRINTER_ISSUE)
        self.enter_text(Locators.SUMMARY_ACCESS_TEXTBOX, "TEST")
        time.sleep(3)
        self.send_enter(Locators.SUMMARY_ACCESS_TEXTBOX)

    def fill_summary(self):
        self.click(Locators.SUMMARY_PRINTER_ISSUE)
        self.enter_text(Locators.SUMMARY_PRINTER_ISSUE, "DESC")
        time.sleep(3)
        self.send_enter(Locators.SUMMARY_PRINTER_ISSUE)

    def fill_description(self):
        self.click(Locators.DESCRIPTION_PRINTER_ISSUE)
        self.enter_text(Locators.DESCRIPTION_PRINTER_ISSUE, "DESC")
        time.sleep(3)
        self.send_enter(Locators.DESCRIPTION_PRINTER_ISSUE)

    def click_submit(self):
        self.click(Locators.SUBMIT_BUTTON_PRINTER_ISSUE)
        time.sleep(5)

    def fill_printer_module_end_user(self):
        try:
            elf.click(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
            self.enter_text(Locators.SEARCH_TEXTBOX_MODULE_END_USER, "PRINTER ISSUE")
            self.send_enter(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
            self.click(Locators.ACCESS_CLICK)
            time.sleep(5)

            self.fill_printer_issue()
            self.fill_printer_id()
            self.fill_summary()
            self.fill_description()
            self.click_submit()
            allure.attach(self.driver.get_screenshot_as_png(), name="Access Module",
                          attachment_type=AttachmentType.PNG)


        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="Access Module",
                          attachment_type=AttachmentType.PNG)
            assert False
