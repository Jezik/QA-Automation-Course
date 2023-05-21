import pytest
import time
import sys
sys.path.append("./pages")
sys.path.append("./helpers")
sys.path.append("./test_data")


from login_page import *
from helpers import *
from urls import *


browser = webdriver.Chrome()
browser.get(login_page)

type_text_to_input(browser, "standard_user", USERNAME_XPATH)
type_text_to_input(browser, "secret_sauce", PASSWORD_XPATH)
click_on_element(browser, LOGIN_BUTTON_XPATH)

time.sleep(5)

# If the login was successful we should see the label PRODUCTS_LABEL_XPATH
def test_if_login_successful():
    assert check_if_element_exists(browser, PRODUCTS_LABEL_XPATH) == True
