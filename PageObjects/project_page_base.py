from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ProjectPageBase:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def find_element(self, locator, timeout_sec=60):
        return WebDriverWait(self.driver, timeout_sec).until(EC.presence_of_element_located(locator),
                                                             message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, timeout_sec=60):
        return WebDriverWait(self.driver, timeout_sec).until(EC.presence_of_all_elements_located(locator),
                                                             message=f"Can't find element by locator {locator}")

    def click_on_element(self, locator: object, timeout_sec: object) -> object:
        self.find_element(locator, timeout_sec).click()

    def navigate_to(self, url=''):
        url = self.base_url + url
        self.driver.get(url)
        self.driver.maximize_window()

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def enter_txt(self, locator, text):
        self.find_element(locator).send_keys(text)

    def clear_txt(self, locator):
        self.find_element(locator).clear()

    def wait_until_visibility_of_element_located(self, locator):
        WebDriverWait(self.driver, timeout=5).until(EC.presence_of_element_located(locator))

    def check_title(self, title):
        assert self.get_title() == title
        return self
