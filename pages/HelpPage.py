import allure
from selenium.webdriver import ActionChains

from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By


class HelpPageLocators:
    SEARCH_FIELD = (By.XPATH, '//*[@class="input__prt1l __size-m__prt1l input__t53m6 input-right__t53m6 input-left__t53m6 __soft__prt1l"]')
    ACTUAL = (By.XPATH, '//*[@name="illustrations/ill_actual"]')
    REGISTRATION = (By.XPATH, '//*[@name="illustrations/ill_registration"]')
    MY_PROFILE = (By.XPATH, '//*[@name="illustrations/ill_my_profile"]')
    COMMUNICATION = (By.XPATH, '//*[@name="illustrations/ill_communication"]')
    ACCESS_PROFILE = (By.XPATH, '//*[@href="/help/dostup-k-profilu"]')
    SECURITY = (By.XPATH, '//*[@name="illustrations/ill_security"]')
    GROUPS = (By.XPATH, '//*[@name="illustrations/ill_group_group"]')
    PAID_FEATURES = (By.XPATH, '//*[@name="illustrations/ill_paid_features"]')
    VIOLATION_AND_SPAM = (By.XPATH, '//*[@name="illustrations/ill_violation_spam"]')
    GAMES_AND_APPS = (By.XPATH, '//*[@name="illustrations/ill_app_game"]')
    OTHER_SERVICES = (By.XPATH, '//*[@name="illustrations/ill_other_services"]')
    USEFUL_INFO = (By.XPATH, '//*[@name="illustrations/ill_useful_info"]')
    ADVERTISEMENT_CABINET = (By.XPATH, '//*[@name="illustrations/ill_advertising_cabinet"]')

class HelpPageHelperHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(HelpPageLocators.SEARCH_FIELD)
        self.find_element(HelpPageLocators.ACTUAL)
        self.find_element(HelpPageLocators.REGISTRATION)
        self.find_element(HelpPageLocators.MY_PROFILE)
        self.find_element(HelpPageLocators.COMMUNICATION)
        self.find_element(HelpPageLocators.ACCESS_PROFILE)
        self.find_element(HelpPageLocators.SECURITY)
        self.find_element(HelpPageLocators.GROUPS)
        self.find_element(HelpPageLocators.PAID_FEATURES)
        self.find_element(HelpPageLocators.VIOLATION_AND_SPAM)
        self.find_element(HelpPageLocators.GAMES_AND_APPS)
        self.find_element(HelpPageLocators.OTHER_SERVICES)
        self.find_element(HelpPageLocators.USEFUL_INFO)
        self.find_element(HelpPageLocators.ADVERTISEMENT_CABINET)

    @allure.step('Скролим до нужной плитки')
    def scroll_to_item(self, locator):
        scroll_item = self.find_element(locator)
        ActionChains(self.driver).scroll_to_element(scroll_item).click(scroll_item).perform()

