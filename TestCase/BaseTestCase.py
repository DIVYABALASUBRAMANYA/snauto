# import unittest
# from selenium import webdriver
# import time
# import pytest
#
#
# class TestBaseTestCase(unittest.TestCase):
#
#     if __name__ == '__main__':
#         unittest.main()
#
#     def setUp(self):
#         chrome_options = webdriver.ChromeOptions()
#         self.driver = webdriver.Chrome(
#              executable_path="/Users/dbalasub/PycharmProjects/pythonProject/Driver/chromedriver")
#         self.driver.maximize_window()
#         self.driver.get("https://supporttest.condenastint.com/sp")
#         time.sleep(80)
#
#     def tearDown(self):
#         """To do the cleanup after test has executed."""
#
#         self.driver.close()
#         self.driver.quit()
#     #
#     # # def tearDown1(self):
#     # #     # To do the cleanup after test has executed.
#     # #     # self.driver.save_screenshot("")
#     # #     self.driver.close()
#     # #     self.driver.quit()
#
#     #comment