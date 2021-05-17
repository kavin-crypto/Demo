from selenium.webdriver.common.by import By


class Dataentery:

    name = (By.XPATH, "//*[contains(@class,'product')]/h4")
    # quantity = (By.XPATH, "parent ::div/div[2]/a[2]")
    # addtocart = (By.XPATH, "parent ::div/div[3]/button")
    formname = (By.XPATH, "//*[contains(text(),'Name')]/parent :: div/input")
    email = (By.XPATH, "//*[@name='email']")
    password = (By.XPATH, "//*[@placeholder='Password']")
    dob = (By.XPATH, "//*[@name='bday']")
    gender = (By.XPATH, "//select[@id='exampleFormControlSelect1']")
    submit = (By.XPATH, "//input[@type='submit']")
    conformation = (By.XPATH,"//*[contains(@class,'alert-success')]")

    def __init__(self, driver):
        self.driver = driver

    def veg_name(self):
        return self.driver.find_elements(*Dataentery.name)

    #def veg_quantity(self):
      #return self.find_element(*Vegetable.quantity)

    #def veg_addtocart(self):
       #return self.driver.find_elements(*Vegetable.addtocart)

    def form_name(self):
        return self.driver.find_element(*Dataentery.formname)

    def form_email(self):
        return self.driver.find_element(*Dataentery.email)

    def form_password(self):
        return self.driver.find_element(*Dataentery.password)

    def form_dob(self):
        return self.driver.find_element(*Dataentery.dob)

    def form_gender(self):
        return self.driver.find_element(*Dataentery.gender)

    def form_submit(self):
        return self.driver.find_element(*Dataentery.submit)

    def form_conform(self):
        return self.driver.find_element(*Dataentery.conformation)