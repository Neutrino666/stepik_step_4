from pages.login_page import LoginPage
link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    page = LoginPage(browser, link)
    page.should_be_login_page()