import allure
from allure_commons.types import AttachmentType

from Locators.ui_mapping import Locators
from Pages.BasePage import BasePage
import time


class TerminationRequestModuleEndUser(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def fill_manager_name(self):
        self.click(Locators.MANAGER_TERMINATION_REQUEST)
        time.sleep(3)
        self.click(Locators.MANAGER_TERMINATION_REQUEST_TEXTBOX)
        time.sleep(3)
        self.enter_text(Locators.MANAGER_TERMINATION_REQUEST_TEXTBOX, "aastha yadav")
        time.sleep(3)
        self.send_enter(Locators.MANAGER_TERMINATION_REQUEST_TEXTBOX)
        time.sleep(4)

    def fill_employee_name(self):
        self.click(Locators.EMPLOYEE_NAME_TERMINATION_REQUEST)
        time.sleep(3)
        self.click(Locators.EMPLOYEE_NAME_TERMINATION_REQUEST_TEXTBOX)
        time.sleep(3)
        self.enter_text(Locators.EMPLOYEE_NAME_TERMINATION_REQUEST_TEXTBOX, "Abby Pond")
        time.sleep(3)
        self.send_enter(Locators.EMPLOYEE_NAME_TERMINATION_REQUEST_TEXTBOX)
        time.sleep(2)

    def fill_date_required(self):
        self.click(Locators.TERMINATION_DATE_TERMINATION_REQUEST)
        time.sleep(2)
        self.enter_text(Locators.TERMINATION_DATE_TERMINATION_REQUEST, "2021-11-30")
        time.sleep(3)
        self.send_enter(Locators.TERMINATION_DATE_TERMINATION_REQUEST)
        time.sleep(2)

    def fill_additional_information(self):
        self.click(Locators.ADDITIONAL_INFORMATION_TERMINATION_REQUEST)
        time.sleep(5)
        self.enter_text(Locators.ADDITIONAL_INFORMATION_TERMINATION_REQUEST, "DESC")
        time.sleep(3)
        self.send_enter(Locators.ADDITIONAL_INFORMATION_TERMINATION_REQUEST)
        time.sleep(3)

    def click_submit(self):
        self.click(Locators.SUBMIT_BUTTON_PRINTER_ISSUE)
        time.sleep(10)

    def fill_termination_request(self):
        try:
            self.click(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
            self.enter_text(Locators.SEARCH_TEXTBOX_MODULE_END_USER, "TERMINATION REQUEST")
            self.send_enter(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
            self.click(Locators.TERMINATION_REQUEST_CLICK)
            time.sleep(5)

            self.fill_manager_name()
            self.fill_employee_name()
            self.fill_date_required()
            self.fill_additional_information()
            self.click_submit()
            allure.attach(self.driver.get_screenshot_as_png(), name="TERMINATION REQUEST",
                          attachment_type=AttachmentType.PNG)

        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="TERMINATION REQUEST",
                          attachment_type=AttachmentType.PNG)
            assert False


