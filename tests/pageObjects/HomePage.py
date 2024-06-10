from selenium.webdriver.common.by import By

from tests.pageObjects.CamerasPage import CamerasPage


class HomePage:
    #constructor of the page class
    def __init__(self, driver):
        self.driver = driver

    #Page Locators

    carousel = (By.ID, "carousel0")
    home_link = (By.ID, "logo")
    desktops_tab = (By.CSS_SELECTOR, "a[href*='Desktops']")
    laptops_and_notebooks_tab = (By.CSS_SELECTOR, "a[href*='Laptops & Notebooks']")
    components_tab = (By.CSS_SELECTOR, "a[href*='Components']")
    tablets_tab = (By.CSS_SELECTOR, "a[href*='Tablets']")
    software_tab = (By.CSS_SELECTOR, "a[href*='Software']")
    phones_and_pdas_tab = (By.CSS_SELECTOR, "a[href*='Phones & PDAs']")
    cameras_tab = (By.XPATH, "//a[text()='Cameras']")
    mp3_players_tab = (By.CSS_SELECTOR, "a[href*='MP3 Players']")
    shopping_cart_dropdown_button = (By.ID, "cart")
    currency_selector = (By.CSS_SELECTOR, "span[class*='Currency']")

    #Page Actions
    def get_carousel(self):
        return self.driver.find_element(*HomePage.carousel)

    def get_home_link(self):
        return self.driver.find_element(*HomePage.home_link)

    def get_desktops_tab(self):
        return self.driver.find_element(*HomePage.desktops_tab)

    def get_laptops_and_notebooks(self):
        return self.driver.find_element(*HomePage.laptops_and_notebooks_tab)

    def get_components_tab(self):
        return self.driver.find_element(*HomePage.components_tab)

    def get_tablets_tab(self):
        return self.driver.find_element(*HomePage.tablets_tab)

    def get_software_tab(self):
        return self.driver.find_element(*HomePage.software_tab)

    def get_phones_and_pdas_tab(self):
        return self.driver.find_element(*HomePage.phones_and_pdas_tab)

    def get_cameras_page(self):
        return self.driver.find_element(*HomePage.cameras_tab)

    def get_mp3_players_tab(self):
        return self.driver.find_element(*HomePage.mp3_players_tab)

    def get_shopping_cart_dropdown_button(self):
        return self.driver.find_element(*HomePage.shopping_cart_dropdown_button)

    def get_currency_selector(self):
        return self.driver.find_element(*HomePage.currency_selector)

    #Bundled Actions
    def open_cameras_page_from_hp(self):
        self.get_cameras_page().click()
        cameras_page = CamerasPage(self.driver)
        return cameras_page
