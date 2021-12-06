import allure
from allure_commons.types import AttachmentType

from Locators.ui_mapping import Locators
from Pages.BasePage import BasePage
import time


class AVBreakFixTicketModuleEndUser(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def choose_category(self):
        self.click(Locators.CATEGORY_AV_BREAK_FIX_TICKET)
        self.click(Locators.CATEGORY_AV_BREAK_FIX_TICKET_TEXTBOX)
        time.sleep(3)
        self.enter_text(Locators.CATEGORY_AV_BREAK_FIX_TICKET_TEXTBOX, "High")
        self.send_enter(Locators.CATEGORY_AV_BREAK_FIX_TICKET_TEXTBOX)
        time.sleep(3)

    def fill_location(self):
        self.click(Locators.LOCATION_AV_BREAK_FIX_TICKET)
        self.enter_text(Locators.LOCATION_AV_BREAK_FIX_TICKET, "TEST")
        time.sleep(3)
        self.send_enter(Locators.LOCATION_AV_BREAK_FIX_TICKET)
        time.sleep(5)

    def choose_urgency(self):
        self.click(Locators.URGENCY_AV_BREAK_FIX_TICKET)
        self.click(Locators.URGENCY_AV_BREAK_FIX_TICKET_TEXTBOX)
        time.sleep(3)
        self.enter_text(Locators.URGENCY_AV_BREAK_FIX_TICKET_TEXTBOX, "High")
        self.send_enter(Locators.URGENCY_AV_BREAK_FIX_TICKET_TEXTBOX)
        time.sleep(3)

    def fill_summary(self):
        self.click(Locators.SUMMARY_AV_BREAK_FIX_TICKET)
        self.enter_text(Locators.SUMMARY_AV_BREAK_FIX_TICKET, "TEST")
        time.sleep(3)
        self.send_enter(Locators.SUMMARY_AV_BREAK_FIX_TICKET)
        time.sleep(5)

    def fill_description(self):
        self.click(Locators.DESCRIPTION_AV_BREAK_FIX_TICKET)
        self.enter_text(Locators.DESCRIPTION_AV_BREAK_FIX_TICKET, "TEST")
        time.sleep(3)
        self.send_enter(Locators.DESCRIPTION_AV_BREAK_FIX_TICKET)
        time.sleep(5)

    def click_submit(self):
        self.click(Locators.SUBMIT_AV_BREAK_FIX_TICKET)
        time.sleep(5)

    def fill_av_break_fix_ticket_module_end_user(self):

        try:
            self.click(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
            self.enter_text(Locators.SEARCH_TEXTBOX_MODULE_END_USER, "Ask a Question")
            time.sleep(3)
            self.send_enter(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
            time.sleep(2)
            self.click(Locators.ASK_A_QUESTION_CLICK)

            time.sleep(2)
            self.choose_category()
            self.fill_location()
            self.choose_urgency()
            self.fill_summary()
            self.fill_description()
            self.click_submit()
            allure.attach(self.driver.get_screenshot_as_png(), name="AV Break fix ",
                          attachment_type=AttachmentType.PNG)

        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="AV Break fix ",
                          attachment_type=AttachmentType.PNG)
            assert False





