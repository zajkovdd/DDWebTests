import allure

from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.HelpPage import HelpPageHelperHelper, HelpPageLocators
from pages.AdvertismentCabinetHelpPage import AdvertismentCabinetHelpHelper

BASE_URL = 'https://ok.ru/help'

@allure.suite('Проверка блока Помощь')
@allure.title('Проверка перехода к Рекламному кабинету')
def test_help_test(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    HelpPage = HelpPageHelperHelper(browser)
    HelpPage.scroll_to_item(HelpPageLocators.ADVERTISEMENT_CABINET)
    AdvertismentCabinetHelpHelper(browser)


