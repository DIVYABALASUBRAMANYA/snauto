from Pages.DAMEnhancementRequestEndUser import DAMEnhancementRequestModuleEndUser
from TestCases.test_base import BaseTest
from Config.login_cred import LoginCred
import time
from Config.excelfunctions import read_data
import pytest

class TestDAMEnhancementRequestModuleEndUser(BaseTest):

    # def setUp(self):
    #     # to call the setUp() method of base class or super class.
    #     super().setUp()

    @pytest.mark.parametrize('requested_for,office,urgency, DAM_Platform, editorial_role,Brand,Summary, Business_justification, use_case', read_data("DAM Enhancement Request"))
    def test_password_reset_module_end_user(self, requested_for, office, urgency, DAM_Platform,editorial_role, Brand, Summary, Business_justification, use_case):
        print("inside")
        self.driver.get("https://supporttest.condenastint.com/sp")
        time.sleep(3)
        login_cred_obj = LoginCred(self.driver)
        login_cred_obj.login_cred()
        time.sleep(40)
        self.ask_a_question_module_end_use_obj = DAMEnhancementRequestModuleEndUser(self.driver)
        self.ask_a_question_module_end_use_obj.fill_dam_enhancement_request_end_user(requested_for, office, urgency, DAM_Platform,editorial_role, Brand, Summary, Business_justification, use_case)

