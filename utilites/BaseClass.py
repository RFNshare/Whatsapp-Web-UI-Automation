import inspect
import logging
import pytest


@pytest.mark.usefixtures("setup")
class BaseClass:
    # def verifyLinkPresence(self, text):
    #     element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.LINK_TEST, text))

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger
