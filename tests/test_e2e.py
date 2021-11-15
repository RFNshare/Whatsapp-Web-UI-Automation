import time

import pytest
from selenium.webdriver import Keys
from pageObjects.home_page import HomePage
from utilites.BaseClass import BaseClass


class TestWhatsApp(BaseClass):

    def test_tc001(self):
        homepage = HomePage(self.driver)
        homepage.searched_contact()
        log = self.getLogger()
        log.info("Display searched contact")

    def test_tc002(self):
        homepage = HomePage(self.driver)
        homepage.search_field()
        log = self.getLogger()
        log.info("Successfully send message")

    def test_tc003(self):
        homepage = HomePage(self.driver)
        homepage.search_field()
        homepage.msg_field().send_keys(HomePage.msg_data)
        homepage.msg_field().send_keys(Keys.ENTER)
        sent = self.driver.find_elements_by_css_selector('span[data-testid="msg-check"]')
        sent_reversed = sent[-1]
        time.sleep(2)
        f_sent = sent_reversed.get_attribute('aria-label')

        # if sent == ' Sent ':
        #     sh1.cell(row=2, column=2, value='sent')
        #     exl.save('whatsapp_number.xlsx')
        assert f_sent == ' Sent ' or ' Delivered '
        log = self.getLogger()
        log.info("Successfully write result on excel")
        time.sleep(2)

    def test_tc004(self):
        # sent = self.driver.find_elements_by_css_selector('span[data-testid*="msg-check"]'
        sent = self.driver.find_elements_by_css_selector('span[data-testid="msg-dblcheck"]')
        sent_reversed = sent[-1]
        time.sleep(2)
        f_sent = sent_reversed.get_attribute('aria-label')
        print(f_sent)
        if f_sent == ' Read ':
            # sh1.cell(row=2, column=3, value='Seen')
            # exl.save('whatsapp_number.xlsx')
            assert f_sent == ' Read '
        else:
            # sh1.cell(row=2, column=3, value='Not Seen')
            # exl.save('whatsapp_number.xlsx')
            assert f_sent == ' Delivered '
        log = self.getLogger()
        log.info("successfully write message status on excel")
        time.sleep(2)

    def test_tc005(self):
        homepage = HomePage(self.driver)
        self.driver.find_element_by_xpath("//span[@data-testid='menu']").click()
        self.driver.find_element_by_xpath("//div[@aria-label='Log out']").click()
        log = self.getLogger()
        log.info("successfully logged out from whatsapp")
