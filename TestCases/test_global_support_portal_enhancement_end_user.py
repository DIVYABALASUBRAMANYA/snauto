"""Request module end user test case"""
from Pages.GlobalSupportPortalEnhancementModuleEndUser import GlobalSupportEnhancementEndUser
from TestCases.test_base import BaseTest
from Config.login_cred import LoginCred
import time

""" PASSED """


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
        self.global_support_enhancement_end_use_obj = GlobalSupportEnhancementEndUser(self.driver)
        self.global_support_enhancement_end_use_obj.fill_global_support_portal_enhancement_module_end_user()
