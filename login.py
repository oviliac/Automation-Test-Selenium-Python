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
from locator import LoginPage, RecoveryPage

class TestLogin(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions() 
        options.add_argument("--headless")
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def test_01_success_login(self):
        driver = self.browser
        driver.get(f"{DataLogin.baseURL}login")
        driver.find_element(By.ID, LoginPage.email).send_keys(DataLogin.email)
        driver.find_element(By.ID, LoginPage.password).send_keys(DataLogin.password)
        driver.find_element(By.ID, LoginPage.rememberme).click()
        driver.find_element(By.CSS_SELECTOR, LoginPage.login_button).click()
        self.assertEqual(driver.current_url, DataLogin.baseURL)
        data = driver.find_element(By.CSS_SELECTOR, LoginPage.profile_info).text
        self.assertEqual(DataLogin.email, data)

    def test_02_invalid_username_and_password(self):
        driver = self.browser
        driver.get(f"{DataLogin.baseURL}login")
        driver.find_element(By.ID, LoginPage.email).send_keys("awqqhj@xsasai.com")
        driver.find_element(By.ID, LoginPage.password).send_keys("1234567a")
        driver.find_element(By.CSS_SELECTOR, LoginPage.login_button).click()
        error1 = driver.find_element(By.CSS_SELECTOR, LoginPage.error_summary).text
        error2 = driver.find_element(By.CSS_SELECTOR, LoginPage.error_summary_detail).text
        self.assertEqual("Login was unsuccessful. Please correct the errors and try again.", error1)
        self.assertEqual("No customer account found", error2)

    def test_03_invalid_username_and_valid_password(self):
        driver = self.browser
        driver.get(f"{DataLogin.baseURL}login")
        driver.find_element(By.ID, LoginPage.email).send_keys("awqqhj@xsasai.com")
        driver.find_element(By.ID, LoginPage.password).send_keys(DataLogin.password)
        driver.find_element(By.CSS_SELECTOR, LoginPage.login_button).click()
        error1 = driver.find_element(By.CSS_SELECTOR, LoginPage.error_summary).text
        error2 = driver.find_element(By.CSS_SELECTOR, LoginPage.error_summary_detail).text
        self.assertEqual("Login was unsuccessful. Please correct the errors and try again.", error1)
        self.assertEqual("No customer account found", error2)
        
    def test_04_valid_username_and_invalid_password(self):
        driver = self.browser
        driver.get(f"{DataLogin.baseURL}login")
        driver.find_element(By.ID, LoginPage.email).send_keys(DataLogin.email)
        driver.find_element(By.ID, LoginPage.password).send_keys("12345")
        driver.find_element(By.CSS_SELECTOR, LoginPage.login_button).click()
        error1 = driver.find_element(By.CSS_SELECTOR, LoginPage.error_summary).text
        error2 = driver.find_element(By.CSS_SELECTOR, LoginPage.error_summary_detail).text
        self.assertEqual("Login was unsuccessful. Please correct the errors and try again.", error1)
        self.assertEqual("The credentials provided are incorrect", error2)

    def test_05_empty_email(self):
        driver = self.browser
        driver.get(f"{DataLogin.baseURL}login")
        driver.find_element(By.ID, LoginPage.email).send_keys("")
        driver.find_element(By.ID, LoginPage.password).send_keys(DataLogin.password)
        driver.find_element(By.CSS_SELECTOR, LoginPage.login_button).click()
        error1 = driver.find_element(By.CSS_SELECTOR, LoginPage.error_summary).text
        error2 = driver.find_element(By.CSS_SELECTOR, LoginPage.error_summary_detail).text
        self.assertEqual("Login was unsuccessful. Please correct the errors and try again.", error1)
        self.assertEqual("No customer account found", error2)

    def test_06_empty_password(self):
        driver = self.browser
        driver.get(f"{DataLogin.baseURL}login")
        driver.find_element(By.ID, LoginPage.email).send_keys(DataLogin.email)
        driver.find_element(By.ID, LoginPage.password).send_keys("")
        driver.find_element(By.CSS_SELECTOR, LoginPage.login_button).click()
        error1 = driver.find_element(By.CSS_SELECTOR, LoginPage.error_summary).text
        error2 = driver.find_element(By.CSS_SELECTOR, LoginPage.error_summary_detail).text
        self.assertEqual("Login was unsuccessful. Please correct the errors and try again.", error1)
        self.assertEqual("The credentials provided are incorrect", error2)

    def test_07_empty_email_and_password(self):
        driver = self.browser
        driver.get(f"{DataLogin.baseURL}login")
        driver.find_element(By.ID, LoginPage.email).send_keys("")
        driver.find_element(By.ID, LoginPage.password).send_keys("")
        driver.find_element(By.CSS_SELECTOR, LoginPage.login_button).click()
        error1 = driver.find_element(By.CSS_SELECTOR, LoginPage.error_summary).text
        error2 = driver.find_element(By.CSS_SELECTOR, LoginPage.error_summary_detail).text
        self.assertEqual("Login was unsuccessful. Please correct the errors and try again.", error1)
        self.assertEqual("No customer account found", error2)

    def test_08_activated_remember_me(self):
        driver = self.browser
        driver.get(f"{DataLogin.baseURL}login")
        driver.find_element(By.ID, LoginPage.email).send_keys(DataLogin.email)
        driver.find_element(By.ID, LoginPage.password).send_keys(DataLogin.password)
        driver.find_element(By.ID, LoginPage.rememberme).click()
        driver.find_element(By.CSS_SELECTOR, LoginPage.login_button).click()
        self.assertEqual(driver.current_url, DataLogin.baseURL)
        data = driver.find_element(By.CSS_SELECTOR, LoginPage.profile_info).text
        self.assertEqual(DataLogin.email, data)

    def test_09_unactivated_remember_me(self):
        driver = self.browser
        driver.get(f"{DataLogin.baseURL}login")
        driver.find_element(By.ID, LoginPage.email).send_keys(DataLogin.email)
        driver.find_element(By.ID, LoginPage.password).send_keys(DataLogin.password)
        driver.find_element(By.CSS_SELECTOR, LoginPage.login_button).click()
        self.assertEqual(driver.current_url, DataLogin.baseURL)
        data = driver.find_element(By.CSS_SELECTOR, LoginPage.profile_info).text
        self.assertEqual(DataLogin.email, data)
    
    def test_10_forgot_password(self):
        driver = self.browser
        driver.get(f"{DataLogin.baseURL}login")
        driver.find_element(By.CSS_SELECTOR, LoginPage.forgot_password).click()
        self.assertEqual(driver.current_url, f"{DataLogin.baseURL}passwordrecovery")
        data = driver.find_element(By.CSS_SELECTOR, RecoveryPage.header).text
        self.assertEqual("Password recovery", data)
        driver.find_element(By.ID, RecoveryPage.email).send_keys(DataLogin.email)
        driver.find_element(By.CSS_SELECTOR, RecoveryPage.recover_button).click()
        data = driver.find_element(By.CSS_SELECTOR, RecoveryPage.result).text
        self.assertEqual("Email with instructions has been sent to you.", data)


if __name__ == "__main__":
    unittest.main()
