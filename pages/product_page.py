from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket_page(self):
        login_link = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        login_link.click()

    def should_be_product_page(self):
        self.should_be_catalogue_url()
        self.should_be_add_to_basket_button()
        self.should_be_product_name()
        self.should_be_product_price()

    def should_be_success_added_page(self):
        self.should_be_product_name()
        self.should_be_product_price()
        self.should_be_product_name_in_messages()
        self.should_be_product_price_in_messages()
        self.should_be_same_product()
        self.should_be_same_price()

    def should_be_catalogue_url(self):
        assert ProductPageLocators.CATALOGUE_STRING in self.browser.current_url, "Product page is not correct"

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not presented"

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Price is not presented"

    def should_be_product_name_in_messages(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE), "Product name is not presented"

    def should_be_product_price_in_messages(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE), "Price is not presented"

    def should_be_same_product(self):
        name_on_page = self.find_element(*ProductPageLocators.PRODUCT_NAME)
        name_in_result = self.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE)
        assert name_on_page.text == name_in_result.text, \
            f"Product names are not matched, got: {name_in_result.text}, expected {name_on_page.text}"

    def should_be_same_price(self):
        price_on_page = self.find_element(*ProductPageLocators.PRODUCT_PRICE)
        price_in_result = self.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE)
        assert price_on_page.text == price_in_result.text, \
            f"Product prices are not matched, got: {price_in_result.text}, expected {price_on_page.text}"
