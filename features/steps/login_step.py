from features.helpers.helpers import *
from features.helpers.urls import *
from behave import given, then, when

USERNAME_XPATH = "//*[@id='user-name']"
USERNAME_CSS = "#user-name"

PASSWORD_XPATH = "//*[@id='password']"
PASSWORD_CSS = "#password"

LOGIN_BUTTON_XPATH = "//*[@id='login-button']"
LOGIN_BUTTON_CSS = "#login-button"

LOGIN_ERROR_FIELD = "//*[@id='login_button_container']/div/form/div[3]"


@given("User starts at login page")
def open_login_page(context):
    #context.driver = get_driver(context)
    context.driver.get(login_page)


@then("User is able to see login and password inputs")
def assert_login_input_is_visible(context):
    check_if_element_exists(context, USERNAME_XPATH)
    check_if_element_exists(context, PASSWORD_XPATH)
    

@when("User types proper credentials and proceed")
def type_proper_credentials(context):
    type_text_to_input(context, "standard_user", USERNAME_XPATH)
    type_text_to_input(context, "secret_sauce", PASSWORD_XPATH)
    click_on_element(context, LOGIN_BUTTON_XPATH)


@when("User types wrong e-mail and right password and proceed")
def type_wrong_email(context):
    type_text_to_input(context, "wrong_email", USERNAME_XPATH)
    type_text_to_input(context, "secret_sauce", PASSWORD_XPATH)
    click_on_element(context, LOGIN_BUTTON_XPATH)

@then("User should see error field with error message")
def assert_error_field_shown(context):
    check_if_element_exists(context, LOGIN_ERROR_FIELD)
