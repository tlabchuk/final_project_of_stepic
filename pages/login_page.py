from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        mail = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTRATION)
        password1 = self.browser.find_element(*LoginPageLocators.PASSWORD1_REGISTRATION)
        password2 = self.browser.find_element(*LoginPageLocators.PASSWORD2_REGISTRATION)
        mail.send_keys(email)
        password1.send_keys(password)
        password2.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION)
        button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert url[0:37] == LoginPageLocators.LOGIN_URL[0:37] and url[-16:] == LoginPageLocators.LOGIN_URL[-16:], f"Url don't correct, {url} should be {LoginPageLocators.LOGIN_URL}"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not exist"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not exist"

