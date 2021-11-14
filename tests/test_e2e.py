import time

from utilites.BaseClass import BaseClass


class TestWhatsApp(BaseClass):
    def test_tc001(self):
        search_field = self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
        search_field.send_keys("01601259370")
        time.sleep(10)
    def test_tc001(self):
        pass


