import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePageLocators:
    LOGO_BUTTON = (By.ID, 'nohook_logo_link')
    VK_ECOSYSTEM_BUTTON = (By.XPATH, '//*[@class="svg-ic svg-More vk-ecosystem-icon"]')
    MORE_BUTTON = (By.XPATH, '//*[@class="toolbar_nav_i_ic"]')
    COOKIE_BUTTON_ACCEPT = (By.XPATH, '//button[text()="Разрешить все"]')

class BasePageHelper:
    def __init__(self, driver):
        self.driver = driver


    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(BasePageLocators.LOGO_BUTTON)
        self.find_element(BasePageLocators.MORE_BUTTON)

    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator), message=f'Не удалось найти элемент {locator}')

    def find_elements(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_all_elements_located(locator), message=f'Не удалось найти элемент {locator}')

    @allure.step('Открываем страницу')
    def get_url(self, url):
        return self.driver.get(url)

    def attach_screenshot(self):
        allure.attach(self.driver.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)

    @allure.step('Нажимаем кноку экосистемы')
    def click_vk_ecosystem(self):
        self.attach_screenshot()
        self.find_element(BasePageLocators.VK_ECOSYSTEM_BUTTON).click()

    @allure.step('Нажимаем кноку "еще"')
    def click_more_button(self):
        self.find_element(BasePageLocators.MORE_BUTTON).click()

    @allure.step('Получаем айди вкладки')
    def get_window_id(self, index):
        return self.driver.window_handles[index]

    @allure.step('Переходим на экран с айди')
    def change_window(self, window_id):
        self.driver.switch_to.window(window_id)

    @allure.step('Принимаем куки')
    def accept_cookie(self):
        self.find_element(BasePageLocators.COOKIE_BUTTON_ACCEPT).click()