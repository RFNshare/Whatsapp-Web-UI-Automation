from selenium.webdriver import Keys
from utilites.locators import *


class HomePage:
    data = "01601259370"  # Excel Implement
    msg_data = "Hello world"

    def __init__(self, driver):
        self.driver = driver
        self.locator = HomePageLocators

    def searched_contact(self):
        return self.driver.find_element(*self.locator.search_p).send_keys(HomePage.data)

    def search_field(self):
        self.driver.find_element(*self.locator.search_field_p).clear()
        self.driver.find_element(*self.locator.search_field_p).send_keys(HomePage.data)
        self.driver.find_element(*self.locator.search_field_p).send_keys(Keys.ENTER)
        self.driver.find_element(*self.locator.search_field_p).send_keys(HomePage.msg_data)
        self.driver.find_element(*self.locator.search_field_p).send_keys(Keys.ENTER)
        return self.driver.find_element(*self.locator.search_field_p)

    def msg_field(self):
        return self.driver.find_element(*self.locator.msg_field_p)

    def sent(self):
        return self.driver.find_element(*self.locator.sent_p)

    def seen_notseen(self):
        return self.driver.find_element(*self.locator.seen_notseen_p)

    def logout1(self):
        return self.driver.find_element(*self.locator.logout_1p)

    def logout2(self):
        return self.driver.find_element(*self.locator.logout_2p)
