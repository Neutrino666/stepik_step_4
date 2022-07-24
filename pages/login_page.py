from .base_page import BasePage
from .main_page import MainPage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        # page = MainPage(self.browser, self.url)
        # page.open()
        # page.go_to_login_page()
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        txt = "login"
        assert txt in self.browser.current_url,\
            f"{txt} в url: {self.url} не найден"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            f"Локатор {LoginPageLocators.LOGIN_FORM} не найден"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            f"Локатор {LoginPageLocators.REGISTER_FORM} не найден"
