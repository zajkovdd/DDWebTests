import allure

from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.VKEcosystemPage import VKEcosystemPageHelper

BASE_URL = 'https://ok.ru/'

@allure.suite('Проверка тулбара')
@allure.title('Переход к проектам экосистемы ВК')
def test_open_vk_ecosystemm(browser):
    BasePage = BasePageHelper(browser)
    BasePage.get_url(BASE_URL)
    BasePage.check_page()
    BasePage.accept_cookie()
    LoginPage = LoginPageHelper(browser)
    current_window_id = LoginPage.get_window_id(0)
    LoginPage.click_more_button()
    LoginPage.click_vk_ecosystem()
    new_window_id = LoginPage.get_window_id(1)
    LoginPage.change_window(new_window_id)
    VKEcosystemPage = VKEcosystemPageHelper(browser)
    VKEcosystemPage.change_window(current_window_id)
    LoginPageHelper(browser)
