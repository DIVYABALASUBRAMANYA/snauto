import pytest
from Pages.AccessModuleEndUser import AccessModuleEndUser
from TestCases.test_base import BaseTest
from Config.login_cred import LoginCred
import time
from Config.excelfunctions import read_data

"""PASSED"""


class TestAccessModuleEndUser(BaseTest):

    # def setUp(self):
    #     # to call the setUp() method of base class or super class.
    #     super().setUp()

    @pytest.mark.parametrize('application_required,summary, description', read_data("Access"))
    def test_access_module_end_user(self, application_required, summary, description):
        self.driver.get("https://supporttest.condenastint.com/sp")
        time.sleep(3)
        login_cred_obj = LoginCred(self.driver)
        login_cred_obj.login_cred()
        time.sleep(40)
        self.access_module_end_use_obj = AccessModuleEndUser(self.driver)
        self.access_module_end_use_obj.fill_access_module_end_user(application_required, summary, description)
