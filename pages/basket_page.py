from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_product(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCT), \
            "Products is the basket, but should not be"

    def should_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), \
            "Basket is not empty, but should not be"
