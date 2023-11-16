from ..pages import base_page, locators
import inspect

class MainPage(base_page.BasePage):
    def is_button_register(self):
        assert self.hover_action(*locators.BasePageLocators.USER_INFO), \
            "The element is not present or intractable"
        assert self.is_element_present(*locators.BasePageLocators.REGISTER), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_autorization(self):
        assert self.hover_action(*locators.BasePageLocators.USER_INFO), \
            "The element is not present or intractable"
        assert self.is_element_present(*locators.BasePageLocators.AUTHORIZATION), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_wishlist(self):
        assert self.hover_action(*locators.BasePageLocators.USER_INFO), \
            "The element is not present or intractable"
        assert self.is_element_present(*locators.BasePageLocators.WISHLIST), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_ukrainian(self):
        assert self.hover_action(*locators.BasePageLocators.LANGUAGE), \
            "The element is not present or intractable"
        assert self.is_element_present(*locators.BasePageLocators.UKRAINIAN), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_russian(self):
        assert self.hover_action(*locators.BasePageLocators.LANGUAGE), \
            "The element is not present or intractable"
        assert self.is_element_present(*locators.BasePageLocators.RUSSIAN), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_facebook(self):
        assert self.is_element_present(*locators.BasePageLocators.FACEBOOK), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_youtube(self):
        assert self.is_element_present(*locators.BasePageLocators.YOUTUBE), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_instagram(self):
        assert self.is_element_present(*locators.BasePageLocators.INSTAGRAM), \
            "The element logo is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_element_logo(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGO), \
            "The search input field is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_search_input_field(self):
        assert self.is_element_present(*locators.BasePageLocators.SEARCH), \
            "The search input field is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_search_button(self):
        assert self.is_element_present(*locators.BasePageLocators.SEARCH_BUTTON), \
            "The search button is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_email_button(self):
        assert self.is_element_present(*locators.BasePageLocators.CONTACT_INFO), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_cart_button(self):
        assert self.is_element_present(*locators.BasePageLocators.CART_SECTION), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_about_us(self):
        assert self.is_element_present(*locators.MainPageLocators.ABOUT_US), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_delivery_and_payment(self):
        assert self.is_element_present(*locators.MainPageLocators.DELIVERY_AND_PAYMENT), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_returns_and_warranty(self):
        assert self.is_element_present(*locators.MainPageLocators.RETURNS_AND_WARRANTY), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_contacts(self):
        assert self.is_element_present(*locators.MainPageLocators.CONTACTS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_specials(self):
        assert self.is_element_present(*locators.MainPageLocators.SPECIALS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_info_block_delivery_across_ukraine(self):
        assert self.is_element_present(*locators.MainPageLocators.DELIVERY_ACROSS_UKRAINE), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_info_block_free_shipping(self):
        assert self.is_element_present(*locators.MainPageLocators.FREE_SHIPPING), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_info_block_convenient_payment(self):
        assert self.is_element_present(*locators.MainPageLocators.CONVENIENT_PAYMENT), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_info_block_guarantee(self):
        assert self.is_element_present(*locators.MainPageLocators.GUARANTEE), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_section_categories(self):
        assert self.is_element_present(*locators.MainPageLocators.CATEGORIES), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_section_selection_of_goods(self):
        assert self.is_element_present(*locators.MainPageLocators.SELECTION_OF_GOODS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_recommended_products(self):
        assert self.is_element_present(*locators.MainPageLocators.RECOMMENDED_PRODUCTS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_popular_products(self):
        assert self.is_element_present(*locators.MainPageLocators.POPULAR_PRODUCTS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_novelty(self):
        assert self.is_element_present(*locators.MainPageLocators.NOVELTY), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_section_offer_of_the_day(self):
        assert self.is_element_present(*locators.MainPageLocators.OFFER_OF_THE_DAY), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_section_action(self):
        assert self.is_element_present(*locators.MainPageLocators.ACTION), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_section_latest_news(self):
        assert self.is_element_present(*locators.MainPageLocators.LATEST_NEWS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_section_carousel_of_news(self):
        assert self.is_element_present(*locators.MainPageLocators.CAROUSEL_OF_NEWS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_subscribe(self):
        assert self.is_element_present(*locators.BasePageLocators.SUBSCRIBE), \
            "The element subscribe is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_footer(self):
        assert self.is_element_present(*locators.BasePageLocators.FOOTER), \
            "The element footer logo is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_footer_payment_mastercard(self):
        assert self.is_element_present(*locators.BasePageLocators.MASTERCARD), \
            "The element mastercard is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_footer_payment_visa(self):
        assert self.is_element_present(*locators.BasePageLocators.VISA), \
            "The element visa is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_footer_payment_apple_pay(self):
        assert self.is_element_present(*locators.BasePageLocators.APPLE_PAY), \
            "The element apple pay is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_footer_payment_google_pay(self):
        assert self.is_element_present(*locators.BasePageLocators.GOOGLE_PAY), \
            "The element visa is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

