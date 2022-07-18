from .base_page import BasePage
from selenium.webdriver.common.by import By


class Locators:
    LINK_LOGIN = (By.CSS_SELECTOR, "#login_link_invalid")
    LINK_LOGIN_VALID = (By.CSS_SELECTOR, "#login_link")


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*Locators.LINK_LOGIN_VALID)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*Locators.LINK_LOGIN),\
            "Login link is not presented"
        # self.browser.find_element(*Locators.LINK_LOGIN)
