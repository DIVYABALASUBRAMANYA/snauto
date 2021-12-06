import allure
from allure_commons.types import AttachmentType

from Locators.ui_mapping import Locators
from Pages.BasePage import BasePage
import time


class MoversRequestEndUser(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # def fill_affected_user(self):
    #     self.click(Locators.AFFECTED_USER_EDITORIAL_SYSTEMS)
    #     time.sleep(2)
    #     self.click(Locators.AFFECTED_USER_EDITORIAL_SYSTEMS_TEXTBOX)
    #     self.enter_text(Locators.AFFECTED_USER_EDITORIAL_SYSTEMS_TEXTBOX, "")
    #     time.sleep(3)
    #     self.send_enter(Locators.AFFECTED_USER_EDITORIAL_SYSTEMS_TEXTBOX)

    def choose_current_location(self):
        self.click(Locators.CURRENT_LOCATION_MOVER_REQUEST)
        time.sleep(2)
        self.click(Locators.CURRENT_LOCATION_MOVER_REQUEST_TEXTBOX)
        time.sleep(2)
        self.enter_text(Locators.CURRENT_LOCATION_MOVER_REQUEST_TEXTBOX, "Remote")
        time.sleep(2)
        self.send_enter(Locators.CURRENT_LOCATION_MOVER_REQUEST_TEXTBOX)
        time.sleep(3)

    def fill_current_desk_or_floor(self):
        self.click(Locators.CURRENT_DESK_POSITION_MOVER_REQUEST_TEXTBOX)
        time.sleep(2)
        self.enter_text(Locators.CURRENT_DESK_POSITION_MOVER_REQUEST_TEXTBOX, "TEST")
        self.send_enter(Locators.CURRENT_DESK_POSITION_MOVER_REQUEST_TEXTBOX)
        time.sleep(3)

    def choose_location_the_person_moving(self):
        self.click(Locators.LOCATION_PERSON_IS_MOVING_MOVER_REQUEST)
        time.sleep(2)
        self.click(Locators.LOCATION_PERSON_IS_MOVING_MOVER_REQUEST_TEXTBOX_MOVERS_REQUEST)
        time.sleep(2)
        self.enter_text(Locators.LOCATION_PERSON_IS_MOVING_MOVER_REQUEST_TEXTBOX_MOVERS_REQUEST, "Remote-US-DE")
        time.sleep(2)
        self.send_enter(Locators.LOCATION_PERSON_IS_MOVING_MOVER_REQUEST_TEXTBOX_MOVERS_REQUEST)
        time.sleep(3)

    def fill_moving_desk_or_floor(self):
        self.click(Locators.DESK_FLOOR_LOCATION_THE_PERSON_IS_MOVING_TO_MOVERS_REQUEST)
        time.sleep(2)
        self.enter_text(Locators.DESK_FLOOR_LOCATION_THE_PERSON_IS_MOVING_TO_MOVERS_REQUEST, "TEST")
        self.send_enter(Locators.CURRENT_DESK_POSITION_MOVER_REQUEST_TEXTBOX)
        time.sleep(3)

    def click_submit(self):
        self.click(Locators.SUBMIT_MOVERS_REQUEST)
        time.sleep(5)

    def fill_movers_request_end_user(self):
        try:
            self.click(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
            self.enter_text(Locators.SEARCH_TEXTBOX_MODULE_END_USER, "MOVERS REQUEST")
            time.sleep(3)
            self.send_enter(Locators.SEARCH_TEXTBOX_MODULE_END_USER)
            time.sleep(2)
            self.click(Locators.MMOVERS_REQUEST_CLICK)
            time.sleep(3)

            self.choose_current_location()
            self.fill_current_desk_or_floor()
            self.choose_location_the_person_moving()
            self.fill_moving_desk_or_floor()
            self.click_submit()
            allure.attach(self.driver.get_screenshot_as_png(), name="Movers Request",
                          attachment_type=AttachmentType.PNG)

        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="Password Reset",
                          attachment_type=AttachmentType.PNG)
            assert False

