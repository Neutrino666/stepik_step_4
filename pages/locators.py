from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.ID, "login_link")
    BTN_ADD_TO_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
    TXT_PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    TXT_PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators:
    TXT_PRODUCT_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')
    TXT_PRODUCT_NAME = (By.XPATH, "(//div[@class='alertinner '])[1]/strong")
