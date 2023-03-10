class RegisterPage:
    gender = "gender-male"
    firstname = "FirstName"
    lastname = "LastName"
    email = "Email"
    password = "Password"
    confirmpassword = "ConfirmPassword"
    registerbutton = "register-button"
    result = "result"
    error_validation = "field-validation-error"
    error_summary = "validation-summary-errors"
    error_password = ".field-validation-error[data-valmsg-for='Password']"
    error_confirmpassword = ".field-validation-error[data-valmsg-for='ConfirmPassword']"

class LoginPage:
    email = "Email"
    password = "Password"
    rememberme = "RememberMe"
    login_button = ".button-1.login-button[type=submit]"
    profile_info = ".header-links > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)"
    forgot_password = ".forgot-password > a:nth-child(1)"
    error_summary = ".validation-summary-errors > span:nth-child(1)"
    error_summary_detail = ".validation-summary-errors > ul:nth-child(2) > li:nth-child(1)"

class RecoveryPage:
    header = ".page-title > h1:nth-child(1)"
    email = "Email"
    recover_button = ".password-recovery-button[type=submit]"
    result = ".result"