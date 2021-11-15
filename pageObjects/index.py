from selenium.webdriver.common.by import By


class PageIndex:
    def __init__(self, driver):
        self.driver = driver

    first = (By.XPATH, "//div[@role='textbox']")

    def asd(self):
        self.driver.find_element(*PageIndex.first)
