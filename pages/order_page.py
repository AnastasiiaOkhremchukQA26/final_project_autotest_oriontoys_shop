from ..pages import base_page, locators
import inspect
import re
import math


class OrderPage(base_page.BasePage):
    def click_on_logo(self):
        assert self.click_element(*locators.BasePageLocators.LOGO), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def add_to_cart_first_product(self):
        assert self.click_element(*locators.OrderPageLocators.FIRST_PRODUCT), \
            "The element is not present"
        assert self.click_element(*locators.OrderPageLocators.BUTTON_ADD_FIRST_PRODUCT), \
            "The element is not present or intractable"
        price = self.get_text(*locators.OrderPageLocators.PRICE_FIRST_PRODUCT)
        if price:
            price = float(price.replace('₴', ''))
        else:
            pass
        print(f"{inspect.currentframe().f_code.co_name} - Ok")
        if price:
            return price

    def is_alert_success_after_add_first_product(self):
        assert self.is_element_appears_after_while(*locators.OrderPageLocators.ALERT_SUCCESS_AFTER_ADD_FIRST_PRODUCT, timeout=5), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def press_btn_continue_shop_popup(self):
        assert self.click_element(*locators.BasePageLocators.LOGO), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def add_to_cart_second_product(self):
        assert self.click_element(*locators.MainPageLocators.ACTIVITIES), \
            "The element currency is not present or intractable"
        self.explicit_wait(2)
        assert self.click_element(*locators.OrderPageLocators.SECOND_PRODUCT), \
            "The element is not present"
        assert self.clear_field(*locators.OrderPageLocators.SECOND_PRODUCT_INPUT_NUMBER_QTY), \
            "The element currency is not present"
        assert self.input_data(*locators.OrderPageLocators.SECOND_PRODUCT_INPUT_NUMBER_QTY, 2), \
            "The element currency is not present"
        price = self.get_text(*locators.OrderPageLocators.PRICE_SECOND_PRODUCT)
        price = float(price.replace('₴', '')) * 2
        assert self.click_element(*locators.OrderPageLocators.CHOOSE_COLOR_SECOND_PRODUCT), \
            "The element is not present"
        assert self.click_element(*locators.OrderPageLocators.ADD_COLOR_SECOND_PRODUCT), \
            "The element is not present"
        assert self.click_element(*locators.OrderPageLocators.BUTTON_ADD_SECOND_PRODUCT), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")
        if price:
            return price

    '''
    def check_total_price_qty(self, price1, price2, qty):
        total_price_str = self.get_text(*locators.OrderPageLocators.TOTAL_PRICE)
        self.explicit_wait(2)

        # Видаляємо всі символи окрім цифр
        total_price = int(re.sub("[^0-9]", "", total_price_str))

        # Перевіряємо, чи total_price має вірній формат
        assert math.isclose(total_price, price1 + price2), "Total price doesn't match the actual total"

        qty_actual = int(self.get_text(*locators.OrderPageLocators.QTY))
        assert qty_actual == qty, "QTY doesn't match the actual qty"

        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    '''
    def check_products(self):
        assert self.click_element(*locators.OrderPageLocators.CART_PRODUCTS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def check_cart(self):
        assert self.is_element_present(*locators.OrderPageLocators.CHECKOUT_BTN_POPUP), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def press_btn_checkout_popup(self):
        assert self.hover_action(*locators.OrderPageLocators.CART_PRODUCTS), \
            "The element is not present"
        assert self.click_element(*locators.OrderPageLocators.CHECKOUT_BTN_POPUP), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def press_payment_after_delivery(self):
        assert self.click_element(*locators.OrderPageLocators.PAYMENT_AFTER_DELIVERY), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def add_notice(self):
        assert self.input_data(*locators.OrderPageLocators.INPUT_NOTE, "Test.."), \
            "The element currency is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def press_green_btn_checkout(self):
        assert self.click_element(*locators.OrderPageLocators.CHECKOUT_BUTTON), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_success(self):
        assert self.is_element_present(*locators.OrderPageLocators.SUCCESS_ORDER), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")
