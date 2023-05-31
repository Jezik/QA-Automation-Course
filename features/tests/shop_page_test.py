import time
import sys
sys.path.append("./pages")
sys.path.append("./helpers")
sys.path.append("./test_data")


from login_page import *
from shop_page import *
from helpers import *
from urls import *


driver = get_driver()
driver.get(login_page)

type_text_to_input(driver, "standard_user", USERNAME_XPATH)
type_text_to_input(driver, "secret_sauce", PASSWORD_XPATH)
click_on_element(driver, LOGIN_BUTTON_XPATH)

time.sleep(3)

click_on_element(driver, ADD_TO_CART_SECOND_ITEM_XPATH)

test_item_added_to_cart(driver)

print("Tests finished.")
