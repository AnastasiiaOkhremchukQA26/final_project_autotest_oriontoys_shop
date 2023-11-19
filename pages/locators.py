from selenium.webdriver.common.by import By

class BasePageLocators:
    USER_INFO = (By.XPATH, "//span[@class='expand-more']")
    REGISTER = (By.XPATH, "//ul[@class='dropdown-menu']//a[contains(text(), 'Реєстрація')]")
    AUTHORIZATION = (By.XPATH, "//ul[@class='dropdown-menu']//a[contains(text(), 'Авторизація')]")
    WISHLIST = (By.XPATH, "//ul[@class='dropdown-menu']//a[contains(@title, 'Закладки')]")
    LOGOUT = (By.XPATH, "//a[@href='https://oriontoys.shop/index.php?route=account/logout' and text()='Вихід']")
    LANGUAGE = (By.XPATH, "//*[@id='form-language']/div/button/img")
    UKRAINIAN = (By.XPATH, "//ul[@class='dropdown-menu']//button[contains(., 'Українська')]")
    RUSSIAN = (By.XPATH, "//ul[@class='dropdown-menu']//button[contains(., 'Русский')]")
    SOCIAL_NETWORKS = (By.XPATH, "//div[@class='block-social']")
    FACEBOOK = (By.XPATH, "//div[@class='block-social']//a[contains(@class, 'facebook')]")
    YOUTUBE = (By.XPATH, "//div[@class='block-social']//a[contains(@class, 'youtube')]")
    INSTAGRAM = (By.XPATH, "//div[@class='block-social']//a[contains(@class, 'instagram')]")
    LOGO = (By.XPATH, "//div[@id='_desktop_logo']//img")
    SEARCH = (By.XPATH, "//div[@id='_desktop_seach_widget']//input[@type='text']")
    SEARCH_BUTTON = (By.XPATH, "//*[@id='ajax-search-btn']")
    CONTACT_INFO = (By.XPATH, "//*[@id='_desktop_contactinfo']")
    CART_SECTION = (By.XPATH, "//*[@id='cart']/button")
    CART = (By.XPATH, "//span[@class='cart-name'][contains(text(), 'Кошик')]")
    CART_DROPDOWN = (By.XPATH, "//*[@id='cart']/ul")

    ABOUT_US = (By.XPATH, "//a[@class='extra-link' and text()='Про нас']")
    DELIVERY_AND_PAYMENT = (By.XPATH, "//a[@class='extra-link' and text()='Доставка та оплата']")
    RETURNS_AND_WARRANTY = (By.XPATH, "//a[@class='extra-link' and text()='Повернення та гарантія']")
    CONTACTS = (By.XPATH, "//a[@class='extra-link' and text()='Контакти']")
    SPECIALS = (By.XPATH, "//a[@class='extra-link' and text()='Акції']")

    SUBSCRIBE = (By.XPATH, "//a[@class='button btn-submit']")
    INPUT_SUBSCRIBE = (By.XPATH, "//input[@id='subscribe_email']")
    FOOTER = (By.XPATH, "//p[@style='text-align:left;']")
    MASTERCARD = (By.XPATH, "//div[@class='ishipaymentblock']//div[@class='paymentblock'][1]/a/img")
    VISA = (By.XPATH, "//div[@class='ishipaymentblock']//div[@class='paymentblock'][2]/a/img")
    APPLE_PAY = (By.XPATH, "//div[@class='ishipaymentblock']//div[@class='paymentblock'][3]/a/img")
    GOOGLE_PAY = (By.XPATH, "//div[@class='ishipaymentblock']//div[@class='paymentblock'][4]/a/img")

class MainPageLocators:
    DELIVERY_ACROSS_UKRAINE = (By.XPATH, "(//div[@class='services col-lg-3 col-md-3 col-sm-6 col-xs-6'])[1]")
    FREE_SHIPPING = (By.XPATH, "(//div[@class='services col-lg-3 col-md-3 col-sm-6 col-xs-6'])[2]")
    CONVENIENT_PAYMENT = (By.XPATH, "(//div[@class='services col-lg-3 col-md-3 col-sm-6 col-xs-6'])[3]")
    GUARANTEE = (By.XPATH, "(//div[@class='services col-lg-3 col-md-3 col-sm-6 col-xs-6'])[4]")

    CATEGORIES = (By.XPATH, "(//div[@class='block_content'])[1]")
    ACTIVITIES = (By.XPATH, "//a[@href='https://oriontoys.shop/aktyvnyy-vidpochynok/']")

    SELECTION_OF_GOODS = (By.XPATH, "(//div[@class='block_content'])[2]")
    RECOMMENDED_PRODUCTS = (By.XPATH, "//a[contains(@href,'#featured-products-block')]")
    POPULAR_PRODUCTS = (By.XPATH, "//a[contains(@href,'#bestseller-products-block')]")
    NOVELTY = (By.XPATH, "//a[contains(@href,'#new-products-block')]")

    OFFER_OF_THE_DAY = (By.XPATH, "//span[text()='Пропозиція дня']")

    ACTION = (By.XPATH, "//section[@class='ishispecial col-lg-8 col-md-12 col-sm-12 col-xs-12']")

    LATEST_NEWS = (By.XPATH, "//div[@class='block_content container']")
    CAROUSEL_OF_NEWS = (By.XPATH, "//*[@id='smartblog-carousel']")



class SignupLoginPageLocators:
    GO_TO_SIGNUP = (By.XPATH, "//a[@href='https://oriontoys.shop/index.php?route=account/simpleregister' and contains(@class, 'btn-primary')]")
    H1_SIGNUP = (By.XPATH, "//h1[text() = 'Швидка реєстрація']")
    INPUT_EMAIL = (By.XPATH, "//input[@type='email']")
    INPUT_PASSWORD = (By.XPATH, "//*[@id='register_password']")
    INPUT_CONFIRM_PASSWORD = (By.XPATH, "//*[@id='register_confirm_password']")
    INPUT_NAME = (By.XPATH, "//*[@id='register_firstname']")
    INPUT_PHONE = (By.XPATH, "//*[@id='register_telephone']")
    INPUT_COUNTRY = (By.XPATH, "//*[@id='register_country_id']/option[11]")
    INPUT_CITY = (By.XPATH, "//*[@id='register_zone_id']/option[147]")
    INPUT_POST = (By.XPATH, "//*[@id='register_city']/option[7]")
    INPUT_POSTCODE = (By.XPATH, "//*[@id='register_postcode']")
    INPUT_ADDRESS = (By.XPATH, "//*[@id='register_address_1']")
    BUTTON_SIGNUP = (By.XPATH, "//*[@id='simpleregister_button_confirm']")
    H1_VHOD = (By.XPATH, "//ul[@class='dropdown-menu']//a[contains(text(), 'Авторизація')]")
    BUTTON_LOGIN = (By.XPATH, "//ul[@class='dropdown-menu']//a[contains(text(), 'Авторизація')]")
    SUCCESS = (By.XPATH, "//*[@id='content']/div[1]/h1")

class OrderPageLocators:
    FIRST_PRODUCT = (By.XPATH, "//a[@href='https://oriontoys.shop/igrashka-vertolit-arbalet-vijskovyj-patriot-orion-art-268v3']")
    BUTTON_ADD_FIRST_PRODUCT = (By.XPATH, "//*[@id='button-cart']")
    PRICE_FIRST_PRODUCT = (By.XPATH, "//li[@class='product-price hidden-xs']/h2")
    ALERT_SUCCESS_AFTER_ADD_FIRST_PRODUCT = (By.XPATH, "//div[@class='col-xs-12 alert alert-success'][@data-notify='container']")
    SECOND_PRODUCT = (By.XPATH, "//a[@href='https://oriontoys.shop/aktyvnyj-vidpochynok/bajk-art-503'']")
    SECOND_PRODUCT_INPUT_NUMBER_QTY = (By.XPATH, "//*[@id='input-quantity']")
    PRICE_SECOND_PRODUCT = (By.XPATH, "//li[@class='product-price hidden-xs']/h2")
    CHOOSE_COLOR_SECOND_PRODUCT = (By.XPATH, "//*[@id='input-option286']")
    ADD_COLOR_SECOND_PRODUCT = (By.XPATH, "//select[@id='input-option286']/option[@value='178']")
    BUTTON_ADD_SECOND_PRODUCT = (By.XPATH, "//button[@id='button-cart']")
    TOTAL_PRICE = (By.XPATH, "//span[@class='cart-products-count']")
    QTY = (By.XPATH, "//span[@class='cart-products-count hidden-lg hidden-md']/text()")
    CHECKOUT_BTN_POPUP = (By.XPATH, "//button[@class='btn btn-primary btn-cartblock' and @style='width:100%;']")
    YA_ZAREESTROVANYU = (By.XPATH, "//a[@href='javascript:void(0)' and @data-onclick='openLoginBox']")


    CART_REG_FORM = (By.XPATH, "//div[@class = 'cart-reg']")
    INPUT_EMAIL = (By.XPATH, "//input[@name = 'email']")
    INPUT_PASSWORD = (By.XPATH, "//input[@name = 'password']")
    INPUT_NOTE = (By.XPATH, "//textarea[@name= 'note']")
    CHECKOUT_BUTTON = (By.XPATH, "//button[@class = 'btn green']")

class CabinetPageLocators:
    pass


class CategoryPageLocators:
    pass


class SearchPageLocators:
    pass











