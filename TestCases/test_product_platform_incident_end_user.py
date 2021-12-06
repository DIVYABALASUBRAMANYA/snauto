""" Product platform Incident test case """


from TestCases.test_base import BaseTest
from Pages.ProductPlatformIncidentEndUser import ProductPlatformIncidentEndUser


class TestProductPlatformIncidentEndUser(BaseTest):

    def test_incident_page_end_user(self):
        print("inside")
        self.product_platform_incident_end_use_obj = ProductPlatformIncidentEndUser(self.driver)
        self.product_platform_incident_end_use_obj.fill_product_platform_incident_end_user()
