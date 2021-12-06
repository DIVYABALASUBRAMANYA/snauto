"""

PEN DRIVE end user test case
Author : Divya B

"""

from Pages.PenDrive import PenDriveRequestModuleEndUser
from TestCases.test_base import BaseTest
import time
from Config.login_cred import LoginCred


class TestPenDriveModuleEndUser(BaseTest):

    # def setUp(self):
    #     # to call the setUp() method of base class or super class.
    #     super().setUp()

    def test_pen_drive_end_user(self):
        print("inside")
        self.driver.get("https://supporttest.condenastint.com/sp")
        time.sleep(3)
        login_cred_obj = LoginCred(self.driver)
        login_cred_obj.login_cred()
        time.sleep(40)
        self.pen_drive_module_end_user_obj = PenDriveRequestModuleEndUser(self.driver)
        self.pen_drive_module_end_user_obj.fill_pen_drive_request_module_end_user()

""" Passed """