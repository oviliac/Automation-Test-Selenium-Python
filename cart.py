import time
import pytest
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

from data import DataLogin
from locator import LoginPage, CartPage, HomePage

class TestCart1(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions() 
        options.add_argument("--headless")
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    def _login(self):
        # login action, use for multiple call
        driver = self.browser
        driver.get(f"{DataLogin.baseURL}login")
        driver.find_element(By.ID, LoginPage.email).send_keys(DataLogin.email)
        driver.find_element(By.ID, LoginPage.password).send_keys(DataLogin.password)
        driver.find_element(By.ID, LoginPage.rememberme).click()
        driver.find_element(By.CSS_SELECTOR, LoginPage.login_button).click()
        self.assertEqual(driver.current_url, DataLogin.baseURL)
        data = driver.find_element(By.CSS_SELECTOR, LoginPage.profile_info).text
        self.assertEqual(DataLogin.email, data)
        return driver
    
    def _clear_cart(self, driver):
        driver.get(f"{DataLogin.baseURL}cart")
        for el in driver.find_elements(By.CSS_SELECTOR, CartPage.cart_item_checkbox):
            el.click()
        driver.find_element(By.CSS_SELECTOR, CartPage.update_cart_button).click()

    def test_01_cart_add_product_to_the_cart(self):
        driver = self._login()
        try:
            driver.get(f"{DataLogin.baseURL}")
            item_count = driver.find_element(By.CSS_SELECTOR, HomePage.cart_qty).text
            self.assertEqual("(0)", item_count)
            # select product 31
            driver.find_element(By.CSS_SELECTOR, HomePage.product_31).click()
            # get product price
            product_price = driver.find_element(By.CSS_SELECTOR, HomePage.product_31_price).text

            # wait unitl notification product added
            notification = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, HomePage.notification))).text
            self.assertEqual("The product has been added to your shopping cart", notification.strip())

            # check chart count is 1
            item_count = driver.find_element(By.CSS_SELECTOR, HomePage.cart_qty).text
            self.assertEqual("(1)", item_count)
            
            # cart page
            driver.get(f"{DataLogin.baseURL}cart")
            
            # check cart item quantity is 1
            cart_count_detail = driver.find_element(By.CSS_SELECTOR, CartPage.cart_single_product_qty).get_attribute('value')
            self.assertEqual("1", cart_count_detail)
            
            # check cart item sub-total equals product_price
            cart_sub_total = driver.find_element(By.CSS_SELECTOR, CartPage.cart_single_product_subtotal).text
            self.assertEqual(product_price, cart_sub_total)
        finally:
            self._clear_cart(driver)
    
    def test_02_cart_add_multiple_same_products_to_cart(self):
        driver = self._login()
        try:
            driver.get(f"{DataLogin.baseURL}")
            item_count = driver.find_element(By.CSS_SELECTOR, HomePage.cart_qty).text
            self.assertEqual("(0)", item_count)
            # select product 31
            driver.find_element(By.CSS_SELECTOR, HomePage.product_31).click()
            # get product price
            product_price = driver.find_element(By.CSS_SELECTOR, HomePage.product_31_price).text

            # wait unitl notification product added
            notification = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, HomePage.notification))).text
            self.assertEqual("The product has been added to your shopping cart", notification.strip())

            # check chart count is 1
            item_count = driver.find_element(By.CSS_SELECTOR, HomePage.cart_qty).text
            self.assertEqual("(1)", item_count)
            
            # cart page
            driver.get(f"{DataLogin.baseURL}cart")
            
            # check cart item quantity is 1
            cart_count_detail = driver.find_element(By.CSS_SELECTOR, CartPage.cart_single_product_qty).get_attribute('value')
            self.assertEqual("1", cart_count_detail)

            # change quantity to 2
            driver.find_element(By.CSS_SELECTOR, CartPage.cart_single_product_qty).clear()
            driver.find_element(By.CSS_SELECTOR, CartPage.cart_single_product_qty).send_keys(2)
            driver.find_element(By.CSS_SELECTOR, CartPage.update_cart_button).click()
            
            # check cart item sub-total equals double of product_price
            cart_sub_total = driver.find_element(By.CSS_SELECTOR, CartPage.cart_single_product_subtotal).text
            self.assertEqual(float(product_price) * 2, float(cart_sub_total))
        finally:
            self._clear_cart(driver)

    def test_03_cart_add_several_different_products_to_the_cart(self):
        driver = self._login()
        try:
            driver.get(f"{DataLogin.baseURL}")
            item_count = driver.find_element(By.CSS_SELECTOR, HomePage.cart_qty).text
            self.assertEqual("(0)", item_count)
            # select product 31
            driver.find_element(By.CSS_SELECTOR, HomePage.product_31).click()
            # get product price
            product_price_1 = driver.find_element(By.CSS_SELECTOR, HomePage.product_31_price).text

            # wait unitl notification product added
            notification = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, HomePage.notification))).text
            self.assertEqual("The product has been added to your shopping cart", notification.strip())

            # check chart count is 1
            item_count = driver.find_element(By.CSS_SELECTOR, HomePage.cart_qty).text
            self.assertEqual("(1)", item_count)

            # select product 72
            product_price_2 = driver.find_element(By.CSS_SELECTOR, HomePage.product_72_price).text
            driver.find_element(By.CSS_SELECTOR, HomePage.product_72).click()
            product_2 = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, HomePage.product_72_title))).text
            self.assertEqual("Build your own cheap computer", product_2)

            driver.find_element(By.CSS_SELECTOR, HomePage.product_72_cpu_option).click()
            driver.find_element(By.CSS_SELECTOR, HomePage.product_72_add_cart).click()

            notification = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, HomePage.notification))).text
            self.assertEqual("The product has been added to your shopping cart", notification.strip())

            # check chart count is 2
            item_count = driver.find_element(By.CSS_SELECTOR, HomePage.cart_qty).text
            self.assertEqual("(2)", item_count)
            
            # cart page
            driver.get(f"{DataLogin.baseURL}cart")
            
            # check cart item quantity is 1
            cart_count_detail = driver.find_element(By.CSS_SELECTOR, CartPage.cart_multi_product_qty_1).get_attribute('value')
            self.assertEqual("1", cart_count_detail)

            cart_count_detail = driver.find_element(By.CSS_SELECTOR, CartPage.cart_multi_product_qty_2).get_attribute('value')
            self.assertEqual("1", cart_count_detail)

            # check cart item sub-total equals double of product_price_1
            cart_sub_total = driver.find_element(By.CSS_SELECTOR, CartPage.cart_multi_product_subtotal_1).text
            self.assertEqual(product_price_1, cart_sub_total)
            cart_sub_total = driver.find_element(By.CSS_SELECTOR, CartPage.cart_multi_product_subtotal_2).text
            self.assertEqual(product_price_2, cart_sub_total)
        finally:
            self._clear_cart(driver)


    def test_05_checkout_multiple_products_without_agree_tos(self):
        driver = self._login()
        try:
            driver.get(f"{DataLogin.baseURL}")
            item_count = driver.find_element(By.CSS_SELECTOR, HomePage.cart_qty).text
            self.assertEqual("(0)", item_count)
            # select product 31
            driver.find_element(By.CSS_SELECTOR, HomePage.product_31).click()
            # get product price
            product_price_1 = driver.find_element(By.CSS_SELECTOR, HomePage.product_31_price).text

            # wait unitl notification product added
            notification = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, HomePage.notification))).text
            self.assertEqual("The product has been added to your shopping cart", notification.strip())

            # check chart count is 1
            item_count = driver.find_element(By.CSS_SELECTOR, HomePage.cart_qty).text
            self.assertEqual("(1)", item_count)

            # select product 72
            product_price_2 = driver.find_element(By.CSS_SELECTOR, HomePage.product_72_price).text
            driver.find_element(By.CSS_SELECTOR, HomePage.product_72).click()
            product_2 = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, HomePage.product_72_title))).text
            self.assertEqual("Build your own cheap computer", product_2)

            driver.find_element(By.CSS_SELECTOR, HomePage.product_72_cpu_option).click()
            driver.find_element(By.CSS_SELECTOR, HomePage.product_72_add_cart).click()

            notification = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, HomePage.notification))).text
            self.assertEqual("The product has been added to your shopping cart", notification.strip())

            # check chart count is 2
            item_count = driver.find_element(By.CSS_SELECTOR, HomePage.cart_qty).text
            self.assertEqual("(2)", item_count)
            
            # cart page
            driver.get(f"{DataLogin.baseURL}cart")
            
            # check cart item quantity is 1
            cart_count_detail = driver.find_element(By.CSS_SELECTOR, CartPage.cart_multi_product_qty_1).get_attribute('value')
            self.assertEqual("1", cart_count_detail)

            cart_count_detail = driver.find_element(By.CSS_SELECTOR, CartPage.cart_multi_product_qty_2).get_attribute('value')
            self.assertEqual("1", cart_count_detail)

            # check cart item sub-total equals double of product_price_1
            cart_sub_total = driver.find_element(By.CSS_SELECTOR, CartPage.cart_multi_product_subtotal_1).text
            self.assertEqual(product_price_1, cart_sub_total)
            cart_sub_total = driver.find_element(By.CSS_SELECTOR, CartPage.cart_multi_product_subtotal_2).text
            self.assertEqual(product_price_2, cart_sub_total)

            # checkout 
            driver.find_element(By.CSS_SELECTOR, CartPage.checkout_button).click()
            alert = driver.find_element(By.CSS_SELECTOR, CartPage.alert_box)
            self.assertTrue(alert.is_displayed)
            self.assertEqual("Please accept the terms of service before the next step.", alert.text)
        finally:
            self._clear_cart(driver)


    def test_06_checkout_multiple_products_agree_tos(self):
        driver = self._login()
        try:
            driver.get(f"{DataLogin.baseURL}")
            item_count = driver.find_element(By.CSS_SELECTOR, HomePage.cart_qty).text
            self.assertEqual("(0)", item_count)
            # select product 31
            driver.find_element(By.CSS_SELECTOR, HomePage.product_31).click()
            # get product price
            product_price_1 = driver.find_element(By.CSS_SELECTOR, HomePage.product_31_price).text

            # wait unitl notification product added
            notification = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, HomePage.notification))).text
            self.assertEqual("The product has been added to your shopping cart", notification.strip())

            # check chart count is 1
            item_count = driver.find_element(By.CSS_SELECTOR, HomePage.cart_qty).text
            self.assertEqual("(1)", item_count)

            # select product 72
            product_price_2 = driver.find_element(By.CSS_SELECTOR, HomePage.product_72_price).text
            driver.find_element(By.CSS_SELECTOR, HomePage.product_72).click()
            product_2 = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, HomePage.product_72_title))).text
            self.assertEqual("Build your own cheap computer", product_2)

            driver.find_element(By.CSS_SELECTOR, HomePage.product_72_cpu_option).click()
            driver.find_element(By.CSS_SELECTOR, HomePage.product_72_add_cart).click()

            notification = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, HomePage.notification))).text
            self.assertEqual("The product has been added to your shopping cart", notification.strip())

            # check chart count is 2
            item_count = driver.find_element(By.CSS_SELECTOR, HomePage.cart_qty).text
            self.assertEqual("(2)", item_count)
            
            # cart page
            driver.get(f"{DataLogin.baseURL}cart")
            
            # check cart item quantity is 1
            cart_count_detail = driver.find_element(By.CSS_SELECTOR, CartPage.cart_multi_product_qty_1).get_attribute('value')
            self.assertEqual("1", cart_count_detail)

            cart_count_detail = driver.find_element(By.CSS_SELECTOR, CartPage.cart_multi_product_qty_2).get_attribute('value')
            self.assertEqual("1", cart_count_detail)

            # check cart item sub-total equals double of product_price_1
            cart_sub_total = driver.find_element(By.CSS_SELECTOR, CartPage.cart_multi_product_subtotal_1).text
            self.assertEqual(product_price_1, cart_sub_total)
            cart_sub_total = driver.find_element(By.CSS_SELECTOR, CartPage.cart_multi_product_subtotal_2).text
            self.assertEqual(product_price_2, cart_sub_total)

            # accept tos
            driver.find_element(By.CSS_SELECTOR, CartPage.accept_tos).click()

            # checkout 
            driver.find_element(By.CSS_SELECTOR, CartPage.checkout_button).click()
            
            self.assertEqual(f"{DataLogin.baseURL}onepagecheckout", driver.current_url)
        finally:
            self._clear_cart(driver)

if __name__ == "__main__":
    unittest.main()