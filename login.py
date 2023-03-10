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
from data import DataLogin

class TestLogin(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions() 
        options.add_argument("--headless")
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def test_01_success_login(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/login")
        driver.find_element(By.ID, "Email").send_keys(DataLogin.email)
        driver.find_element(By.ID, "Password").send_keys(DataLogin.password)
        driver.find_element(By.ID, "RememberMe").click()
        driver.find_element(By.CSS_SELECTOR, ".button-1.login-button[type=submit]").click()
        self.assertEqual(driver.current_url, "https://demowebshop.tricentis.com/")
        data = driver.find_element(By.CSS_SELECTOR, ".header-links > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)").text
        self.assertEqual("oviliach123@gmail.com", data)

    def test_02_invalid_username_and_password(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/login")
        driver.find_element(By.ID, "Email").send_keys("awqqhj@xsasai.com")
        driver.find_element(By.ID, "Password").send_keys("1234567a")
        driver.find_element(By.CSS_SELECTOR, ".button-1.login-button[type=submit]").click()
        error1 = driver.find_element(By.CSS_SELECTOR, ".validation-summary-errors > span:nth-child(1)").text
        error2 = driver.find_element(By.CSS_SELECTOR, ".validation-summary-errors > ul:nth-child(2) > li:nth-child(1)").text
        self.assertEqual("Login was unsuccessful. Please correct the errors and try again.", error1)
        self.assertEqual("No customer account found", error2)

    def test_03_invalid_username_and_valid_password(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/login")
        driver.find_element(By.ID, "Email").send_keys("awqqhj@xsasai.com")
        driver.find_element(By.ID, "Password").send_keys(DataLogin.password)
        driver.find_element(By.CSS_SELECTOR, ".button-1.login-button[type=submit]").click()
        error1 = driver.find_element(By.CSS_SELECTOR, ".validation-summary-errors > span:nth-child(1)").text
        error2 = driver.find_element(By.CSS_SELECTOR, ".validation-summary-errors > ul:nth-child(2) > li:nth-child(1)").text
        self.assertEqual("Login was unsuccessful. Please correct the errors and try again.", error1)
        self.assertEqual("No customer account found", error2)
        
    def test_04_valid_username_and_invalid_password(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/login")
        driver.find_element(By.ID, "Email").send_keys(DataLogin.email)
        driver.find_element(By.ID, "Password").send_keys("12345")
        driver.find_element(By.CSS_SELECTOR, ".button-1.login-button[type=submit]").click()
        error1 = driver.find_element(By.CSS_SELECTOR, ".validation-summary-errors > span:nth-child(1)").text
        error2 = driver.find_element(By.CSS_SELECTOR, ".validation-summary-errors > ul:nth-child(2) > li:nth-child(1)").text
        self.assertEqual("Login was unsuccessful. Please correct the errors and try again.", error1)
        self.assertEqual("The credentials provided are incorrect", error2)

    def test_05_empty_email(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/login")
        driver.find_element(By.ID, "Email").send_keys("")
        driver.find_element(By.ID, "Password").send_keys(DataLogin.password)
        driver.find_element(By.CSS_SELECTOR, ".button-1.login-button[type=submit]").click()
        error1 = driver.find_element(By.CSS_SELECTOR, ".validation-summary-errors > span:nth-child(1)").text
        error2 = driver.find_element(By.CSS_SELECTOR, ".validation-summary-errors > ul:nth-child(2) > li:nth-child(1)").text
        self.assertEqual("Login was unsuccessful. Please correct the errors and try again.", error1)
        self.assertEqual("No customer account found", error2)

    def test_06_empty_password(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/login")
        driver.find_element(By.ID, "Email").send_keys(DataLogin.email)
        driver.find_element(By.ID, "Password").send_keys("")
        driver.find_element(By.CSS_SELECTOR, ".button-1.login-button[type=submit]").click()
        error1 = driver.find_element(By.CSS_SELECTOR, ".validation-summary-errors > span:nth-child(1)").text
        error2 = driver.find_element(By.CSS_SELECTOR, ".validation-summary-errors > ul:nth-child(2) > li:nth-child(1)").text
        self.assertEqual("Login was unsuccessful. Please correct the errors and try again.", error1)
        self.assertEqual("The credentials provided are incorrect", error2)

    def test_07_empty_email_and_password(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/login")
        driver.find_element(By.ID, "Email").send_keys("")
        driver.find_element(By.ID, "Password").send_keys("")
        driver.find_element(By.CSS_SELECTOR, ".button-1.login-button[type=submit]").click()
        error1 = driver.find_element(By.CSS_SELECTOR, ".validation-summary-errors > span:nth-child(1)").text
        error2 = driver.find_element(By.CSS_SELECTOR, ".validation-summary-errors > ul:nth-child(2) > li:nth-child(1)").text
        self.assertEqual("Login was unsuccessful. Please correct the errors and try again.", error1)
        self.assertEqual("No customer account found", error2)

    def test_08_activated_remember_me(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/login")
        driver.find_element(By.ID, "Email").send_keys(DataLogin.email)
        driver.find_element(By.ID, "Password").send_keys(DataLogin.password)
        driver.find_element(By.ID, "RememberMe").click()
        driver.find_element(By.CSS_SELECTOR, ".button-1.login-button[type=submit]").click()
        self.assertEqual(driver.current_url, "https://demowebshop.tricentis.com/")
        data = driver.find_element(By.CSS_SELECTOR, ".header-links > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)").text
        self.assertEqual("oviliach123@gmail.com", data)

    def test_09_unactivated_remember_me(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/login")
        driver.find_element(By.ID, "Email").send_keys(DataLogin.email)
        driver.find_element(By.ID, "Password").send_keys(DataLogin.password)
        driver.find_element(By.CSS_SELECTOR, ".button-1.login-button[type=submit]").click()
        self.assertEqual(driver.current_url, "https://demowebshop.tricentis.com/")
        data = driver.find_element(By.CSS_SELECTOR, ".header-links > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)").text
        self.assertEqual("oviliach123@gmail.com", data)
    
    def test_10_forgot_password(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/login")
        driver.find_element(By.CSS_SELECTOR, ".forgot-password > a:nth-child(1)").click()
        self.assertEqual(driver.current_url, "https://demowebshop.tricentis.com/passwordrecovery")
        data = driver.find_element(By.CSS_SELECTOR, ".page-title > h1:nth-child(1)").text
        self.assertEqual("Password recovery", data)
        driver.find_element(By.ID, "Email").send_keys(DataLogin.email)
        driver.find_element(By.CSS_SELECTOR, ".password-recovery-button[type=submit]").click()
        data = driver.find_element(By.CSS_SELECTOR, ".result").text
        self.assertEqual("Email with instructions has been sent to you.", data)


if __name__ == "__main__":
    unittest.main()
