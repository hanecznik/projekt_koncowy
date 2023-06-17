import time

from selenium.webdriver import ActionChains

from Helpers.selectors import Selectors
from Helpers.test_data import TestData
from PageObjects.login_page import LoginPage
from PageObjects.project_page_base import ProjectPageBase


# TODO: Investigate all sleeps
class MainPage(ProjectPageBase):
    @staticmethod
    def navigate(driver, url):
        page = MainPage(driver, url)
        page.navigate_to()
        page.click_on_element(Selectors.MainPage.btn_accept, 360)
        return page

    def find_product_by_name_and_validate(self, product_name):
        self.find_product(product_name)
        product_search = self.find_element(Selectors.MainPage.number_of_found_items).text
        time.sleep(2)
        total = ''.join(filter(lambda x: x.isdigit(), product_search))
        total = int(total)
        assert total > 0, TestData.something_went_wrong_message
        return self

    def find_product(self, product_name):
        time.sleep(5)
        self.enter_txt(Selectors.MainPage.txt_search, product_name)
        self.click_on_element(Selectors.MainPage.btn_search, 360)
        return self

    def show_only_available_product(self):
        self.click_on_element(Selectors.MainPage.chkbox_hide_unavailable, 360)
        return self

    def show_promotions(self):
        self.click_on_element(Selectors.MainPage.chkbox_promotions, 360)
        return self

    def order_products_by_cheapest(self):
        # TODO: remove this in future, investigate why element is interactable after this period
        time.sleep(5)
        self.click_on_element(Selectors.MainPage.price_menu, 360)
        time.sleep(5)
        self.click_on_element(Selectors.MainPage.price_menu_cheapest_item, 360)
        return self

    def find_random_product_and_validate(self):
        # szukanie po wpisaniu losowych znaków
        self.clear_txt(Selectors.MainPage.txt_search)
        self.find_product("@")
        random = self.find_element(Selectors.MainPage.not_found_message).text
        assert random == TestData.we_could_not_find_message
        return self

    def click_on_logo_and_check_title(self):
        # powrót przez logo na stronę główną
        self.find_element(Selectors.MainPage.logo).click()
        title = self.get_title()
        time.sleep(10)
        assert title == TestData.main_page_title

    def click_on_your_account(self):
        time.sleep(2)
        self.click_on_element(Selectors.MainPage.your_account_icon, 360)
        login_page = LoginPage(self.driver, self.base_url)
        return login_page

    def logout(self):
        time.sleep(10)
        action = ActionChains(self.driver)
        action.move_to_element(self.find_element(Selectors.MainPage.menu_dropdown))
        action.perform()
        self.click_on_element(Selectors.MainPage.menu_item_logout, 360)
        time.sleep(5)
        self.find_element(Selectors.MainPage.btn_login)
        assert self.get_title() == TestData.main_page_title
        return self

    def add_selected_product_to_basket(self):
        time.sleep(5)
        self.click_on_element(Selectors.MainPage.btn_add_selected_product_to_cart, 360)
        return self

    def go_to_basket(self):
        time.sleep(5)
        self.click_on_element(Selectors.MainPage.btn_go_to_cart, 360)
        from PageObjects.basket_page import BasketPage
        basket = BasketPage(self.driver, self.base_url)
        return basket
