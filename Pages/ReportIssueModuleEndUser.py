import allure
from allure_commons.types import AttachmentType

from Locators.ui_mapping import Locators
from Pages.BasePage import BasePage
import time


@allure.severity(allure.severity_level.NORMAL)
class ReportIssueModuleEndUser(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def fill_brief_description(self):
        self.click(Locators.BRIEF_DESCRIPTION_REPORT_ISSUE_TEXTBOX)
        self.enter_text(Locators.BRIEF_DESCRIPTION_REPORT_ISSUE_TEXTBOX, "TEST SUMMARY")
        time.sleep(3)
        self.send_enter(Locators.BRIEF_DESCRIPTION_REPORT_ISSUE_TEXTBOX)
        time.sleep(5)

    def fill_detailed_description(self):
        self.click(Locators.DETAILED_DESCRIPTION_REPORT_ISSUE_TEXTBOX)
        self.enter_text(Locators.DETAILED_DESCRIPTION_REPORT_ISSUE_TEXTBOX, "Description")
        time.sleep(3)
        self.send_enter(Locators.DETAILED_DESCRIPTION_REPORT_ISSUE_TEXTBOX)
        time.sleep(5)

    def fill_possible_suggestions(self):
        self.click(Locators.POSSIBLE_SUGGESTIONS_REPORT_ISSUE_TEXTBOX)
        self.enter_text(Locators.POSSIBLE_SUGGESTIONS_REPORT_ISSUE_TEXTBOX, "Description")
        time.sleep(3)
        # self.send_enter(Locators.POSSIBLE_SUGGESTIONS_REPORT_ISSUE_TEXTBOX)
        time.sleep(5)

    def click_submit(self):
        self.click(Locators.SUBMIT_REPORT_ISSUE_BUTTON)
        time.sleep(5)

    def fill_report_issue_module_end_user(self):
        try:
            self.click(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
            self.enter_text(Locators.SEARCH_TEXTBOX_MODULE_END_USER, "REPORT ISSUE")
            self.send_enter(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
            self.click(Locators.REPORT_ISSUE_CLICK)
            time.sleep(5)

            self.fill_brief_description()
            self.fill_detailed_description()
            self.fill_possible_suggestions()
            self.click_submit()
            allure.attach(self.driver.get_screenshot_as_png(), name="Report Issue",
                          attachment_type=AttachmentType.PNG)

        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="Report issue",
                          attachment_type=AttachmentType.PNG)
            assert False

