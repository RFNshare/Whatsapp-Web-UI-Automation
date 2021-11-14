from selenium import webdriver
import pytest
import time


@pytest.fixture(scope="class")
def setup(request):
    # Getting Cached files for Auto login
    # options = webdriver.ChromeOptions()
    # options.add_argument(r'--user-data-dir=C:\Users\rfnsh\AppData\Local\Google\Chrome\User Data\Default')
    # options.add_argument('--profile--directory=Default')

    driver = webdriver.Firefox(
        executable_path=r'C:\Users\rfnsh\PycharmProjects\WhatsappWebUiAutomation\utilites\geckodriver.exe')
    driver.get('https://web.whatsapp.com/')
    time.sleep(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
