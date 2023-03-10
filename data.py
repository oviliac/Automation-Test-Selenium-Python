import random
import string

def random_string(len=3):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(len))

class DataRegisterInvalid:
    baseURL = "https://demowebshop.tricentis.com/"
    firstname = "a"
    lastname = "a"
    email = "awqqhjd@xsasai.com"
    password = "1234567"
    confirmpassword = "1234567"

class DataRegister:
    baseURL = "https://demowebshop.tricentis.com/"
    firstname = "Selenium123"
    lastname = "SQA123"
    email = "oviliach123@gmail.com"
    password = "ovi123"
    confirmpassword = "ovi123"

class DataLogin:
    baseURL = "https://demowebshop.tricentis.com/"
    email = "oviliach123@gmail.com"
    password = "123456"
