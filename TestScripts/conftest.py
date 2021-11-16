import time

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(
            executable_path='C:/files/chromedriver.exe')
    elif browser_name == "firefox":
        driver = webdriver.Firefox(
            executable_path=r'C:/files/geckodriver.exe')

    driver.get('https://web.whatsapp.com/')
    driver.implicitly_wait(180)
    driver.maximize_window()
    request.cls.driver = driver
    time.sleep(2)
    yield
    driver.close()
