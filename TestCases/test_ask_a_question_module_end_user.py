"""Request module end user test case"""
from Pages.AskAQuestionModuleEndUser import AskAQuestionModuleEndUser
from TestCases.test_base import BaseTest
from Config.login_cred import LoginCred
import time
import pytest
from Config.excelfunctions import read_data


"""Passed"""


class TestAskAQuestionModuleEndUser(BaseTest):


    # def setUp(self):
    #     # to call the setUp() method of base class or super class.
    #     super().setUp()
    @pytest.mark.smoke
    @pytest.mark.parametrize('office,summary, description', read_data("Ask A Question"))
    def test_ask_a_question_module_end_user(self, office, summary, description):
    # def test_ask_a_question_module_end_user(self,):
        print("inside")
        self.driver.get("https://supporttest.condenastint.com/sp")
        time.sleep(3)


        login_cred_obj = LoginCred(self.driver)
        login_cred_obj.login_cred()
        time.sleep(40)
        self.ask_a_question_module_end_use_obj = AskAQuestionModuleEndUser(self.driver)
        self.ask_a_question_module_end_use_obj.fill_ask_a_question_module_fields_end_user(office, summary, description)



