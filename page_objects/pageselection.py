from selenium.webdriver.common.by import By

from page_objects.name_selection import Dataentery


class PgSelect():

    page1 = (By.XPATH, "//*[contains(text(),'Automation Practise - 1')]")
    page2 = (By.XPATH, "//*[contains(text(),'Automation Practise - 3')]")

    def __init__(self, driver):
        self.driver = driver

    def select_pg1(self):
        self.driver.find_element(*PgSelect.page1).click()
        vegetable = Dataentery(self.driver)
        return vegetable

    def select_pg2(self):
        self.driver.find_element(*PgSelect.page2).click()
        formfill = Dataentery(self.driver)
        return formfill
