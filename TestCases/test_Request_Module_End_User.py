"""Request module end user test case"""
from Pages.RequestModuleEndUser import RequestModuleEndUser
from TestCases.test_base import BaseTest
from Config.login_cred import LoginCred
import time

"""PASSED"""


class TestRequestModuleEndUser(BaseTest):

    # def setUp(self):
    #     # to call the setUp() method of base class or super class.
    #     super().setUp()

    def test_request_module_end_user(self):
        print("inside")
        self.driver.get("https://supporttest.condenastint.com/sp")
        time.sleep(3)
        login_cred_obj = LoginCred(self.driver)
        login_cred_obj.login_cred()
        time.sleep(40)
        self.request_module_end_use_obj = RequestModuleEndUser(self.driver)
        self.request_module_end_use_obj.fill_request_module_end_user()
