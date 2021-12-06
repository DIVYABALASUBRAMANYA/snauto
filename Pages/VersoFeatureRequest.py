from allure_commons.types import AttachmentType

from Locators.ui_mapping import Locators
from Pages.BasePage import BasePage
import time
import allure


class VersoFeatureRequestModuleEndUser(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def choose_urgency(self):
        self.click(Locators.URGENCY_VERSO_FEATURE_REQUEST)
        time.sleep(2)
        self.click(Locators.URGENCY_VERSO_FEATURE_REQUEST_TEXTBOX)
        time.sleep(2)
        self.enter_text(Locators.URGENCY_VERSO_FEATURE_REQUEST_TEXTBOX, "High")
        self.send_enter(Locators.URGENCY_VERSO_FEATURE_REQUEST_TEXTBOX)
        time.sleep(3)

    def choose_brand(self):
        self.click(Locators.BRAND_VERSO_FEATURE_REQUEST)
        time.sleep(2)
        self.click(Locators.BRAND_VERSO_FEATURE_REQUEST_TEXTBOX)
        time.sleep(2)
        self.enter_text(Locators.BRAND_VERSO_FEATURE_REQUEST_TEXTBOX, "AD India")
        time.sleep(3)
        self.send_enter(Locators.BRAND_VERSO_FEATURE_REQUEST_TEXTBOX)
        time.sleep(3)

    def fill_page_url(self):
        time.sleep(10)
        self.click(Locators.UNLOCK_VERSO_FEATURE_REQUEST_BUTTON)
        time.sleep(2)
        self.click(Locators.PAGE_VERSO_FEATURE_REQUEST_TEXTBOX)
        time.sleep(4)
        self.enter_text(Locators.PAGE_VERSO_FEATURE_REQUEST_TEXTBOX, "https://supporttest.condenastint.com/sp?id=sc_cat_item&sys_id=d7ca3698db7568101f8fb4c4f396191e")
        time.sleep(3)
        self.click(Locators.LOCK_VERSO_FEATURE_REQUEST_BUTTON)
        time.sleep(3)

    def fill_description(self):
        self.click(Locators.DESCRIPTION_VERSO_FEATURE_REQUEST_TEXTBOX)
        self.enter_text(Locators.DESCRIPTION_VERSO_FEATURE_REQUEST_TEXTBOX, "TEST")
        time.sleep(3)
        self.send_enter(Locators.DESCRIPTION_VERSO_FEATURE_REQUEST_TEXTBOX)
        time.sleep(3)

    def fill_justification(self):
        self.click(Locators.JUSTIFICATION_VERSO_FEATURE_REQUEST_TEXTBOX)
        self.enter_text(Locators.JUSTIFICATION_VERSO_FEATURE_REQUEST_TEXTBOX, "TEST")
        time.sleep(3)
        self.send_enter(Locators.JUSTIFICATION_VERSO_FEATURE_REQUEST_TEXTBOX)
        time.sleep(3)

    def click_submit(self):
        self.click(Locators.SUBMIT_VERSO_FEATURE_REQUEST)
        time.sleep(5)

    def fill_verso_feature_request_brand_ens_user_module(self):
        try:
            self.click(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
            self.enter_text(Locators.SEARCH_TEXTBOX_MODULE_END_USER, "VERSO FEATURE REQUEST")
            time.sleep(3)
            self.send_enter(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
            time.sleep(2)
            self.click(Locators.VERSO_FEATURE_REQUEST_CLICK)
            time.sleep(5)

            self.choose_urgency()
            self.choose_brand()
            self.fill_page_url()
            self.fill_description()
            self.fill_justification()
            self.click_submit()
            allure.attach(self.driver.get_screenshot_as_png(), name="VERSO FEATURE REQUEST",
                          attachment_type=AttachmentType.PNG)

        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="VERSO FEATURE REQUEST",
                          attachment_type=AttachmentType.PNG)
            assert False
