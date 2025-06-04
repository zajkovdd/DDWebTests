import allure

from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By

class VKEcosystemPageLocators:
    TITLE_LABEL = (By.XPATH, '//*[@class="title-h2"]')

class VKEcosystemPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(VKEcosystemPageLocators.TITLE_LABEL)