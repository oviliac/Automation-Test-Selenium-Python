import random
import string

def random_string(len=3):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(len))

class DataRegisterInvalid:
    firstname = "a"
    lastname = "a"
    email = "awqqhjd@xsasai.com"
    password = "1234567"
    confirmpassword = "1234567"
    email_no_at = "pdndtgamdil.com"
    email_no_dot = "pdndt@gamdilcom"
    email_no_domain = "pdndt@"
    email_registered = "awqqhjd@xsasai.com"
    short_password = "12345"
    mismatch_password = ["123457", "123456"]

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


class DataLoginInvalid:
    email = "awqqhj@xsasai.com"
    password = "1234567a"
