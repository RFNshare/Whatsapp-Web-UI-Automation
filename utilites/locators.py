from selenium.webdriver.common.by import By


class HomePageLocators(object):
    # --- Search Box Locators ---
    SEARCH_TEXTBOX = (By.XPATH, "//div[@role='textbox']")

    # --- Message Box Locators ---
    MESSAGE_TEXTBOX = (By.CSS_SELECTOR, "div[title='Type a message']")

    # --- Last Sent Message Locators ---
    MESSAGE_SENT = (By.CSS_SELECTOR, 'span[data-testid="msg-check"]')
    MESSAGE_SEEN_UNSEEN = (By.CSS_SELECTOR, 'span[data-testid="msg-dblcheck"]')

    # --- Logout Button's Locators ---
    THREE_DOT_BUTTON = (By.XPATH, "//span[@data-testid='menu']")
    LOGOUT_BUTTON = (By.XPATH, "//div[@aria-label='Log out']")

    BASE_URL = (By.XPATH, "//meta[@content='https://web.whatsapp.com/']")
