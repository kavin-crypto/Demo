from selenium.webdriver.common.by import By


class Dataentery:

    name = (By.XPATH, "//*[contains(@class,'product')]/h4")
    # quantity = (By.XPATH, "parent ::div/div[2]/a[2]")
    # addtocart = (By.XPATH, "parent ::div/div[3]/button")


    def __init__(self, driver):
        self.driver = driver

    def veg_name(self):
        return self.driver.find_elements(*Dataentery.name)

    #def veg_quantity(self):
      #return self.find_element(*Vegetable.quantity)

    #def veg_addtocart(self):
       #return self.driver.find_elements(*Vegetable.addtocart)
