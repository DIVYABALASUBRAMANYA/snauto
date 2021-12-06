import allure
from allure_commons.types import AttachmentType

from Locators.ui_mapping import Locators
from Pages.BasePage import BasePage
import time


@allure.severity(allure.severity_level.NORMAL)
class AskAQuestionModuleEndUser(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def fill_office(self, office):
        self.click(Locators.OFFICE_ASK_A_QUESTION_CLICK)
        self.click(Locators.OFFICE_ASK_A_QUESTION_TEXTBOX)
        self.enter_text(Locators.OFFICE_ASK_A_QUESTION_TEXTBOX, office)
        time.sleep(5)
        self.send_enter(Locators.OFFICE_ASK_A_QUESTION_TEXTBOX)
        time.sleep(5)

    def fill_summary(self, summary):
        self.click(Locators.SUMMARY_ASK_A_QUESTION_TEXTBOX)
        self.enter_text(Locators.SUMMARY_ASK_A_QUESTION_TEXTBOX, summary)
        self.send_enter(Locators.SUMMARY_ASK_A_QUESTION_TEXTBOX)

    def fill_description(self, description):
        self.click(Locators.DESCRIPTION_ASK_A_QUESTION_TEXTBOX)
        self.enter_text(Locators.DESCRIPTION_ASK_A_QUESTION_TEXTBOX, description)
        self.send_enter(Locators.DESCRIPTION_ASK_A_QUESTION_TEXTBOX)

    def click_submit(self):
        self.click(Locators.SUBMIT_ASK_A_QUESTION_BUTTON)
        self.is_visible(Locators.FULFILLMENT_ASK_A_QUESTION)

    # def fill_ask_a_question_module_fields_end_user(self):
    def fill_ask_a_question_module_fields_end_user(self, office, summary, description):
        try:

            self.click(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
            self.enter_text(Locators.SEARCH_TEXTBOX_MODULE_END_USER, "Ask a Question")
            time.sleep(3)
            # self.driver.implicitly_wait(10)
            self.send_enter(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
            time.sleep(2)
            # self.driver.implicitly_wait(10)
            self.click(Locators.ASK_A_QUESTION_CLICK)
            time.sleep(2)

            self.click(Locators.TITLE_ASK_A_QUESTION)

            self.fill_office(office)
            self.fill_summary(summary)
            self.fill_description(description)
            self.click_submit()

            allure.attach(self.driver.get_screenshot_as_png(), name="Ask a question",
                          attachment_type=AttachmentType.PNG)
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name=" Ask a question",
                          attachment_type=AttachmentType.PNG)
            assert False





