import unittest
from selenium import webdriver
from TestCase.BaseTestCase import TestBaseTestCase
from Pages.IncidentEndUser import IncidentEndUser


class TestIncidentEndUser(TestBaseTestCase):

    def setUp(self):
        super().setUp()

    def test_incident_page_end_user(self):
        print("inside")
        self.incident_end_use_obj = IncidentEndUser(self.driver)
        self.incident_end_use_obj.fill_incident_end_user_form()

    def tearDown(self):
        super().tearDown()
        # To do the cleanup after test has executed.@




