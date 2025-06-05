import pytest

from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--lang=ru")
    driver = webdriver.Remote(command_executor="http://164.215.97.143:4444", options=options)
    yield driver
    driver.quit()