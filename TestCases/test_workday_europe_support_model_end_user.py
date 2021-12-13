"""
Workday europe support end user test case
Author: Divya B, CNTL

"""
from Pages.WorkDayEuropeSupportModelEndUser import WorkDayEuropeSupportModelEndUser
from TestCases.test_base import BaseTest
import time
from Config.login_cred import LoginCred
from Config.config import TestData
import pytest
from Config.excelfunctions import read_data

"""  PASSED  """


class TestWorkDayEuropeSupportModel(BaseTest):

    # def setUp(self):
    #     # to call the setUp() method of base class or super class.
    #     super().setUp()

    @pytest.mark.parametrize('issue_inquiry,description', read_data("Workday Europe Support Model"))
    def test_request_module_end_user(self, issue_inquiry, description):
        print("inside")
        self.driver.get(TestData.SN_END_USER_PORTAL)
        time.sleep(3)
        login_cred_obj = LoginCred(self.driver)
        login_cred_obj.login_cred()
        time.sleep(40)
        self.work_day_europe_support_model_end_user_obj = WorkDayEuropeSupportModelEndUser(self.driver)
        self.work_day_europe_support_model_end_user_obj.fill_workday_europe_support_model_end_user(issue_inquiry, description)
