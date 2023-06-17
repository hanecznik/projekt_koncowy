from time import sleep, time

from selenium.webdriver import ActionChains

from Helpers.selectors import Selectors
from Helpers.test_data import TestData
from PageObjects.project_page_base import ProjectPageBase


# TODO: Investigate all sleeps
class BasketPage(ProjectPageBase):
    def click_favourites(self):
        sleep(5)
        self.click_on_element(Selectors.BasketPage.btn_favourites, 360)
        return self

    def add_to_favourites_list(self):
        sleep(5)
        self.click_on_element(Selectors.BasketPage.btn_add_list, 360)
        return self

    def check_favourites_list(self,favourities):
        sleep(10)
        self.click_on_element(Selectors.BasketPage.btn_user_lists, 360)
        sleep(10)
        assert self.get_title() == TestData.shopping_list_title
        favourities_list = self.find_element(Selectors.BasketPage.favourites_lists).get_attribute('title')
        assert favourities_list == favourities
        return self

    def click_on_basket_and_goto_order(self):
        sleep(3)
        self.click_on_element(Selectors.BasketPage.btn_basket, 360)
        sleep(3)
        action = ActionChains(self.driver)
        action.move_to_element(self.find_element(Selectors.MainPage.logo, 360))
        action.perform()
        self.click_on_element(Selectors.BasketPage.btn_shipment, 360)
        from PageObjects.login_page import LoginPage
        login_page = LoginPage(self.driver, self.base_url)
        return login_page
