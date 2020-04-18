import pytest
from .pages.product_page import ProductPage

main_url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


@pytest.mark.parametrize('link', [main_url + "?promo=offer0",
                                  main_url + "?promo=offer1",
                                  main_url + "?promo=offer2",
                                  main_url + "?promo=offer3",
                                  main_url + "?promo=offer4",
                                  main_url + "?promo=offer5",
                                  main_url + "?promo=offer6",
                                  pytest.param(main_url + "?promo=offer7", marks=pytest.mark.xfail),
                                  main_url + "?promo=offer8",
                                  main_url + "?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.add_to_basket_page()
    page.solve_quiz_and_get_code()
    page.should_be_success_added_page()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, main_url)
    page.open()
    page.add_to_basket_page()
    page.is_result_messages_not_present()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, main_url)
    page.open()
    page.is_result_messages_not_present()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, main_url)
    page.open()
    page.add_to_basket_page()
    page.is_result_messages_disappeared()
