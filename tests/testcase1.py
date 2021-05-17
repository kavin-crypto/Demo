import time

from page_objects.cart import Bag
from page_objects.name_selection import Dataentery
from page_objects.pageselection import PgSelect
from utilities.bassclass import BassClass


class TestRun(BassClass):

    def test_cart(self,textdata):
        log = self.getLogger()
        vegetable = Dataentery(self.driver)
        bag = Bag(self.driver)

        #self.wait("//*[contains(text(),'Automation Practise - 1')]")
        #vegetable = page.select_pg1()

        # veg_selection
        veg = vegetable.veg_name()
        log.info("selected fruits or vegetable is "+textdata["name"])

        for i in veg:
            if i.text == textdata["name"]:
                i.find_element_by_xpath("parent ::div/div[2]/a[2]").click()
                i.find_element_by_xpath("parent ::div/div[3]/button").click()
                break

        # cart
        bag.cart_bag().click()
        assert textdata["name"] == bag.cart_conformation().text
        checkout = bag.cart_checkout()

        self.wait("//input[contains(@class,'promoCode')]")

        # checkout
        checkout.check_promocode().send_keys("rahulshettyacademy")
        checkout.check_apply().click()
        ui = checkout.check_conform().text
        assert ui in "Code applied ..!"
        total_amount = checkout.check_tamount().text
        log.info("Total amount is " + total_amount)
        time.sleep(5)
        after_discount = checkout.check_discount().text
        log.info("Discount amount is "+after_discount)
        assert not total_amount == after_discount

        delivery = checkout.check_placeorder()

        # delivery
        delivery.del_country_selection().click()
        country = delivery.del_country_name()
        log.info("Selected country is "+textdata["Country"])
        for con in country:
            if con.text == textdata["Country"]:
                con.click()

        delivery.del_click().click()
        delivery.del_checkbox().click()
        delivery.del_proceed().click()
        log.info("text received from confrom pg is " + delivery.del_conformation().text )
        assert "Thank you" in delivery.del_conformation().text
        log.info("Firstrun is over")
        time.sleep(5)
