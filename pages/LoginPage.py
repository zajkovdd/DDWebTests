import allure

from pages.BasePage import BasePageHelper
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
    ERROR_TEXT = (By.XPATH, '//*[@class="input-e login_error"]')
    GO_BACK_BUTTON = (By.XPATH, '//*[@data-l="t,cancel"]')
    SUPPORT_BUTTON = (By.XPATH, '//*[@class="svg-ic svg-ico_help_circle_16 tico_img"]')
    RECOVERY_BUTTON = (By.XPATH, '//*[@class="button-pro __wide mb-3x"]')

class LoginPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_TAB_BUTTON)
        self.find_element(LoginPageLocators.QR_TAB_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_BUTTON_QR)
        self.find_element(LoginPageLocators.CAN_NOT_LOGIN)
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON)
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON_VK)
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON_MAIL_RU)
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON_YANDEX)


    @allure.step('Нажимаем на кнопку "Войти"')
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step('Получаем текст ошибки')
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_TEXT).text

    @allure.step('Заполняем поле "Логин"')
    def type_login(self, login):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(login)
        self.attach_screenshot()

    @allure.step('Заполняем поле "Пароль"')
    def type_password(self, password):
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.attach_screenshot()

    @allure.step('Переходим к восстановлению')
    def click_recovery(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.RECOVERY_BUTTON).click()

    @allure.step('Переходим к регистрации')
    def click_registration(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON).click()
