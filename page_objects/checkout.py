from selenium.webdriver.common.by import By

from page_objects.conformation import ConformationPg


class CheckOut:
    promocode = (By.XPATH,"//*[contains(@class,'promoCode')]")
    apply = (By.XPATH,"//*[contains(@class,'promoBtn')]")
    conform=(By.CSS_SELECTOR,".promoWrapper span")
    tamount=(By.XPATH,"//*[contains(@class,'totAmt')]")
    discount=(By.XPATH,"//*[contains(@class,'discountAmt')]")
    placeorder=(By.XPATH,"//*[contains(text(),'Place Order')]")

    def __init__(self,driver):
        self.driver = driver

    def check_promocode(self):
        return self.driver.find_element(*CheckOut.promocode)

    def check_apply(self):
        return self.driver.find_element(*CheckOut.apply)

    def check_conform(self):
        return self.driver.find_element(*CheckOut.conform)

    def check_tamount(self):
        return self.driver.find_element(*CheckOut.tamount)

    def check_discount(self):
        return self.driver.find_element(*CheckOut.discount)

    def check_placeorder(self):
        self.driver.find_element(*CheckOut.placeorder).click()
        delivery = ConformationPg(self.driver)
        return delivery
