from selenium.webdriver.common.by import By


class HomePageLocators(object):
    search_p = (By.XPATH, "//div[@role='textbox']")
    search_field_p = (By.XPATH, "//div[@role='textbox']")
    msg_field_p = (By.CSS_SELECTOR, "div[title='Type a message']")
    sent_p = (By.CSS_SELECTOR, 'span[data-testid="msg-check"]')
    seen_notseen_p = (By.CSS_SELECTOR, 'span[data-testid="msg-dblcheck"]')
    logout_1p = (By.XPATH, "//span[@data-testid='menu']")
    logout_2p = (By.XPATH, "//div[@aria-label='Log out']")
