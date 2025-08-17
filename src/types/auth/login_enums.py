from enum import Enum

class LoginPageErrorMessages(str, Enum):
    LOCKED_OUT = "Epic sadface: Sorry, this user has been locked out."
    INVALID_CREDS = "Epic sadface: Username and password do not match any user in this service"
