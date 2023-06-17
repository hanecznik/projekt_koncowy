from selenium.webdriver.common.by import By

from Helpers.selectors import Selectors
from Helpers.test_data import TestData
from PageObjects.project_page_base import ProjectPageBase


class RegisterPage(ProjectPageBase):
    def register_account(self, recipent_name, recipent_email,password):
        recipent_extracted_name = recipent_name.split()
        # tworzenie nowego konta
        self.enter_txt(Selectors.RegisterPage.first_name, recipent_extracted_name[0])
        self.enter_txt(Selectors.RegisterPage.last_name, recipent_extracted_name[1])
        self.enter_txt(Selectors.RegisterPage.email, recipent_email)
        self.enter_txt(Selectors.RegisterPage.password, password)
        self.click_on_element((By.XPATH,
                       "//div[@class='sc-4mwtey-0 cHXQmZ sc-1jh87d2-7 daNAca']//div[@size='24']"), 360)
        self.click_on_element((By.XPATH, "//span[@class='sc-6i4pc6-2 gIXjlD']"), 360)
        return self

    def click_on_logo_and_goto_main_page(self):
        self.click_on_element(Selectors.MainPage.logo, 360)
        from PageObjects.main_page import MainPage
        main_page = MainPage(self.driver, self.base_url)
        return main_page

    def verify_validation_message_for_existing_account(self):
        occupied_email = self.find_element(Selectors.RegisterPage.email_validator).text
        assert occupied_email == TestData.occupied_email
        return self
