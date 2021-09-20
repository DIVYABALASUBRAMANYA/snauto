import unittest
from selenium import webdriver
import time


class TestBaseTestCase(unittest.TestCase):

    if __name__ == '__main__':
        unittest.main()

    def setUp(self):
        # Setting up how we want Chrome to run
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(
            executable_path="/Users/dbalasub/PycharmProjects/pythonProject/Driver/chromedriver")
        # browser should be loaded in maximized window
        self.driver.maximize_window()
        self.driver.get("https://supporttest.condenastint.com/")
        time.sleep(80)

        # self.driver.implicitly_wait(20)
        # return self.driver

    # def take_screenshot(self):
    #     self.driver.save_screenshot("Incident")

    # def SetUp1(self):
    #     self.driver = webdriver.Chrome(
    #         executable_path="/Users/dbalasub/PycharmProjects/pythonProject/Driver/chromedriver")
    #     # browser should be loaded in maximized window
    #     self.driver.maximize_window()
    #     self.driver.get("https://supporttest.condenastint.com/")
    #     time.sleep(80)

    def tearDown(self):
        # To do the cleanup after test has executed.
        # self.driver.save_screenshot("")
        self.driver.close()
        self.driver.quit()

    # def tearDown1(self):
    #     # To do the cleanup after test has executed.
    #     # self.driver.save_screenshot("")
    #     self.driver.close()
    #     self.driver.quit()

    #comment