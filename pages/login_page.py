from .base_page import BasePage
from .main_page import MainPage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        page = MainPage(self.browser, self.url)
        page.open()
        page.go_to_login_page()
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        start_link = 'http://selenium1py.pythonanywhere.com/'
        end_link = '/accounts/login/'
        assert \
            self.browser.current_url.startswith(start_link) and\
            self.browser.current_url.endswith(end_link)

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM)
