import allure
from allure_commons.types import AttachmentType

from Locators.ui_mapping import Locators
from Pages.BasePage import BasePage
import time


class PenDriveRequestModuleEndUser(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def choose_office(self):
        self.click(Locators.OFFICE_PEN_DRIVE)
        time.sleep(3)
        self.click(Locators.OFFICE_PEN_DRIVE_TEXTBOX)
        time.sleep(3)
        self.enter_text(Locators.OFFICE_PEN_DRIVE_TEXTBOX, "1WTC NY")
        time.sleep(3)
        self.send_enter(Locators.OFFICE_PEN_DRIVE_TEXTBOX)
        time.sleep(3)

    def fill_summary(self):
        self.click(Locators.SUMMARY_PEN_DRIVE)
        self.clear_text(Locators.SUMMARY_PEN_DRIVE)
        self.enter_text(Locators.SUMMARY_PEN_DRIVE, "TEST SUMMARY")
        time.sleep(3)
        self.send_enter(Locators.SUMMARY_PEN_DRIVE)
        time.sleep(3)

    def fill_intended_use_of_equipment(self):
        self.click(Locators.INTENDED_USE_OF_EQUIPMENT_PEN_DRIVE)
        self.enter_text(Locators.INTENDED_USE_OF_EQUIPMENT_PEN_DRIVE, "Description")
        time.sleep(3)
        self.send_enter(Locators.INTENDED_USE_OF_EQUIPMENT_PEN_DRIVE)
        time.sleep(3)

    def fill_date_required(self):
        self.click(Locators.DATE_REQUIRED_PEN_DRIVE)
        self.enter_text(Locators.DATE_REQUIRED_PEN_DRIVE, "2021-11-19")
        time.sleep(3)
        self.send_enter(Locators.DATE_REQUIRED_PEN_DRIVE)
        time.sleep(3)

    def click_submit(self):
        self.click(Locators.SUBMIT_BTN)
        time.sleep(5)

    def fill_pen_drive_request_module_end_user(self):
        try:
            self.click(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
            self.enter_text(Locators.SEARCH_TEXTBOX_MODULE_END_USER, "PEN DRIVE")
            self.send_enter(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
            self.click(Locators.PEN_DRIVE_CLICK)
            time.sleep(5)

            self.choose_office()
            self.fill_summary()
            self.fill_intended_use_of_equipment()
            self.fill_date_required()
            self.click_submit()
            allure.attach(self.driver.get_screenshot_as_png(), name="Pen Drive",
                          attachment_type=AttachmentType.PNG)

        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="Pen Drive",
                          attachment_type=AttachmentType.PNG)
            assert False





