"""
IP INFRIGMENT end user test case
Author : Divya B
"""

from Pages.IPInfringementOrImpersonation import IPInfringementOrImpersonationModuleEndUser
from TestCases.test_base import BaseTest
import time
from Config.login_cred import LoginCred


class TestIPInfringementOrImpersonationModuleEndUser(BaseTest):

    # def setUp(self):
    #     # to call the setUp() method of base class or super class.
    #     super().setUp()

    def test_ip_infringement_or_impersonation_module_end_user(self):
        print("inside")
        self.driver.get("https://supporttest.condenastint.com/sp")
        time.sleep(3)
        login_cred_obj = LoginCred(self.driver)
        login_cred_obj.login_cred()
        time.sleep(40)
        self.ip_infringement_or_impersonation_module_end_user_obj = IPInfringementOrImpersonationModuleEndUser(self.driver)
        self.ip_infringement_or_impersonation_module_end_user_obj.fill_ip_infringement_or_impersonation_module_end_user()
"""PASSED"""