from selenium.webdriver.common.by import By

class BasePageLocators:
    USER_INFO = (By.XPATH, "//a[@title='Особистий кабінет']")
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
    CART_SECTION = (By.XPATH, "//*[@id='cart']/button")
    CART = (By.XPATH, "//span[@class='cart-name'][contains(text(), 'Кошик')]")
    CART_DROPDOWN = (By.XPATH, "//*[@id='cart']/ul")



