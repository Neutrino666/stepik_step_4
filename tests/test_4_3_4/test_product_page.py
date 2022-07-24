import time
from pages.product_page import ProductPage
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"


@pytest.mark.parametrize('num', range(10))
def test_guest_can_add_product_to_basket(browser, num):
    page = ProductPage(browser, f"{link}{str(num)}")
    page.open()
    page.should_be_product_to_basket()
