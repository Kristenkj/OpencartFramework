from selenium.webdriver.common.by import By


class CamerasPage:
    def __init__(self, driver):
        self.driver = driver

    camera_page_title = (By.XPATH, "//h2[text()='Cameras']")
    product_compare_link = (By.XPATH, "//a[@id='compare-total']")
    grid_view_button = (By.XPATH, "//button[@id= 'grid-view']")
    list_view_button = (By.XPATH, "//button[@id= 'list-view']")

    #house_img_selector = (By.XPATH, "//a[@id="product-category"]/ul/li[1]/a")

    def get_camera_page_title(self):
        return self.driver.find_elements(*CamerasPage.camera_page_title)

    def get_compare_product_link(self):
        return self.driver.find_elements(*CamerasPage.product_compare_link)

    def get_grid_view(self):
        return self.driver.find_element(*CamerasPage.grid_view_button)

    def get_list_view(self):
        return self.driver.find_element(*CamerasPage.list_view_button)

    def change_view_to_grid_view(self):
        self.get_grid_view().click()
        grid_view = CamerasPage(self.driver)
        return grid_view
