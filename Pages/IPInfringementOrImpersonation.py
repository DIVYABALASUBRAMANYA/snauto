import allure
from allure_commons.types import AttachmentType

from Locators.ui_mapping import Locators
from Pages.BasePage import BasePage
import time


class IPInfringementOrImpersonationModuleEndUser(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def fill_category(self):
        self.click(Locators.CATEGORY_IP_INFRINGEMENT_OR_IMPERSONATION)
        time.sleep(3)
        self.click(Locators.CATEGORY_IP_INFRINGEMENT_OR_IMPERSONATION_TEXTBOX)
        time.sleep(3)
        self.enter_text(Locators.CATEGORY_IP_INFRINGEMENT_OR_IMPERSONATION_TEXTBOX, "Other")
        self.send_enter(Locators.CATEGORY_IP_INFRINGEMENT_OR_IMPERSONATION_TEXTBOX)
        time.sleep(2)

    def fill_summary(self):
        self.click(Locators.SUMMARY_IP_INFRINGEMENT_OR_IMPERSONATION_TEXTBOX)
        time.sleep(2)
        self.enter_text(Locators.SUMMARY_IP_INFRINGEMENT_OR_IMPERSONATION_TEXTBOX, "DESC")
        time.sleep(3)
        self.send_enter(Locators.SUMMARY_IP_INFRINGEMENT_OR_IMPERSONATION_TEXTBOX)

    def fill_description(self):
        self.click(Locators.DESCRIPTION_IP_INFRINGEMENT_OR_IMPERSONATION_TEXTBOX)
        time.sleep(2)
        self.enter_text(Locators.DESCRIPTION_IP_INFRINGEMENT_OR_IMPERSONATION_TEXTBOX, "DESC")
        time.sleep(3)
        self.send_enter(Locators.DESCRIPTION_IP_INFRINGEMENT_OR_IMPERSONATION_TEXTBOX)

    def click_submit(self):
        self.click(Locators.SUBMIT_IP_INFRINGEMENT_OR_IMPERSONATION_BUTTON)
        time.sleep(5)

    def fill_ip_infringement_or_impersonation_module_end_user(self):

        try:
            self.click(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
            self.enter_text(Locators.SEARCH_TEXTBOX_MODULE_END_USER, "IP Infringement or Impersonation")
            self.send_enter(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
            self.click(Locators.IP_INFRIGMENT_CLICK)
            time.sleep(5)

            self.fill_category()
            self.fill_summary()
            self.fill_description()
            self.click_submit()

            allure.attach(self.driver.get_screenshot_as_png(), name="IP Infirgment",
                          attachment_type=AttachmentType.PNG)

        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="IP Infirgment",
                          attachment_type=AttachmentType.PNG)
            assert False
