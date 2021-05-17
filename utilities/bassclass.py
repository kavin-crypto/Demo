import pytest
import inspect
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("browser_invoke")
class BassClass:

    def wait(self, text):
        w = WebDriverWait(self.driver, 5)
        w.until(expected_conditions.element_to_be_clickable((By.XPATH, text)))

    def selecttag(self, locator, text):
        tag = Select(locator)
        tag.select_by_visible_text(text)

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)  # in run time it automatically catches the filename
        filelocation = logging.FileHandler("/Users/kavin/Desktop/script/reports/logfile.log")  # FileHandler is used to create a file to save all logs
        format = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filelocation.setFormatter(format)
        logger.addHandler(filelocation)

        logger.setLevel(logging.DEBUG)
        return logger
