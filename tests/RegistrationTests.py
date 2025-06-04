import allure

from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.RegistrationPage import RegistrationPageHelperHelper


BASE_URL = 'https://ok.ru/'

@allure.suite('Проверка формы авторизации')
@allure.title('Проверка ошибки при пустой форме авторизации')
def test_registration_random_country(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.click_registration()
    RegistrationPage = RegistrationPageHelperHelper(browser)
    SelectedCountryCode = RegistrationPage.select_random_country()
    ActualCountryCode = RegistrationPage.get_phone_field_value()
    assert ActualCountryCode == SelectedCountryCode
