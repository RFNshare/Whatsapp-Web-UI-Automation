import time
from selenium.webdriver import Keys

from utilites.BaseClass import BaseClass


class TestWhatsApp(BaseClass):
    def test_tc001(self):
        data = "01601259370"  # Excel Implement
        search_field = self.driver.find_element_by_xpath("//div[@role='textbox']")
        search_field.send_keys(data)
        time.sleep(2)
        assert self.driver.find_element_by_xpath("//div[@role='textbox']").text == data
        search_field.clear()

    def test_tc002(self):
        data = "01601259370"  # Excel Implement
        search_field = self.driver.find_element_by_xpath("//div[@role='textbox']")
        search_field.send_keys(data)
        search_field.send_keys(Keys.ENTER)
        msg_field = self.driver.find_element_by_css_selector("div[title='Type a message']")
        msg_field.send_keys('Hello world')
        msg_field.send_keys(Keys.ENTER)
        time.sleep(2)
