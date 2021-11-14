import time

from utilites.BaseClass import BaseClass


class TestSample(BaseClass):
    def test_e2e(self):
        search_field = self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
        search_field.send_keys("01601259370")
        time.sleep(10)

