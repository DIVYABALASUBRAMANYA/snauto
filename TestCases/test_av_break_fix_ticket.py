"""Request module end user test case"""
from Pages.AVBreakFixTicket import AVBreakFixTicketModuleEndUser
from TestCases.test_base import BaseTest
from Config.login_cred import LoginCred
import time


class TestAVBreakFixTicketModuleEndUser(BaseTest):

    # def setUp(self):
    #     # to call the setUp() method of base class or super class.
    #     super().setUp()

    def test_av_break_fix_ticket_module_end_user(self):
        print("inside")
        self.driver.get("https://supporttest.condenastint.com/sp")
        time.sleep(3)
        login_cred_obj = LoginCred(self.driver)
        login_cred_obj.login_cred()
        time.sleep(40)
        self.av_break_fix_ticket_module_end_user_obj = AVBreakFixTicketModuleEndUser(self.driver)
        self.av_break_fix_ticket_module_end_user_obj.fill_av_break_fix_ticket_module_end_user()
