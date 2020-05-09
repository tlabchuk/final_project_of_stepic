from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    PRODUCT_URL = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_OF_BOOK = (By.CSS_SELECTOR, '.product_main > h1')
    NAME_OF_BOOK_IN_BASKET = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    PRICE_OF_BOOK = (By.CSS_SELECTOR, '.product_main > .price_color')
    PRICE_OF_BOOK_IN_BASKET = (By.CSS_SELECTOR, '.alertinner > p > strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")