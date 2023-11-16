import pytest
from ..pages.base_page import BasePage
from ..pages.main_page import MainPage
import random
from ..settings import sets


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.main_page
class TestMainPage:

    def setup_method(self):
        hash_name = "%032x" % random.getrandbits(128)
        self.email_for_subscribe = f"{hash_name}@mail.com"

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.PROD_SERVER)
        page.open()

    def test_main_page_header(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_button_register()
        page.is_button_autorization()
        page.is_button_wishlist()
        page.is_button_ukrainian()
        page.is_button_russian()
        page.is_button_facebook()
        page.is_button_youtube()
        page.is_button_instagram()
        page.is_element_logo()
        page.is_search_input_field()
        page.is_search_button()
        page.is_email_button()
        page.is_cart_button()

    def test_main_page_content(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_about_us()
        page.is_delivery_and_payment()
        page.is_returns_and_warranty()
        page.is_contacts()
        page.is_specials()
        page.is_info_block_delivery_across_ukraine()
        page.is_info_block_free_shipping()
        page.is_info_block_convenient_payment()
        page.is_info_block_guarantee()
        page.is_section_categories()
        page.is_section_selection_of_goods()
        page.is_button_recommended_products()
        page.is_button_popular_products()
        page.is_button_novelty()
        page.is_section_offer_of_the_day()
        page.is_section_action()
        page.is_section_latest_news()
        page.is_section_carousel_of_news()

    def test_main_page_footer(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_button_subscribe()
        page.is_elem_footer()
        page.is_elem_footer_payment_mastercard()
        page.is_elem_footer_payment_visa()
        page.is_elem_footer_payment_apple_pay()
        page.is_elem_footer_payment_google_pay()

