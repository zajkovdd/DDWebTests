from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_TAB_BUTTON = (By.XPATH, '//*[@data-l="t,login_tab"]')
    QR_TAB_BUTTON = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    LOGIN_FIELD = (By.ID, "field_email")
    PASSWORD_FIELD = (By.ID, "field_password")
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    LOGIN_BUTTON_QR = (By.XPATH, '//*[@data-l="t,get_qr"]')
    CAN_NOT_LOGIN = (By.XPATH, '//*[@data-l="t,restore"]')
    REGISTRATION_BUTTON = (By.XPATH, '//*[@class="button-pro __sec mb-3x __wide"]')
    REGISTRATION_BUTTON_VK = (By.XPATH, '//*[@class="i ic social-icon __s __vk_id"]')
    REGISTRATION_BUTTON_MAIL_RU = (By.XPATH, '//*[@class="i ic social-icon __s __mailru"]')
    REGISTRATION_BUTTON_YANDEX = (By.XPATH, '//*[@class="i ic social-icon __s __yandex"]')

class LoginPageHelper(BasePage):
    pass