from selenium.webdriver.common.by import By

class BasePageLocators:
    USER_INFO = (By.XPATH, "//span[@class='expand-more']")
    REGISTER = (By.XPATH, "//ul[@class='dropdown-menu']//a[contains(text(), 'Реєстрація')]")
    AUTHORIZATION = (By.XPATH, "//ul[@class='dropdown-menu']//a[contains(text(), 'Авторизація')]")
    WISHLIST = (By.XPATH, "//ul[@class='dropdown-menu']//a[contains(@title, 'Закладки')]")
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

    SUBSCRIBE = (By.XPATH, "//a[@class='button btn-submit']")
    INPUT_SUBSCRIBE = (By.XPATH, "//input[@id='subscribe_email']")
    FOOTER = (By.XPATH, "//p[@style='text-align:left;']")
    MASTERCARD = (By.XPATH, "//div[@class='ishipaymentblock']//div[@class='paymentblock'][1]/a/img")
    VISA = (By.XPATH, "//div[@class='ishipaymentblock']//div[@class='paymentblock'][2]/a/img")
    APPLE_PAY = (By.XPATH, "//div[@class='ishipaymentblock']//div[@class='paymentblock'][3]/a/img")
    GOOGLE_PAY = (By.XPATH, "//div[@class='ishipaymentblock']//div[@class='paymentblock'][4]/a/img")

class MainPageLocators:
    ABOUT_US = (By.XPATH, "//a[@class='extra-link' and text()='Про нас']")
    DELIVERY_AND_PAYMENT = (By.XPATH, "//a[@class='extra-link' and text()='Доставка та оплата']")
    RETURNS_AND_WARRANTY = (By.XPATH, "//a[@class='extra-link' and text()='Повернення та гарантія']")
    CONTACTS = (By.XPATH, "//a[@class='extra-link' and text()='Контакти']")
    SPECIALS = (By.XPATH, "//a[@class='extra-link' and text()='Акції']")

    DELIVERY_ACROSS_UKRAINE = (By.XPATH, "(//div[@class='services col-lg-3 col-md-3 col-sm-6 col-xs-6'])[1]")
    FREE_SHIPPING = (By.XPATH, "(//div[@class='services col-lg-3 col-md-3 col-sm-6 col-xs-6'])[2]")
    CONVENIENT_PAYMENT = (By.XPATH, "(//div[@class='services col-lg-3 col-md-3 col-sm-6 col-xs-6'])[3]")
    GUARANTEE = (By.XPATH, "(//div[@class='services col-lg-3 col-md-3 col-sm-6 col-xs-6'])[4]")

    CATEGORIES = (By.XPATH, "(//div[@class='block_content'])[1]")

    SELECTION_OF_GOODS = (By.XPATH, "//*[@id='ishiproductblock-1800853095']")
    RECOMMENDED_PRODUCTS = (By.XPATH, "//*[@id='ishiproductblock-1800853095']/ul/li[1]/a")
    POPULAR_PRODUCTS = (By.XPATH, "//*[@id='ishiproductblock-1800853095']/ul/li[2]/a")
    NOVELTY = (By.XPATH, "//*[@id='ishiproductblock-1800853095']/ul/li[3]/a")

    OFFER_OF_THE_DAY = (By.XPATH, "//*[@id='ishispecialdeal-970343166']")

    ACTION = (By.XPATH, "//section[@class='ishispecial col-lg-8 col-md-12 col-sm-12 col-xs-12']")

    LATEST_NEWS = (By.XPATH, "//div[@class='block_content container']")
    CAROUSEL_OF_NEWS = (By.XPATH, "//*[@id='smartblog-carousel']")











