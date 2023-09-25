import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from Helpers.test_data import TestData
from PageObjects.main_page import MainPage


@pytest.fixture
def browser():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield browser
    browser.close()
    browser.quit()


def test_xkom_searching_products(browser):
    MainPage.navigate(browser, TestData.xkom_url) \
        .find_product_by_name_and_validate(TestData.product_philips) \
        .find_random_product_and_validate() \
        .click_on_logo_and_check_title()


def test_xkom_create_login_account(browser):
    MainPage.navigate(browser, TestData.xkom_url) \
        .click_on_your_account() \
        .goto_register_account() \
        .register_account(TestData.recipent_name, TestData.valid_user_email, TestData.valid_user_password) \
        .click_on_logo_and_goto_main_page() \
        .click_on_your_account() \
        .goto_register_account() \
        .register_account(TestData.recipent_name, TestData.valid_user_email, TestData.valid_user_password) \
        .verify_validation_message_for_existing_account() \
        .click_on_logo_and_goto_main_page() \
        .click_on_your_account() \
        .login(TestData.valid_user_email, TestData.valid_user_password) \
        .logout()


def test_xkom_buying_products(browser):
    MainPage.navigate(browser, TestData.xkom_url) \
        .find_product(TestData.iphone) \
        .show_only_available_product() \
        .show_promotions() \
        .order_products_by_cheapest() \
        .add_selected_product_to_basket() \
        .go_to_basket() \
        .click_favourites() \
        .add_to_favourites_list() \
        .check_favourites_list(TestData.ringke_silicone_pink) \
        .click_on_basket_and_goto_order() \
        .login_and_goto_shipment() \
        .select_pickup_location() \
        .enter_customer_data_and_select_payment_method(TestData.recipent_name, TestData.recipent_phone_number, TestData.valid_user_email) \
        .verify_order_summary(TestData.recipent_name, TestData.valid_user_email, TestData.recipent_phone_number)
