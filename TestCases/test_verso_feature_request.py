"""
VERSO FEATURE REQUEST end user test case
Author : Divya B, CNTL
"""


from Pages.VersoFeatureRequest import VersoFeatureRequestModuleEndUser
from TestCases.test_base import BaseTest
import time
from Config.login_cred import LoginCred
from Config.config import TestData


class TestPrinterIssueEndUser(BaseTest):

    # def setUp(self):
    #     # to call the setUp() method of base class or super class.
    #     super().setUp()

    def test_verso_feature_request_end_user(self):
        self.driver.get(TestData.SN_END_USER_PORTAL)
        time.sleep(3)
        login_cred_obj = LoginCred(self.driver)
        login_cred_obj.login_cred()
        time.sleep(40)
        self.verso_feature_request_module_end_user_obj = VersoFeatureRequestModuleEndUser(self.driver)
        self.verso_feature_request_module_end_user_obj.fill_verso_feature_request_brand_ens_user_module()


"""PASSED"""
