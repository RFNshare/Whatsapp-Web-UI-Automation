from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    search_p = (By.XPATH, "//div[@role='textbox']")
    search_field_p = (By.XPATH, "//div[@role='textbox']")
    msg_field_p = (By.CSS_SELECTOR, "div[title='Type a message']")
    sent_p = (By.CSS_SELECTOR,'span[data-testid="msg-check"]')
    seen_notseen_p = (By.CSS_SELECTOR,'span[data-testid="msg-dblcheck"]')
    logout_1p = (By.XPATH, "//span[@data-testid='menu']")
    logout_2p = (By.XPATH, "//div[@aria-label='Log out']")

    def searched_contact(self):
        return self.driver.find_element(*HomePage.search_p)

    def search_field(self):
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
