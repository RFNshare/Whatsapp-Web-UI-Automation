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

    def test_tc002(self):
        homepage = HomePage(self.driver)
        homepage.search_field()
        homepage.msg_field()
        log = self.getLogger()
        log.info("Successfully send message")

    @pytest.mark.now
    def test_tc003(self):
        homepage = HomePage(self.driver)
        log = self.getLogger()
        homepage.search_field()
        homepage.msg_field()
        sent_reversed = homepage.sent()[-1]
        time.sleep(2)
        f_sent = sent_reversed.get_attribute('aria-label')
        assert f_sent == ' Sent ' or ' Delivered '
        try:
            if f_sent == ' Sent ' or ' Delivered ':
                TestData.sheet.cell(row=2, column=2, value='Sent')
                TestData.data_load.save(TestData.EXCEL_EXECUTABLE_PATH)
                log.info("Successfully write result on excel")
            elif f_sent == ' Pending ':
                log.warning(TestData._404)
        except Exception as e:
            log.error(e)
            log.error("Close your excel file & run test case again")
        finally:
            time.sleep(2)

    @pytest.mark.now
    def test_tc004(self):
        homepage = HomePage(self.driver)
        log = self.getLogger()
        sent_reversed = homepage.seen_notseen()[-1]
        time.sleep(2)
        f_sent = sent_reversed.get_attribute('aria-label')
        assert f_sent == ' Read ' or ' Delivered '
        try:
            if f_sent == ' Read ':
                TestData.sheet.cell(row=2, column=3, value='Seen')
                TestData.data_load.save(TestData.EXCEL_EXECUTABLE_PATH)
            elif f_sent == ' Delivered ':
                TestData.sheet.cell(row=2, column=3, value='Not Seen')
                TestData.data_load.save(TestData.EXCEL_EXECUTABLE_PATH)
            else:
                log.warning(TestData._404)
        except Exception as e:
            log.error(e)
            log.error("Close your excel file & run test case again")
        finally:
            time.sleep(2)
        log.info("successfully write message status on excel")
        time.sleep(2)

    def test_tc005(self):
        homepage = HomePage(self.driver)
        homepage.logout1().click()
        homepage.logout2().click()
        log = self.getLogger()
        log.info("successfully logged out from whatsapp")
