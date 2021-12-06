from Pages.DAMEnhancementRequestEndUser import DAMEnhancementRequestModuleEndUser
from TestCases.test_base import BaseTest
from Config.login_cred import LoginCred
import time





class TestDAMEnhancementRequestModuleEndUser(BaseTest):

    # def setUp(self):
    #     # to call the setUp() method of base class or super class.
    #     super().setUp()

    def test_password_reset_module_end_user(self):
        print("inside")
        self.driver.get("https://supporttest.condenastint.com/sp")
        time.sleep(3)
        login_cred_obj = LoginCred(self.driver)
        login_cred_obj.login_cred()
        time.sleep(40)
        self.ask_a_question_module_end_use_obj = DAMEnhancementRequestModuleEndUser(self.driver)
        self.ask_a_question_module_end_use_obj.fill_dam_enhancement_request_end_user()
