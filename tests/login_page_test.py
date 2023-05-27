import time
import sys
sys.path.append("./pages")
sys.path.append("./helpers")
sys.path.append("./test_data")


from login_page import *
from helpers import *
from urls import *


driver = webdriver.Chrome()
driver.get(login_page)

type_text_to_input(driver, "standard_user", USERNAME_XPATH)
type_text_to_input(driver, "secret_sauce", PASSWORD_XPATH)
click_on_element(driver, LOGIN_BUTTON_XPATH)

time.sleep(3)

# If the login was successful we should see the label PRODUCTS_LABEL_XPATH
test_if_login_successful(driver)

print("Test finished.")
