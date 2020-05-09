from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_button.click()
        self.solve_quiz_and_get_code()

    def check_name_of_book(self):
        name_of_book = self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK).text
        name_of_book_in_basket = self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK_IN_BASKET).text
        assert name_of_book == name_of_book_in_basket, f'Name of book must be {name_of_book}, not {name_of_book_in_basket}'

    def check_price_of_book(self):
        price_of_book = self.browser.find_element(*ProductPageLocators.PRICE_OF_BOOK).text
        price_of_book_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_OF_BOOK_IN_BASKET).text
        assert price_of_book == price_of_book_in_basket, f'Name of book must be {price_of_book}, not {price_of_book_in_basket}'
