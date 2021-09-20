import unittest
from selenium import webdriver
from TestCase.BaseTestCase import TestBaseTestCase
from Pages.IncidentEndUser import IncidentEndUser


class TestIncidentEndUser(TestBaseTestCase):

    def setUp(self):
        # to call the setUp() method of base class or super class.
        super().setUp()

    def test_incident_page_end_user(self):
        print("inside")
        self.incident_end_use_obj = IncidentEndUser(self.driver)
        self.incident_end_use_obj.fill_incident_end_user_form()

        # self.test_obj = IncidentEndUser(self.driver)
        # self.test_obj.test_fun()

    def tearDown(self):
        # To do the cleanup after test has executed.@
        super().tearDown()



