""" Workday europe support end user test case"""

from Pages.EditorialSystemEndUser import EditorialSystemModuleEndUser
from TestCases.test_base import BaseTest
import time
from Config.login_cred import LoginCred

"""  PASSED  """


class TestEditorialSystemEndUser(BaseTest):

    # def setUp(self):
    #     # to call the setUp() method of base class or super class.
    #     super().setUp()

    def test_editorial_system_end_user(self):
        print("inside")
        self.driver.get("https://supporttest.condenastint.com/sp")
        time.sleep(3)
        login_cred_obj = LoginCred(self.driver)
        login_cred_obj.login_cred()
        time.sleep(40)
        self.editorial_system_end_user_obj = EditorialSystemModuleEndUser(self.driver)
        self.editorial_system_end_user_obj.fill_editorial_systems_module_end_user()