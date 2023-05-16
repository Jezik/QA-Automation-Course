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

time.sleep(10)
