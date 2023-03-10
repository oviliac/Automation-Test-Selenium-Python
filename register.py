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

from data import DataRegisterInvalid, DataRegister, random_string
from locator import RegisterPage

class TestRegister(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions() 
        options.add_argument("--headless")
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def test_01_success_register_gendermale(self):
        driver = self.browser
        driver.get(f"{DataRegister.baseURL}register")
        driver.find_element(By.ID, RegisterPage.gender).click()
        driver.find_element(By.ID, RegisterPage.firstname).send_keys(f"{random_string()}{DataRegister.firstname}")
        driver.find_element(By.ID, RegisterPage.lastname).send_keys(f"{random_string()}{DataRegister.lastname}")
        driver.find_element(By.ID, RegisterPage.email).send_keys(f"{random_string()}{DataRegister.email}")
        driver.find_element(By.ID, RegisterPage.password).send_keys(DataRegister.password)
        driver.find_element(By.ID, RegisterPage.confirmpassword).send_keys(DataRegister.confirmpassword)
        driver.find_element(By.ID, RegisterPage.registerbutton).click()
        respon = driver.find_element(By.CLASS_NAME, RegisterPage.result).text
        self.assertIn("Your registration completed", respon)
        registerresult_url = driver.current_url
        self.assertEqual(registerresult_url, f"{DataRegister.baseURL}registerresult/1")
    
    def test_02_empty_all_field(self):
        driver = self.browser
        driver.get(f"{DataRegister.baseURL}register")
        # driver.find_element(By.ID, RegisterPage.gender).click()
        driver.find_element(By.ID, RegisterPage.firstname).send_keys("")
        driver.find_element(By.ID, RegisterPage.lastname).send_keys("")
        driver.find_element(By.ID, RegisterPage.email).send_keys("")
        driver.find_element(By.ID, RegisterPage.password).send_keys("")
        driver.find_element(By.ID, RegisterPage.confirmpassword).send_keys("")
        driver.find_element(By.ID, RegisterPage.registerbutton).click()
        data = driver.find_element(By.CLASS_NAME, RegisterPage.error_validation).text
        self.assertIn("First name is required.", data)

    def test_03_register_without_select_gender(self):
        driver = self.browser
        driver.get(f"{DataRegister.baseURL}register")
        # driver.find_element(By.ID, RegisterPage.gender).click() user can register without selecting gender
        driver.find_element(By.ID, RegisterPage.firstname).send_keys(f"{random_string()}{DataRegister.firstname}")
        driver.find_element(By.ID, RegisterPage.lastname).send_keys(f"{random_string()}{DataRegister.lastname}")
        driver.find_element(By.ID, RegisterPage.email).send_keys(f"{random_string()}{DataRegister.email}")
        driver.find_element(By.ID, RegisterPage.password).send_keys(DataRegister.password)
        driver.find_element(By.ID, RegisterPage.confirmpassword).send_keys(DataRegister.confirmpassword)
        driver.find_element(By.ID, RegisterPage.registerbutton).click()
        respon = driver.find_element(By.CLASS_NAME, RegisterPage.result).text
        self.assertIn("Your registration completed", respon)
        registerresult_url = driver.current_url
        self.assertEqual(registerresult_url, f"{DataRegister.baseURL}registerresult/1")
    
    def test_04_empty_first_name(self):
        driver = self.browser
        driver.get(f"{DataRegister.baseURL}register")
        driver.find_element(By.ID, RegisterPage.gender).click()
        driver.find_element(By.ID, RegisterPage.firstname).send_keys("")
        driver.find_element(By.ID, RegisterPage.lastname).send_keys(f"{random_string()}{DataRegister.lastname}")
        driver.find_element(By.ID, RegisterPage.email).send_keys(f"{random_string()}{DataRegister.email}") 
        driver.find_element(By.ID, RegisterPage.password).send_keys(DataRegister.password)
        driver.find_element(By.ID, RegisterPage.confirmpassword).send_keys(DataRegister.confirmpassword)
        driver.find_element(By.ID, RegisterPage.registerbutton).click()
        data = driver.find_element(By.CLASS_NAME, RegisterPage.error_validation).text
        self.assertIn("First name is required.", data)

    def test_05_empty_last_name(self):
        driver = self.browser
        driver.get(f"{DataRegister.baseURL}register")
        driver.find_element(By.ID, RegisterPage.gender).click()
        driver.find_element(By.ID, RegisterPage.firstname).send_keys(f"{random_string()}{DataRegister.firstname}")
        driver.find_element(By.ID, RegisterPage.lastname).send_keys("")
        driver.find_element(By.ID, RegisterPage.email).send_keys(f"{random_string()}{DataRegister.email}") 
        driver.find_element(By.ID, RegisterPage.password).send_keys(DataRegister.password)
        driver.find_element(By.ID, RegisterPage.confirmpassword).send_keys(DataRegister.confirmpassword)
        driver.find_element(By.ID, RegisterPage.registerbutton).click()
        data = driver.find_element(By.CLASS_NAME, RegisterPage.error_validation).text
        self.assertIn("Last name is required.", data)

    def test_06_empty_email(self):
        driver = self.browser
        driver.get(f"{DataRegister.baseURL}register")
        driver.find_element(By.ID, RegisterPage.gender).click()
        driver.find_element(By.ID, RegisterPage.firstname).send_keys(f"{random_string()}{DataRegister.firstname}")
        driver.find_element(By.ID, RegisterPage.lastname).send_keys(f"{random_string()}{DataRegister.lastname}")
        driver.find_element(By.ID, RegisterPage.email).send_keys("")
        driver.find_element(By.ID, RegisterPage.password).send_keys(DataRegister.password)
        driver.find_element(By.ID, RegisterPage.confirmpassword).send_keys(DataRegister.confirmpassword)
        driver.find_element(By.ID, RegisterPage.registerbutton).click()
        data = driver.find_element(By.CLASS_NAME, RegisterPage.error_validation).text
        self.assertIn("Email is required.", data)
    
    def test_07_empty_password(self):
        driver = self.browser
        driver.get(f"{DataRegister.baseURL}register")
        driver.find_element(By.ID, RegisterPage.gender).click()
        driver.find_element(By.ID, RegisterPage.firstname).send_keys(f"{random_string()}{DataRegister.firstname}")
        driver.find_element(By.ID, RegisterPage.lastname).send_keys(f"{random_string()}{DataRegister.lastname}")
        driver.find_element(By.ID, RegisterPage.email).send_keys(f"{random_string()}{DataRegister.email}") 
        driver.find_element(By.ID, RegisterPage.password).send_keys("")
        driver.find_element(By.ID, RegisterPage.confirmpassword).send_keys("")
        driver.find_element(By.ID, RegisterPage.registerbutton).click()
        data = driver.find_element(By.CLASS_NAME, RegisterPage.error_validation).text
        self.assertIn("Password is required.", data)

    def test_08_empty_confirm_password(self):
        driver = self.browser
        driver.get(f"{DataRegister.baseURL}register")
        driver.find_element(By.ID, RegisterPage.gender).click()
        driver.find_element(By.ID, RegisterPage.firstname).send_keys(f"{random_string()}{DataRegister.firstname}")
        driver.find_element(By.ID, RegisterPage.lastname).send_keys(f"{random_string()}{DataRegister.lastname}")
        driver.find_element(By.ID, RegisterPage.email).send_keys(f"{random_string()}{DataRegister.email}") 
        driver.find_element(By.ID, RegisterPage.password).send_keys(DataRegister.password)
        driver.find_element(By.ID, RegisterPage.confirmpassword).send_keys("")
        driver.find_element(By.ID, RegisterPage.registerbutton).click()
        data = driver.find_element(By.CLASS_NAME, RegisterPage.error_validation).text
        self.assertIn("Password is required.", data)

    def test_09_invalid_email_format_without_At_symbol(self):
        driver = self.browser
        driver.get(f"{DataRegister.baseURL}register")
        driver.find_element(By.ID, RegisterPage.gender).click()
        driver.find_element(By.ID, RegisterPage.firstname).send_keys(f"{random_string()}{DataRegister.firstname}")
        driver.find_element(By.ID, RegisterPage.lastname).send_keys(f"{random_string()}{DataRegister.lastname}")
        driver.find_element(By.ID, RegisterPage.email).send_keys(DataRegisterInvalid.email_no_at)
        driver.find_element(By.ID, RegisterPage.password).send_keys(DataRegister.password)
        driver.find_element(By.ID, RegisterPage.confirmpassword).send_keys(DataRegister.confirmpassword)
        driver.find_element(By.ID, RegisterPage.registerbutton).click()
        data = driver.find_element(By.CLASS_NAME, RegisterPage.error_validation).text
        self.assertIn("Wrong email", data)

    def test_10_invalid_email_format_without_dot(self):
        driver = self.browser
        driver.get(f"{DataRegister.baseURL}register")
        driver.find_element(By.ID, RegisterPage.gender).click()
        driver.find_element(By.ID, RegisterPage.firstname).send_keys(f"{random_string()}{DataRegister.firstname}")
        driver.find_element(By.ID, RegisterPage.lastname).send_keys(f"{random_string()}{DataRegister.lastname}")
        driver.find_element(By.ID, RegisterPage.email).send_keys(DataRegisterInvalid.email_no_dot)
        driver.find_element(By.ID, RegisterPage.password).send_keys(DataRegister.password)
        driver.find_element(By.ID, RegisterPage.confirmpassword).send_keys(DataRegister.confirmpassword)
        driver.find_element(By.ID, RegisterPage.registerbutton).click()
        data = driver.find_element(By.CLASS_NAME, RegisterPage.error_validation).text
        self.assertIn("Wrong email", data)

    def test_11_invalid_email_format_without_domain(self):
        driver = self.browser
        driver.get(f"{DataRegister.baseURL}register")
        driver.find_element(By.ID, RegisterPage.gender).click()
        driver.find_element(By.ID, RegisterPage.firstname).send_keys(f"{random_string()}{DataRegister.firstname}")
        driver.find_element(By.ID, RegisterPage.lastname).send_keys(f"{random_string()}{DataRegister.lastname}")
        driver.find_element(By.ID, RegisterPage.email).send_keys(DataRegisterInvalid.email_no_domain)
        driver.find_element(By.ID, RegisterPage.password).send_keys(DataRegister.password)
        driver.find_element(By.ID, RegisterPage.confirmpassword).send_keys(DataRegister.confirmpassword)
        driver.find_element(By.ID, RegisterPage.registerbutton).click()
        data = driver.find_element(By.CLASS_NAME, RegisterPage.error_validation).text
        self.assertIn("Wrong email", data)

    def test_12_register_using_registered_user_email(self):
        driver = self.browser
        driver.get(f"{DataRegister.baseURL}register")
        driver.find_element(By.ID, RegisterPage.gender).click()
        driver.find_element(By.ID, RegisterPage.firstname).send_keys(f"{random_string()}{DataRegister.firstname}")
        driver.find_element(By.ID, RegisterPage.lastname).send_keys(f"{random_string()}{DataRegister.lastname}")
        driver.find_element(By.ID, RegisterPage.email).send_keys(DataRegisterInvalid.email_registered)
        driver.find_element(By.ID, RegisterPage.password).send_keys(DataRegister.password)
        driver.find_element(By.ID, RegisterPage.confirmpassword).send_keys(DataRegister.confirmpassword)
        driver.find_element(By.ID, RegisterPage.registerbutton).click()
        data = driver.find_element(By.CLASS_NAME, RegisterPage.error_summary).text
        self.assertEqual("The specified email already exists", data)
    
    def test_13_password_length_less_than_six_characters(self):
        driver = self.browser
        driver.get(f"{DataRegister.baseURL}register")
        driver.find_element(By.ID, RegisterPage.gender).click()
        driver.find_element(By.ID, RegisterPage.firstname).send_keys(f"{random_string()}{DataRegister.firstname}")
        driver.find_element(By.ID, RegisterPage.lastname).send_keys(f"{random_string()}{DataRegister.lastname}")
        driver.find_element(By.ID, RegisterPage.email).send_keys(f"{random_string()}{DataRegister.email}") 
        driver.find_element(By.ID, RegisterPage.password).send_keys(DataRegisterInvalid.short_password)
        driver.find_element(By.ID, RegisterPage.confirmpassword).send_keys(DataRegisterInvalid.short_password)
        driver.find_element(By.ID, RegisterPage.registerbutton).click()
        data = driver.find_element(By.CSS_SELECTOR, RegisterPage.error_password).text
        self.assertEqual("The password should have at least 6 characters.", data)

    def test_14_password_confirmation_does_not_match_password(self):
        driver = self.browser
        driver.get(f"{DataRegister.baseURL}register")
        driver.find_element(By.ID, RegisterPage.gender).click()
        driver.find_element(By.ID, RegisterPage.firstname).send_keys(f"{random_string()}{DataRegister.firstname}")
        driver.find_element(By.ID, RegisterPage.lastname).send_keys(f"{random_string()}{DataRegister.lastname}")
        driver.find_element(By.ID, RegisterPage.email).send_keys(f"{random_string()}{DataRegister.email}") 
        driver.find_element(By.ID, RegisterPage.password).send_keys(DataRegisterInvalid.mismatch_password[0])
        driver.find_element(By.ID, RegisterPage.confirmpassword).send_keys(DataRegisterInvalid.mismatch_password[1])
        driver.find_element(By.ID, RegisterPage.registerbutton).click()
        data = driver.find_element(By.CSS_SELECTOR, RegisterPage.error_confirmpassword).text
        self.assertEqual("The password and confirmation password do not match.", data)
    


if __name__ == "__main__":
    unittest.main()