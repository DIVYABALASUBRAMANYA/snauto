""" Movers Request end user test case"""

from Pages.MoversRequestEndUser import MoversRequestEndUser
from TestCases.test_base import BaseTest
import time
from Config.login_cred import LoginCred

"""  PASSED  """


class TestMoversRequestEndUser(BaseTest):

    # def setUp(self):
    #     # to call the setUp() method of base class or super class.
    #     super().setUp()

    def test_printer_issue_end_user(self):
        print("inside")
        self.driver.get("https://supporttest.condenastint.com/sp")
        time.sleep(3)
        login_cred_obj = LoginCred(self.driver)
        login_cred_obj.login_cred()
        time.sleep(40)
        self.movers_request_end_user_obj = MoversRequestEndUser(self.driver)
        self.movers_request_end_user_obj.fill_movers_request_end_user()
