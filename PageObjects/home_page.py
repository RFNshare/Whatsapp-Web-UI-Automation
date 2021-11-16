from selenium.webdriver import Keys

from utilites.TestData import TestData
from utilites.locators import *


class HomePage:
    data = "01601259370"  # Excel Implement

    def __init__(self, driver):
        self.driver = driver
        self.locator = HomePageLocators
        # self.driver.get(TestData.BASE_URL)

    def searched_contact(self):
        return self.driver.find_element(*self.locator.SEARCH_TEXTBOX)

    def search_field(self):
        self.driver.find_element(*self.locator.SEARCH_TEXTBOX).clear()
        self.driver.find_element(*self.locator.SEARCH_TEXTBOX).send_keys(TestData.SAMPLE_DATA)
        self.driver.find_element(*self.locator.SEARCH_TEXTBOX).send_keys(Keys.ENTER)
        return self.driver.find_element(*self.locator.SEARCH_TEXTBOX)

    def msg_field(self):
        self.driver.find_element(*self.locator.MESSAGE_TEXTBOX).send_keys(TestData.SEARCH_TERM)
        self.driver.find_element(*self.locator.MESSAGE_TEXTBOX).send_keys(Keys.ENTER)
        return self.driver.find_element(*self.locator.MESSAGE_TEXTBOX)

    def sent(self):
        return self.driver.find_elements(*self.locator.MESSAGE_SENT)

    def seen_notseen(self):
        return self.driver.find_element(*self.locator.MESSAGE_SEEN_UNSEEN)

    def logout1(self):
        return self.driver.find_element(*self.locator.THREE_DOT_BUTTON)

    def logout2(self):
        return self.driver.find_element(*self.locator.LOGOUT_BUTTON)
