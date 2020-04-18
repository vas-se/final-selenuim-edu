from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self, email, password):
        email_field = self.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        password_field = self.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)
        confirm_field = self.find_element(*LoginPageLocators.PASSWORD_CONFIRMATION_FIELD)
        confirm_field.send_keys(password)
        submit = self.find_element(*LoginPageLocators.REGISTER_BUTTON)
        submit.click()

    def should_be_login_url(self):
        assert LoginPageLocators.LOGIN_STRING in self.browser.current_url, "Login link is not valid"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FROM), "Register form is not presented"
