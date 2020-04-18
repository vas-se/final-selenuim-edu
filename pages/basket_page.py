from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty(self):
        self.no_items_in_basket()
        self.message_no_items_is_present()

    def no_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORM)

    def message_no_items_is_present(self):
        assert self.is_element_present(*BasketPageLocators.NO_ITEMS_CONTENT)
