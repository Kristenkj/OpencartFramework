import time

import allure
import pytest
from tests.pageObjects.CamerasPage import CamerasPage
from tests.pageObjects.HomePage import HomePage
from tests.utils.BaseClass import BaseClass


class TestActions(BaseClass):

    def test_navigate_to_cameras_tab(self):
        home_page = HomePage(self.driver)
        home_page.open_cameras_page_from_hp()
        time.sleep(5)

    @allure.description("Verify navigation to the camera page from the home page and select change the product view")
    def test_change_product_view(self):
        home_page = HomePage(self.driver)
        camera_page = home_page.open_cameras_page_from_hp()
        camera_page.change_view_to_grid_view()
        time.sleep(5)


