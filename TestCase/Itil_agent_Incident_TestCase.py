import unittest
from selenium import webdriver
from TestCase.BaseTestCase import Test_Base_Test_Case
from Pages.ITILAgentIncident import IncidentItilAgent


class TestItilAgentIncident(Test_Base_Test_Case):

    def setUp(self):
        # to call the setUp() method of base class or super class.
        super().setUp()

    def test_incident_page_itil_agent(self):
        print("inside")

        self.incident_end_use_obj = IncidentItilAgent(self.driver)

        self.incident_end_use_obj.fill_itil_incident_form()
        # self.test_obj = IncidentEndUser(self.driver)
        # self.test_obj.test_fun()
    #
    # def switch_frame(self):
    #     self.driver.switch_to_frame("form-frame")

    def tearDown(self):
        # To do the cleanup after test has executed.@
        super().tearDown()

