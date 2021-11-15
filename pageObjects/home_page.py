from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class HomePage:
    data = "01601259370"  # Excel Implement
    msg_data = "Hello world"

    def __init__(self, driver):
        self.driver = driver

    search_p = (By.XPATH, "//div[@role='textbox']")
    search_field_p = (By.XPATH, "//div[@role='textbox']")
    msg_field_p = (By.CSS_SELECTOR, "div[title='Type a message']")
    sent_p = (By.CSS_SELECTOR, 'span[data-testid="msg-check"]')
    seen_notseen_p = (By.CSS_SELECTOR, 'span[data-testid="msg-dblcheck"]')
    logout_1p = (By.XPATH, "//span[@data-testid='menu']")
    logout_2p = (By.XPATH, "//div[@aria-label='Log out']")

    def searched_contact(self):
        return self.driver.find_element(*HomePage.search_p).send_keys(HomePage.data)

    def search_field(self):
        self.driver.find_element(*HomePage.search_field_p).clear()
        self.driver.find_element(*HomePage.search_field_p).send_keys(HomePage.data)
        self.driver.find_element(*HomePage.search_field_p).send_keys(Keys.ENTER)
        self.driver.find_element(*HomePage.search_field_p).send_keys(HomePage.msg_data)
        self.driver.find_element(*HomePage.search_field_p).send_keys(Keys.ENTER)
        return self.driver.find_element(*HomePage.search_field_p)


    def msg_field(self):
        return self.driver.find_element(*HomePage.msg_field_p)

    def sent(self):
        return self.driver.find_element(*HomePage.sent_p)

    def seen_notseen(self):
        return self.driver.find_element(*HomePage.seen_notseen_p)

    def logout1(self):
        return self.driver.find_element(*HomePage.logout_1p)

    def logout2(self):
        return self.driver.find_element(*HomePage.logout_2p)
