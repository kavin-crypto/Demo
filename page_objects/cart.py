from selenium.webdriver.common.by import By

from page_objects.checkout import CheckOut


class Bag():
    cart_icon = (By.XPATH,"//img[@alt='Cart']")
    conformation = (By.XPATH,"//*[contains(@class,'cart-preview')]/div//li/div[1]/p[1]")
    checkout = (By.XPATH,"//*[contains(@class,'action-block')]/button")

    def __init__(self, driver):
        self.driver = driver

    def cart_bag(self):
        return self.driver.find_element(*Bag.cart_icon)

    def cart_conformation(self):
        return self.driver.find_element(*Bag.conformation)

    def cart_checkout(self):
         self.driver.find_element(*Bag.checkout).click()
         checkout = CheckOut(self.driver)
         return checkout

