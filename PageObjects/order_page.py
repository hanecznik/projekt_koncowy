from time import sleep

from Helpers.selectors import Selectors
from Helpers.test_data import TestData
from PageObjects.project_page_base import ProjectPageBase


# TODO: Inviestigate all sleeps
class OrderPage(ProjectPageBase):
    def select_pickup_location(self):
        try:
            self.click_on_element(Selectors.OrderPage.btn_pickup_location, 20)
            sleep(2)
            self.click_on_element(Selectors.OrderPage.btn_bielany, 20)
            sleep(2)
            store = self.find_element(Selectors.OrderPage.element_bielany).text
            sleep(2)
            assert store == TestData.order_store_name
        except:
            self.click_on_element(Selectors.OrderPage.btn_change_pickup_location, 20)
            sleep(2)
            self.click_on_element(Selectors.OrderPage.element_selected, 20)
            store = self.find_element(Selectors.OrderPage.element_bielany, 10).text
            sleep(2)
            assert store == TestData.x_kom_bielany

        return self

    def enter_customer_data_and_select_payment_method(self, recipent_name, recipent_phone_number, valid_recipent_email):
        try:
            self.enter_txt(Selectors.OrderPage.txt_recipent_name, recipent_name)
            sleep(2)
            self.enter_txt(Selectors.OrderPage.txt_recipent_phone_number, recipent_phone_number)
            sleep(2)
            self.enter_txt(Selectors.OrderPage.txt_recipent_email, valid_recipent_email)
        except:
            self.click_on_element(Selectors.OrderPage.btn_change_recipent, 20)
            sleep(2)
            self.click_on_element(Selectors.OrderPage.btn_new_recipent, 20)
            self.enter_txt(Selectors.OrderPage.txt_recipent_name, recipent_name)
            self.enter_txt(Selectors.OrderPage.txt_phone_number, recipent_phone_number)
            self.enter_txt(Selectors.OrderPage.txt_email, valid_recipent_email)
            sleep(2)
            self.click_on_element(Selectors.OrderPage.btn_save, 20)
            sleep(2)
            self.click_on_element(Selectors.OrderPage.btn_accept, 20)
        # płatność
        self.click_on_element(Selectors.OrderPage.element_in_pickup_location, 20)
        return self

    def verify_order_summary(self, surname, email, phone):
        # przejdź do podsumowania
        self.click_on_element(Selectors.OrderPage.btn_goto_summary, 360)
        name_surname = self.find_element(Selectors.OrderPage.txt_name_surname).text
        assert name_surname == surname
        email_info = self.find_element(Selectors.OrderPage.txt_email_info, 10).text
        assert email_info == f"e-mail: {email}"
        phone_number_info = self.find_element(Selectors.OrderPage.txt_phone_info, 10).text
        phone_number_info = ''.join(filter(lambda x: x.isdigit(), phone_number_info))
        assert phone_number_info == phone
        self.click_on_element(Selectors.OrderPage.btn_buy_and_pay, 360)
        # potwordzenie złożenia zamówienia i przyjęcia do realizacji
        order = self.find_element(Selectors.OrderPage.element_order_status, 10).text
        assert order == TestData.order_confirmation
        return self
