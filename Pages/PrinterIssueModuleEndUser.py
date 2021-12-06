import allure
from allure_commons.types import AttachmentType

from Locators.ui_mapping import Locators
from Pages.BasePage import BasePage
import time


class PrinterIssueModuleEndUser(BasePage):

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

    def fill_printer_issue(self):
        self.click(Locators.PRINTER_ISSUE_PRINTER_ISSUE)
        time.sleep(2)
        self.click(Locators.PRINTER_ISSUE_PRINTER_ISSUE_TEXTBOX)
        self.enter_text(Locators.PRINTER_ISSUE_PRINTER_ISSUE_TEXTBOX, "Error")
        time.sleep(3)
        self.send_enter(Locators.PRINTER_ISSUE_PRINTER_ISSUE_TEXTBOX)
        time.sleep(4)

    def fill_printer_id(self):
        self.click(Locators.PRINTER_ID_PRINTER_ISSUE)
        time.sleep(2)
        self.click(Locators.PRINTER_ID_PRINTER_ISSUE_TEXTBOX)
        time.sleep(2)
        self.enter_text(Locators.PRINTER_ID_PRINTER_ISSUE_TEXTBOX, "EDITOPS2")
        self.send_enter(Locators.PRINTER_ID_PRINTER_ISSUE_TEXTBOX)
        time.sleep(3)

    def fill_description(self):
        self.click(Locators.DESCRIPTION_PRINTER_ISSUE)
        self.enter_text(Locators.DESCRIPTION_PRINTER_ISSUE, "TEST")
        time.sleep(3)

    def submit(self):
        self.click(Locators.SUBMIT_BUTTON_PRINTER_ISSUE)
        time.sleep(5)

    def fill_printer_issue_end_user(self):
        try:
            self.click(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
            self.enter_text(Locators.SEARCH_TEXTBOX_MODULE_END_USER, "PRINTER_ISSUE")
            time.sleep(3)
            self.send_enter(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
            time.sleep(2)
            self.click(Locators.PRINTER_ISSUE_CLICK)

            time.sleep(3)
            self.fill_office()
            self.fill_printer_issue()
            self.fill_printer_id()
            self.fill_description()
            self.submit()

            allure.attach(self.driver.get_screenshot_as_png(), name="Printer Issue",
                          attachment_type=AttachmentType.PNG)

        except:

            allure.attach(self.driver.get_screenshot_as_png(), name="Printer Issue",
                          attachment_type=AttachmentType.PNG)
            assert False
