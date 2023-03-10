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

class TestRegister(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions() 
        options.add_argument("--headless")
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def test_01_success_register_gendermale(self):
        driver = self.browser
        driver.get(f"{DataRegister.baseURL}register")
        driver.find_element(By.ID, "gender-male").click()
        driver.find_element(By.ID, "FirstName").send_keys(f"{random_string()}{DataRegister.firstname}")
        driver.find_element(By.ID, "LastName").send_keys(f"{random_string()}{DataRegister.lastname}")
        driver.find_element(By.ID, "Email").send_keys(f"{random_string()}{DataRegister.email}")
        driver.find_element(By.ID, "Password").send_keys(DataRegister.password)
        driver.find_element(By.ID, "ConfirmPassword").send_keys(DataRegister.confirmpassword)
        driver.find_element(By.ID, "register-button").click()
        respon = driver.find_element(By.CLASS_NAME, "result").text
        self.assertIn("Your registration completed", respon)
        registerresult_url = driver.current_url
        self.assertEqual(registerresult_url, "https://demowebshop.tricentis.com/registerresult/1")
    
    def test_02_empty_all_field(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/register")
        # driver.find_element(By.ID, "gender-male").click()
        driver.find_element(By.ID, "FirstName").send_keys("")
        driver.find_element(By.ID, "LastName").send_keys("")
        driver.find_element(By.ID, "Email").send_keys("")
        driver.find_element(By.ID, "Password").send_keys("")
        driver.find_element(By.ID, "ConfirmPassword").send_keys("")
        driver.find_element(By.ID, "register-button").click()
        data = driver.find_element(By.CLASS_NAME, "field-validation-error").text
        self.assertIn("First name is required.", data)

    def test_03_register_without_select_gender(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/register")
        # driver.find_element(By.ID, "gender-male").click() user can register without selecting gender
        driver.find_element(By.ID, "FirstName").send_keys(f"{random_string()}{DataRegister.firstname}")
        driver.find_element(By.ID, "LastName").send_keys(f"{random_string()}{DataRegister.lastname}")
        driver.find_element(By.ID, "Email").send_keys(f"{random_string()}{DataRegister.email}")
        driver.find_element(By.ID, "Password").send_keys(DataRegister.password)
        driver.find_element(By.ID, "ConfirmPassword").send_keys(DataRegister.confirmpassword)
        driver.find_element(By.ID, "register-button").click()
        respon = driver.find_element(By.CLASS_NAME, "result").text
        self.assertIn("Your registration completed", respon)
        registerresult_url = driver.current_url
        self.assertEqual(registerresult_url, "https://demowebshop.tricentis.com/registerresult/1")
    
    def test_04_empty_first_name(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/register")
        driver.find_element(By.ID, "gender-male").click()
        driver.find_element(By.ID, "FirstName").send_keys("")
        driver.find_element(By.ID, "LastName").send_keys(f"{random_string()}{DataRegister.lastname}")
        driver.find_element(By.ID, "Email").send_keys(f"{random_string()}{DataRegister.email}") 
        driver.find_element(By.ID, "Password").send_keys(DataRegister.password)
        driver.find_element(By.ID, "ConfirmPassword").send_keys(DataRegister.confirmpassword)
        driver.find_element(By.ID, "register-button").click()
        data = driver.find_element(By.CLASS_NAME, "field-validation-error").text
        self.assertIn("First name is required.", data)

    def test_05_empty_last_name(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/register")
        driver.find_element(By.ID, "gender-male").click()
        driver.find_element(By.ID, "FirstName").send_keys(f"{random_string()}{DataRegister.firstname}")
        driver.find_element(By.ID, "LastName").send_keys("")
        driver.find_element(By.ID, "Email").send_keys(f"{random_string()}{DataRegister.email}") 
        driver.find_element(By.ID, "Password").send_keys(DataRegister.password)
        driver.find_element(By.ID, "ConfirmPassword").send_keys(DataRegister.confirmpassword)
        driver.find_element(By.ID, "register-button").click()
        data = driver.find_element(By.CLASS_NAME, "field-validation-error").text
        self.assertIn("Last name is required.", data)

    def test_06_empty_email(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/register")
        driver.find_element(By.ID, "gender-male").click()
        driver.find_element(By.ID, "FirstName").send_keys(f"{random_string()}{DataRegister.firstname}")
        driver.find_element(By.ID, "LastName").send_keys(f"{random_string()}{DataRegister.lastname}")
        driver.find_element(By.ID, "Email").send_keys("")
        driver.find_element(By.ID, "Password").send_keys(DataRegister.password)
        driver.find_element(By.ID, "ConfirmPassword").send_keys(DataRegister.confirmpassword)
        driver.find_element(By.ID, "register-button").click()
        data = driver.find_element(By.CLASS_NAME, "field-validation-error").text
        self.assertIn("Email is required.", data)
    
    def test_07_empty_password(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/register")
        driver.find_element(By.ID, "gender-male").click()
        driver.find_element(By.ID, "FirstName").send_keys(f"{random_string()}{DataRegister.firstname}")
        driver.find_element(By.ID, "LastName").send_keys(f"{random_string()}{DataRegister.lastname}")
        driver.find_element(By.ID, "Email").send_keys(f"{random_string()}{DataRegister.email}") 
        driver.find_element(By.ID, "Password").send_keys("")
        driver.find_element(By.ID, "ConfirmPassword").send_keys("")
        driver.find_element(By.ID, "register-button").click()
        data = driver.find_element(By.CLASS_NAME, "field-validation-error").text
        self.assertIn("Password is required.", data)

    def test_08_empty_confirm_password(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/register")
        driver.find_element(By.ID, "gender-male").click()
        driver.find_element(By.ID, "FirstName").send_keys(f"{random_string()}{DataRegister.firstname}")
        driver.find_element(By.ID, "LastName").send_keys(f"{random_string()}{DataRegister.lastname}")
        driver.find_element(By.ID, "Email").send_keys(f"{random_string()}{DataRegister.email}") 
        driver.find_element(By.ID, "Password").send_keys(DataRegister.password)
        driver.find_element(By.ID, "ConfirmPassword").send_keys("")
        driver.find_element(By.ID, "register-button").click()
        data = driver.find_element(By.CLASS_NAME, "field-validation-error").text
        self.assertIn("Password is required.", data)

    def test_09_invalid_email_format_without_At_symbol(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/register")
        driver.find_element(By.ID, "gender-male").click()
        driver.find_element(By.ID, "FirstName").send_keys(f"{random_string()}{DataRegister.firstname}")
        driver.find_element(By.ID, "LastName").send_keys(f"{random_string()}{DataRegister.lastname}")
        driver.find_element(By.ID, "Email").send_keys("pdndtgamdil.com")
        driver.find_element(By.ID, "Password").send_keys(DataRegister.password)
        driver.find_element(By.ID, "ConfirmPassword").send_keys(DataRegister.confirmpassword)
        driver.find_element(By.ID, "register-button").click()
        data = driver.find_element(By.CLASS_NAME, "field-validation-error").text
        self.assertIn("Wrong email", data)

    def test_10_invalid_email_format_without_dot(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/register")
        driver.find_element(By.ID, "gender-male").click()
        driver.find_element(By.ID, "FirstName").send_keys(f"{random_string()}{DataRegister.firstname}")
        driver.find_element(By.ID, "LastName").send_keys(f"{random_string()}{DataRegister.lastname}")
        driver.find_element(By.ID, "Email").send_keys("pdndt@gamdilcom")
        driver.find_element(By.ID, "Password").send_keys(DataRegister.password)
        driver.find_element(By.ID, "ConfirmPassword").send_keys(DataRegister.confirmpassword)
        driver.find_element(By.ID, "register-button").click()
        data = driver.find_element(By.CLASS_NAME, "field-validation-error").text
        self.assertIn("Wrong email", data)

    def test_11_invalid_email_format_without_domain(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/register")
        driver.find_element(By.ID, "gender-male").click()
        driver.find_element(By.ID, "FirstName").send_keys(f"{random_string()}{DataRegister.firstname}")
        driver.find_element(By.ID, "LastName").send_keys(f"{random_string()}{DataRegister.lastname}")
        driver.find_element(By.ID, "Email").send_keys("pdndt@")
        driver.find_element(By.ID, "Password").send_keys(DataRegister.password)
        driver.find_element(By.ID, "ConfirmPassword").send_keys(DataRegister.confirmpassword)
        driver.find_element(By.ID, "register-button").click()
        data = driver.find_element(By.CLASS_NAME, "field-validation-error").text
        self.assertIn("Wrong email", data)

    def test_12_register_using_registered_user_email(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/register")
        driver.find_element(By.ID, "gender-male").click()
        driver.find_element(By.ID, "FirstName").send_keys(f"{random_string()}{DataRegister.firstname}")
        driver.find_element(By.ID, "LastName").send_keys(f"{random_string()}{DataRegister.lastname}")
        driver.find_element(By.ID, "Email").send_keys("awqqhjd@xsasai.com")
        driver.find_element(By.ID, "Password").send_keys(DataRegister.password)
        driver.find_element(By.ID, "ConfirmPassword").send_keys(DataRegister.confirmpassword)
        driver.find_element(By.ID, "register-button").click()
        data = driver.find_element(By.CLASS_NAME, "validation-summary-errors").text
        self.assertEqual("The specified email already exists", data)
    
    def test_13_password_length_less_than_six_characters(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/register")
        driver.find_element(By.ID, "gender-male").click()
        driver.find_element(By.ID, "FirstName").send_keys(f"{random_string()}{DataRegister.firstname}")
        driver.find_element(By.ID, "LastName").send_keys(f"{random_string()}{DataRegister.lastname}")
        driver.find_element(By.ID, "Email").send_keys(f"{random_string()}{DataRegister.email}") 
        driver.find_element(By.ID, "Password").send_keys("12345")
        driver.find_element(By.ID, "ConfirmPassword").send_keys("12345")
        driver.find_element(By.ID, "register-button").click()
        data = driver.find_element(By.CSS_SELECTOR, ".field-validation-error[data-valmsg-for='Password']").text
        self.assertEqual("The password should have at least 6 characters.", data)

    def test_14_password_confirmation_does_not_match_password(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/register")
        driver.find_element(By.ID, "gender-male").click()
        driver.find_element(By.ID, "FirstName").send_keys(f"{random_string()}{DataRegister.firstname}")
        driver.find_element(By.ID, "LastName").send_keys(f"{random_string()}{DataRegister.lastname}")
        driver.find_element(By.ID, "Email").send_keys(f"{random_string()}{DataRegister.email}") 
        driver.find_element(By.ID, "Password").send_keys("123457")
        driver.find_element(By.ID, "ConfirmPassword").send_keys("123456")
        driver.find_element(By.ID, "register-button").click()
        data = driver.find_element(By.CSS_SELECTOR, ".field-validation-error[data-valmsg-for='ConfirmPassword']").text
        self.assertEqual("The password and confirmation password do not match.", data)
    


if __name__ == "__main__":
    unittest.main()