import pytest
import time

from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage

product_url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
registration_url = "http://selenium1py.pythonanywhere.com/accounts/login/"


@pytest.mark.login
class TestLoginFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.link = product_url
        yield
        pass

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_be_login_link()


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, registration_url)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        page.register_new_user(email, "test_password")
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, product_url)
        page.open()
        page.is_result_messages_not_present()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, product_url+"?promo=offer1")
        page.open()
        page.should_be_product_page()
        page.add_to_basket_page()
        page.solve_quiz_and_get_code()
        page.should_be_success_added_page()


@pytest.mark.need_review
@pytest.mark.parametrize('link', [product_url + "?promo=offer0",
                                  product_url + "?promo=offer1",
                                  product_url + "?promo=offer2",
                                  product_url + "?promo=offer3",
                                  product_url + "?promo=offer4",
                                  product_url + "?promo=offer5",
                                  product_url + "?promo=offer6",
                                  pytest.param(product_url + "?promo=offer7", marks=pytest.mark.xfail),
                                  product_url + "?promo=offer8",
                                  product_url + "?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.add_to_basket_page()
    page.solve_quiz_and_get_code()
    page.should_be_success_added_page()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_url)
    page.open()
    page.add_to_basket_page()
    page.is_result_messages_not_present()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, product_url)
    page.open()
    page.is_result_messages_not_present()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_url)
    page.open()
    page.add_to_basket_page()
    page.is_result_messages_disappeared()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, product_url)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty()
