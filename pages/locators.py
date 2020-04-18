from selenium.webdriver.common.by import By


class BasePageLocators:
    GOTO_BASKET = (By.CSS_SELECTOR, ".btn[href='/en-gb/basket/']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_STRING = "/login"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FROM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_CONFIRMATION_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    CATALOGUE_STRING = "/catalogue"
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "#messages :nth-child(1) .alertinner strong")
    PRODUCT_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, "#messages :nth-child(3) .alertinner strong")
    RESULT_MESSAGE = (By.CSS_SELECTOR, ".alert-success")


class BasketPageLocators:
    NO_ITEMS_CONTENT = (By.CSS_SELECTOR, "#content_inner>p")
    BASKET_FORM = (By.CSS_SELECTOR, "#basket_formset")
