"""Request module end user test case"""
from Pages.PasswordResetModuleEndUser import PasswordResetModuleEndUser
from TestCases.test_base import BaseTest
from Config.login_cred import LoginCred
import time
from Config.excelfunctions import read_data
import pytest

"""PASSED"""


class TestPasswordResetModuleEndUser(BaseTest):

    # def setUp(self):
    #     # to call the setUp() method of base class or super class.
    #     super().setUp()
    @pytest.mark.parametrize('caller,application, summary, description', read_data("Password Reset"))
    def test_password_reset_module_end_user(self, caller, application, summary, description):
        print("inside")
        self.driver.get("https://supporttest.condenastint.com/sp")
        time.sleep(3)
        login_cred_obj = LoginCred(self.driver)
        login_cred_obj.login_cred()
        time.sleep(40)
        self.password_reset_module_end_use_obj = PasswordResetModuleEndUser(self.driver)
        self.password_reset_module_end_use_obj.fill_password_reset_fields_end_user(caller, application, summary, description)
