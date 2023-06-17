from time import sleep

from Helpers.selectors import Selectors
from PageObjects.project_page_base import ProjectPageBase


# TODO: Investigate all sleeps
class LoginPage(ProjectPageBase):
    def goto_register_account(self):
        # TODO:remove it in future
        sleep(5)
        self.click_on_element(Selectors.LoginPage.register_account, 360)
        from PageObjects.register_page import RegisterPage
        register_page = RegisterPage(self.driver, self.base_url)
        return register_page

    def login(self, user, password):
        # TODO: remove it in future
        sleep(5)
        self.enter_txt(Selectors.LoginPage.login, user)
        sleep(5)
        self.enter_txt(Selectors.LoginPage.password, password)
        self.click_on_element(Selectors.LoginPage.element_login, 360)
        from PageObjects.main_page import MainPage
        main_page = MainPage(self.driver, self.base_url)
        return main_page

    def login_and_goto_shipment(self):
        # TODO: remove it in future
        self.click_on_element(Selectors.LoginPage.btn_login, 360)
        sleep(5)
        self.enter_txt(Selectors.LoginPage.login, "testowanie.strony.2023@gmail.com")
        sleep(5)
        self.enter_txt(Selectors.LoginPage.password2, "12345678")
        self.click_on_element(Selectors.LoginPage.element_login, 360)
        self.click_on_element(Selectors.BasketPage.btn_pickup, 360)
        from PageObjects.order_page import OrderPage
        shipment_page = OrderPage(self.driver, self.base_url)
        return shipment_page
