"""This will be he global fixture for all test cases"""
import pytest
from selenium import webdriver
from Pages.BasePage import BasePage


@pytest.fixture(params = ["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path="/Users/dbalasub/PycharmProjects/pythonProject/Driver/chromedriver 7")
        request.cls.driver = web_driver
    yield
    web_driver.close()
