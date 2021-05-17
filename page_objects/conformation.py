from selenium.webdriver.common.by import By


class ConformationPg:

    country_selection = (By.XPATH,"//select")
    country_name = (By.XPATH,"//select/option")
    click = (By.XPATH,"//body")
    checkbox = (By.XPATH,"//*[@type='checkbox']")
    proceed = (By.XPATH,"//button[text()='Proceed']")
    conformation = (By.XPATH,"//*[contains(@class,'wrapperTwo')]")


    def __init__(self, driver):
        self.driver = driver

    def del_country_selection(self):
        return self.driver.find_element(*ConformationPg.country_selection)

    def del_country_name(self):
        return self.driver.find_elements(*ConformationPg.country_name)

    def del_click(self):
        return self.driver.find_element(*ConformationPg.click)

    def del_checkbox(self):
        return self.driver.find_element(*ConformationPg.checkbox)

    def del_proceed(self):
        return self.driver.find_element(*ConformationPg.proceed)

    def del_conformation(self):
        return self.driver.find_element(*ConformationPg.conformation)
