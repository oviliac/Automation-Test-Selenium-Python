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

class TestCart1(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions() 
        options.add_argument("--headless")
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    def _login(self):
        # login action, use for multiple call
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/login")
        driver.find_element(By.ID, "Email").send_keys("awqqhjd@xsasai.com")
        driver.find_element(By.ID, "Password").send_keys("1234567")
        driver.find_element(By.ID, "RememberMe").click()
        driver.find_element(By.CSS_SELECTOR, ".button-1.login-button[type=submit]").click()
        self.assertEqual(driver.current_url, "https://demowebshop.tricentis.com/")
        data = driver.find_element(By.CSS_SELECTOR, ".header-links > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)").text
        self.assertEqual("awqqhjd@xsasai.com", data)
        return driver
    
    def _clear_cart(self, driver):
        driver.get("https://demowebshop.tricentis.com/cart")
        for el in driver.find_elements(By.CSS_SELECTOR, ".remove-from-cart input[type='checkbox']"):
            el.click()
        driver.find_element(By.CSS_SELECTOR, ".update-cart-button").click()

    def test_01_cart_add_product_to_the_cart(self):
        driver = self._login()
        try:
            driver.get("https://demowebshop.tricentis.com/")
            item_count = driver.find_element(By.CSS_SELECTOR, ".cart-qty").text
            self.assertEqual("(0)", item_count)
            # select product 31
            driver.find_element(By.CSS_SELECTOR, "div.item-box .product-item[data-productid='31'] .details .add-info .buttons input[type=button]").click()
            # get product price
            product_price = driver.find_element(By.CSS_SELECTOR, "div.item-box .product-item[data-productid='31'] .details .add-info .prices .price.actual-price").text

            # wait unitl notification product added
            notification = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#bar-notification"))).text
            self.assertEqual("The product has been added to your shopping cart", notification.strip())

            # check chart count is 1
            item_count = driver.find_element(By.CSS_SELECTOR, ".cart-qty").text
            self.assertEqual("(1)", item_count)
            
            # cart page
            driver.get("https://demowebshop.tricentis.com/cart")
            
            # check cart item quantity is 1
            cart_count_detail = driver.find_element(By.CSS_SELECTOR, "tbody .cart-item-row .qty-input").get_attribute('value')
            self.assertEqual("1", cart_count_detail)
            
            # check cart item sub-total equals product_price
            cart_sub_total = driver.find_element(By.CSS_SELECTOR, "tbody .cart-item-row .product-subtotal").text
            self.assertEqual(product_price, cart_sub_total)
        finally:
            self._clear_cart(driver)
    
    def test_02_cart_add_multiple_same_products_to_cart(self):
        driver = self._login()
        try:
            driver.get("https://demowebshop.tricentis.com/")
            item_count = driver.find_element(By.CSS_SELECTOR, ".cart-qty").text
            self.assertEqual("(0)", item_count)
            # select product 31
            driver.find_element(By.CSS_SELECTOR, "div.item-box .product-item[data-productid='31'] .details .add-info .buttons input[type=button]").click()
            # get product price
            product_price = driver.find_element(By.CSS_SELECTOR, "div.item-box .product-item[data-productid='31'] .details .add-info .prices .price.actual-price").text

            # wait unitl notification product added
            notification = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#bar-notification"))).text
            self.assertEqual("The product has been added to your shopping cart", notification.strip())

            # check chart count is 1
            item_count = driver.find_element(By.CSS_SELECTOR, ".cart-qty").text
            self.assertEqual("(1)", item_count)
            
            # cart page
            driver.get("https://demowebshop.tricentis.com/cart")
            
            # check cart item quantity is 1
            cart_count_detail = driver.find_element(By.CSS_SELECTOR, "tbody .cart-item-row .qty-input").get_attribute('value')
            self.assertEqual("1", cart_count_detail)

            # change quantity to 2
            driver.find_element(By.CSS_SELECTOR, "tbody .cart-item-row .qty-input").clear()
            driver.find_element(By.CSS_SELECTOR, "tbody .cart-item-row .qty-input").send_keys(2)
            driver.find_element(By.CSS_SELECTOR, ".update-cart-button").click()
            
            # check cart item sub-total equals double of product_price
            cart_sub_total = driver.find_element(By.CSS_SELECTOR, "tbody .cart-item-row .product-subtotal").text
            self.assertEqual(float(product_price) * 2, float(cart_sub_total))
        finally:
            self._clear_cart(driver)

    def test_03_cart_add_several_different_products_to_the_cart(self):
        driver = self._login()
        try:
            driver.get("https://demowebshop.tricentis.com/")
            item_count = driver.find_element(By.CSS_SELECTOR, ".cart-qty").text
            self.assertEqual("(0)", item_count)
            # select product 31
            driver.find_element(By.CSS_SELECTOR, "div.item-box .product-item[data-productid='31'] .details .add-info .buttons input[type=button]").click()
            # get product price
            product_price_1 = driver.find_element(By.CSS_SELECTOR, "div.item-box .product-item[data-productid='31'] .details .add-info .prices .price.actual-price").text

            # wait unitl notification product added
            notification = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#bar-notification"))).text
            self.assertEqual("The product has been added to your shopping cart", notification.strip())

            # check chart count is 1
            item_count = driver.find_element(By.CSS_SELECTOR, ".cart-qty").text
            self.assertEqual("(1)", item_count)

            # select product 72
            product_price_2 = driver.find_element(By.CSS_SELECTOR, "div.item-box .product-item[data-productid='72'] .details .add-info .prices .price.actual-price").text
            driver.find_element(By.CSS_SELECTOR, "div.item-box .product-item[data-productid='72'] .details .add-info .buttons input[type=button]").click()
            product_2 = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-name > h1:nth-child(1)"))).text
            self.assertEqual("Build your own cheap computer", product_2)

            driver.find_element(By.CSS_SELECTOR, "#product_attribute_72_5_18_52").click()
            driver.find_element(By.CSS_SELECTOR, "#add-to-cart-button-72").click()

            notification = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#bar-notification"))).text
            self.assertEqual("The product has been added to your shopping cart", notification.strip())

            # check chart count is 2
            item_count = driver.find_element(By.CSS_SELECTOR, ".cart-qty").text
            self.assertEqual("(2)", item_count)
            
            # cart page
            driver.get("https://demowebshop.tricentis.com/cart")
            
            # check cart item quantity is 1
            cart_count_detail = driver.find_element(By.CSS_SELECTOR, "tr.cart-item-row:nth-child(1) .qty-input").get_attribute('value')
            self.assertEqual("1", cart_count_detail)

            cart_count_detail = driver.find_element(By.CSS_SELECTOR, "tr.cart-item-row:nth-child(2) .qty-input").get_attribute('value')
            self.assertEqual("1", cart_count_detail)

            # check cart item sub-total equals double of product_price_1
            cart_sub_total = driver.find_element(By.CSS_SELECTOR, "tr.cart-item-row:nth-child(1) .product-subtotal").text
            self.assertEqual(product_price_1, cart_sub_total)
            cart_sub_total = driver.find_element(By.CSS_SELECTOR, "tr.cart-item-row:nth-child(2) .product-subtotal").text
            self.assertEqual(product_price_2, cart_sub_total)
        finally:
            self._clear_cart(driver)


    def test_05_checkout_multiple_products_without_agree_tos(self):
        driver = self._login()
        try:
            driver.get("https://demowebshop.tricentis.com/")
            item_count = driver.find_element(By.CSS_SELECTOR, ".cart-qty").text
            self.assertEqual("(0)", item_count)
            # select product 31
            driver.find_element(By.CSS_SELECTOR, "div.item-box .product-item[data-productid='31'] .details .add-info .buttons input[type=button]").click()
            # get product price
            product_price_1 = driver.find_element(By.CSS_SELECTOR, "div.item-box .product-item[data-productid='31'] .details .add-info .prices .price.actual-price").text

            # wait unitl notification product added
            notification = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#bar-notification"))).text
            self.assertEqual("The product has been added to your shopping cart", notification.strip())

            # check chart count is 1
            item_count = driver.find_element(By.CSS_SELECTOR, ".cart-qty").text
            self.assertEqual("(1)", item_count)

            # select product 72
            product_price_2 = driver.find_element(By.CSS_SELECTOR, "div.item-box .product-item[data-productid='72'] .details .add-info .prices .price.actual-price").text
            driver.find_element(By.CSS_SELECTOR, "div.item-box .product-item[data-productid='72'] .details .add-info .buttons input[type=button]").click()
            product_2 = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-name > h1:nth-child(1)"))).text
            self.assertEqual("Build your own cheap computer", product_2)

            driver.find_element(By.CSS_SELECTOR, "#product_attribute_72_5_18_52").click()
            driver.find_element(By.CSS_SELECTOR, "#add-to-cart-button-72").click()

            notification = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#bar-notification"))).text
            self.assertEqual("The product has been added to your shopping cart", notification.strip())

            # check chart count is 2
            item_count = driver.find_element(By.CSS_SELECTOR, ".cart-qty").text
            self.assertEqual("(2)", item_count)
            
            # cart page
            driver.get("https://demowebshop.tricentis.com/cart")
            
            # check cart item quantity is 1
            cart_count_detail = driver.find_element(By.CSS_SELECTOR, "tr.cart-item-row:nth-child(1) .qty-input").get_attribute('value')
            self.assertEqual("1", cart_count_detail)

            cart_count_detail = driver.find_element(By.CSS_SELECTOR, "tr.cart-item-row:nth-child(2) .qty-input").get_attribute('value')
            self.assertEqual("1", cart_count_detail)

            # check cart item sub-total equals double of product_price_1
            cart_sub_total = driver.find_element(By.CSS_SELECTOR, "tr.cart-item-row:nth-child(1) .product-subtotal").text
            self.assertEqual(product_price_1, cart_sub_total)
            cart_sub_total = driver.find_element(By.CSS_SELECTOR, "tr.cart-item-row:nth-child(2) .product-subtotal").text
            self.assertEqual(product_price_2, cart_sub_total)

            # checkout 
            driver.find_element(By.CSS_SELECTOR, "#checkout").click()
            alert = driver.find_element(By.CSS_SELECTOR, "#terms-of-service-warning-box")
            self.assertTrue(alert.is_displayed)
            self.assertEqual("Please accept the terms of service before the next step.", alert.text)
        finally:
            self._clear_cart(driver)


    def test_06_checkout_multiple_products_agree_tos(self):
        driver = self._login()
        try:
            driver.get("https://demowebshop.tricentis.com/")
            item_count = driver.find_element(By.CSS_SELECTOR, ".cart-qty").text
            self.assertEqual("(0)", item_count)
            # select product 31
            driver.find_element(By.CSS_SELECTOR, "div.item-box .product-item[data-productid='31'] .details .add-info .buttons input[type=button]").click()
            # get product price
            product_price_1 = driver.find_element(By.CSS_SELECTOR, "div.item-box .product-item[data-productid='31'] .details .add-info .prices .price.actual-price").text

            # wait unitl notification product added
            notification = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#bar-notification"))).text
            self.assertEqual("The product has been added to your shopping cart", notification.strip())

            # check chart count is 1
            item_count = driver.find_element(By.CSS_SELECTOR, ".cart-qty").text
            self.assertEqual("(1)", item_count)

            # select product 72
            product_price_2 = driver.find_element(By.CSS_SELECTOR, "div.item-box .product-item[data-productid='72'] .details .add-info .prices .price.actual-price").text
            driver.find_element(By.CSS_SELECTOR, "div.item-box .product-item[data-productid='72'] .details .add-info .buttons input[type=button]").click()
            product_2 = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-name > h1:nth-child(1)"))).text
            self.assertEqual("Build your own cheap computer", product_2)

            driver.find_element(By.CSS_SELECTOR, "#product_attribute_72_5_18_52").click()
            driver.find_element(By.CSS_SELECTOR, "#add-to-cart-button-72").click()

            notification = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#bar-notification"))).text
            self.assertEqual("The product has been added to your shopping cart", notification.strip())

            # check chart count is 2
            item_count = driver.find_element(By.CSS_SELECTOR, ".cart-qty").text
            self.assertEqual("(2)", item_count)
            
            # cart page
            driver.get("https://demowebshop.tricentis.com/cart")
            
            # check cart item quantity is 1
            cart_count_detail = driver.find_element(By.CSS_SELECTOR, "tr.cart-item-row:nth-child(1) .qty-input").get_attribute('value')
            self.assertEqual("1", cart_count_detail)

            cart_count_detail = driver.find_element(By.CSS_SELECTOR, "tr.cart-item-row:nth-child(2) .qty-input").get_attribute('value')
            self.assertEqual("1", cart_count_detail)

            # check cart item sub-total equals double of product_price_1
            cart_sub_total = driver.find_element(By.CSS_SELECTOR, "tr.cart-item-row:nth-child(1) .product-subtotal").text
            self.assertEqual(product_price_1, cart_sub_total)
            cart_sub_total = driver.find_element(By.CSS_SELECTOR, "tr.cart-item-row:nth-child(2) .product-subtotal").text
            self.assertEqual(product_price_2, cart_sub_total)

            # accept tos
            driver.find_element(By.CSS_SELECTOR, "#termsofservice").click()

            # checkout 
            driver.find_element(By.CSS_SELECTOR, "#checkout").click()
            
            self.assertEqual("https://demowebshop.tricentis.com/onepagecheckout", driver.current_url)
        finally:
            self._clear_cart(driver)

if __name__ == "__main__":
    unittest.main()