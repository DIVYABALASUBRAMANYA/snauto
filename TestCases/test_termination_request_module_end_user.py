"""
Termination module end user test case
Author : Divya B,CNTL
"""
from Pages.TerminationRequestModuleEndUser import TerminationRequestModuleEndUser
from TestCases.test_base import BaseTest
from Config.login_cred import LoginCred
import time
from Config.config import TestData

class TestTerminationRequestModuleEndUser(BaseTest):

    # def setUp(self):
    #     # to call the setUp() method of base class or super class.
    #     super().setUp()

    def test_termination_request_module_end_user(self):
        print("inside")
        self.driver.get(TestData.SN_END_USER_PORTAL)
        time.sleep(3)
        login_cred_obj = LoginCred(self.driver)
        login_cred_obj.login_cred()
        time.sleep(40)
        self.termination_request_module_end_use_obj = TerminationRequestModuleEndUser(self.driver)
        self.termination_request_module_end_use_obj.fill_termination_request()

"""passed"""
