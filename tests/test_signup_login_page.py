import pytest
from ..pages.base_page import BasePage
from ..pages.signup_login_page import SignupLoginPage
from ..pages.main_page import MainPage
from ..settings import sets
import random


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.signup_login_logout
class TestSignupLoginLogautPage:

    def setup_method(self):
        hash_name = "%032x" % random.getrandbits(128)
        self.email_for_signup = f"{hash_name}@mail.com"
        self.password_for_signup = "123654789"
        self.name_for_signup = "Jaylen Blackwell"
        self.phone_for_signup = "0999999999"
        self.postcode_for_signup = "03190"
        self.address_for_signup = "вул. Миколи Василенка"

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.PROD_SERVER)
        page.open()

    def test_signup_page(self, browser):
        self.link_to_cabinet = browser.current_url
        page = SignupLoginPage(browser, self.link_to_cabinet)
        page.click_button_signup_login()
        page.explicit_wait(2)
        page.button_login()
        page.press_button_login()
        page.click_signup()
        page.explicit_wait(2)
        page.is_h1_signup()
        page.input_email_password(self.email_for_signup, self.password_for_signup, self.name_for_signup,
                                  self.phone_for_signup, self.postcode_for_signup, self.address_for_signup)
        page.press_button_signup()
        page.is_alert_success()

    def test_login_page(self, browser):
        self.link_to_cabinet = browser.current_url
        page = SignupLoginPage(browser, self.link_to_cabinet)
        page.click_button_signup_login()
        page.explicit_wait(2)
        page.input_email_password(sets.TEST_EMAIL, sets.PASSWORD, sets.NAME, sets.PHONE, sets.POSTCODE, sets.ADDRESS)
        page.press_button_login()
        page.is_alert_success()
        page.is_button_logout_in_header()

    def test_logout_page(self, browser):
        self.link_to_cabinet = browser.current_url
        page = SignupLoginPage(browser, self.link_to_cabinet)
        page.press_button_logout()
        page.explicit_wait(2)
        page = MainPage(browser, self.link_to_cabinet)
        page.is_button_user()
