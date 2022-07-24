import time

from .base_page import BasePage
from .locators import MainPageLocators, ProductPageLocators


class ProductPage(BasePage):
    product_price = None
    product_name = None

    def should_be_product_to_basket(self):
        self.product_price = self.browser.find_element(*MainPageLocators.TXT_PRODUCT_PRICE).text
        self.product_name = self.browser.find_element(*MainPageLocators.TXT_PRODUCT_NAME).text
        self.add_to_basket()
        self.should_be_price()
        self.should_be_product()

    def add_to_basket(self):
        self.browser.find_element(*MainPageLocators.BTN_ADD_TO_BASKET).click()
        self.solve_quiz_and_get_code()

    def should_be_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.TXT_PRODUCT_PRICE).text
        assert self.product_price == product_price,\
            f"Цена на главной странице {self.product_name}: {self.product_price} " \
            f"не совпадает с ценой товара в коризне: {product_price}"

    def should_be_product(self):
        product_name = self.browser.find_element(*ProductPageLocators.TXT_PRODUCT_NAME).text
        assert product_name == self.product_name, \
            f"Название товара на главной странице: {self.product_name} " \
            f"не совпадает с товаром в коризне: {product_name}"
