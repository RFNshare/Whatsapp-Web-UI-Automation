import time

import pytest
from selenium.webdriver import Keys

from PageObjects.home_page import HomePage
from utilites.BaseClass import BaseClass
from utilites.TestData import TestData


class TestWhatsApp(BaseClass):

    def test_tc001(self):
        homepage = HomePage(self.driver)
        homepage.searched_contact().send_keys(TestData.SAMPLE_DATA)
        time.sleep(2)
        assert homepage.searched_contact().text == TestData.SAMPLE_DATA
        log = self.getLogger()
        log.info("Display searched contact")

    @pytest.mark.now
    def test_tc002(self):
        homepage = HomePage(self.driver)
        homepage.search_field()
        homepage.msg_field()
        log = self.getLogger()
        log.info("Successfully send message")

    def test_tc003(self):
        homepage = HomePage(self.driver)
        homepage.search_field()
        homepage.msg_field()
        sent = self.driver.find_elements_by_css_selector('span[data-testid="msg-check"]')
        sent_reversed = sent[-1]
        time.sleep(2)
        f_sent = sent_reversed.get_attribute('aria-label')

        if sent == ' Sent ' or ' Delivered ':
            TestData.sheet.cell(row=2, column=2, value='Sent')
            TestData.data_load.save(TestData.EXCEL_EXECUTABLE_PATH)
        assert f_sent == ' Sent ' or ' Delivered '
        log = self.getLogger()
        log.info("Successfully write result on excel")
        time.sleep(2)

    def test_tc004(self):
        sent = self.driver.find_elements_by_css_selector('span[data-testid="msg-dblcheck"]')
        sent_reversed = sent[-1]
        time.sleep(2)
        f_sent = sent_reversed.get_attribute('aria-label')

        if f_sent == ' Read ':
            TestData.sheet.cell(row=2, column=3, value='Seen')
            # sh1.cell(row=2, column=3, value='Seen')
            # exl.save('whatsapp_number.xlsx')
            assert f_sent == ' Read '
        else:
            TestData.sheet.cell(row=2, column=3, value='Not Seen')
            TestData.data_load.save(TestData.EXCEL_EXECUTABLE_PATH)
            assert f_sent == ' Delivered '
        log = self.getLogger()
        log.info("successfully write message status on excel")
        time.sleep(2)

    def test_tc005(self):
        homepage = HomePage(self.driver)
        homepage.logout1().click()
        homepage.logout2().click()
        log = self.getLogger()
        log.info("successfully logged out from whatsapp")
