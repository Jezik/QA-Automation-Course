import time
from helpers import *
from urls import *

USERNAME_XPATH = "//*[@id='user-name']"
USERNAME_CSS = "#user-name"

PASSWORD_XPATH = "//*[@id='password']"
PASSWORD_CSS = "#password"

LOGIN_BUTTON_XPATH = "//*[@id='login-button']"
LOGIN_BUTTON_CSS = "#login-button"

PRODUCTS_LABEL_XPATH = "//*[@id='header_container']/div[2]/span"
PRODUCTS_LABEL_CSS = "#header_container > div.header_secondary_container > span"

@given("User starts at login page")
def open_login_page(context):
    context.driver = get_driver(context)
    context.driver.get(login_page)
    time.sleep(5)

    


@then("User ia able to see login and password inputs")
def assert_login_input_is_visible(context):
    check_if_element_exists(context, USERNAME_XPATH)
    check_if_element_exists(context, PASSWORD_XPATH)

@when("User types proper credentials and proceed")
def type_proper_credentials(context):
    type_text_to_input(context.driver, "standard_user", USERNAME_XPATH)
    type_text_to_input(context.driver, "secret_sauce", PASSWORD_XPATH)
    click_on_element(context.driver, LOGIN_BUTTON_XPATH)





# If the login was successful we should see the label PRODUCTS_LABEL_XPATH
def test_if_login_successful(driver):
    assert check_if_element_exists(driver, PRODUCTS_LABEL_XPATH) == True
    print("'check_if_element_exists'..........PASSED")
