import time

from login_page import *


USERNAME_XPATH = "//*[@id='user-name']"
USERNAME_CSS = "#user-name"

PASSWORD_XPATH = "//*[@id='password']"
PASSWORD_CSS = "#password"

LOGIN_BUTTON_XPATH = "//*[@id='login-button']"
LOGIN_BUTTON_CSS = "#login-button"


browser = webdriver.Chrome()
browser.get("https://www.saucedemo.com/")

type_text_to_input(browser, "standard_user", USERNAME_XPATH)
type_text_to_input(browser, "secret_sauce", PASSWORD_XPATH)
click_on_element(browser, LOGIN_BUTTON_XPATH)

time.sleep(10)
