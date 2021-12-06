""" This page is the parent of all pages"""
""" This contains all the generic methods """

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class BasePage:
    """This class is the parent class for all the pages in our application."""
    """It contains all common elements and functionalities available to all pages."""

    # this function is called every time a new object of the base class is created.
    def __init__(self, driver):
        self.driver = driver

    # this function performs click on web element whose locator is passed to it.
    def click(self, by_locator):
        WebDriverWait(self.driver, 1000).until(EC.visibility_of_element_located(by_locator)).click()

    # this function asserts comparison of a web element's text with passed in text.
    def assert_element_text(self, by_locator, element_text):
        web_element = WebDriverWait(self.driver, 80).until(EC.visibility_of_element_located(by_locator))
        assert web_element.text == element_text

    # this function performs text entry of the passed in text, in a web element whose locator is passed to it.
    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 8000).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def send_enter(self, by_locator):
        return WebDriverWait(self.driver, 8000).until(EC.visibility_of_element_located(by_locator)).send_keys(Keys.ENTER)

    # this function checks if the web element whose locator has been passed to it, is enabled or not and returns
    # web element if it is enabled.
    def is_enabled(self, by_locator):
        return WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator))

    # this function checks if the web element whose locator has been passed to it, is visible or not and returns
    # true or false depending upon its visibility.
    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 1000).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    # def take_screenshot(self):
    #     driver.i

    # this function moves the mouse pointer over a web element whose locator has been passed to it.
    def hover_to(self, by_locator):
        element = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()

    # def double_click(self, locator):
    def select_dropdown_by_visible_text(self, by_locator, value):
        element = Select(WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator)))

        element.select_by_visible_text("value")

    def switch_frame(self, frame_id):
        self.driver.switch_to.frame(frame_id)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator))
        return element.text
    # def get_element_test(self, locator):
    #     element = self.driver.find_element


    def get_title(self, title):
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(title))
        return self.driver.title

    def clear_text(self,by_locator):
        return WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator)).clear()

    def implicit_wait(self, sec):
        self.driver.implicitly_wait(sec)
    # def save_screenshot(self):
