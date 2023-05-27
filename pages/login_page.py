from helpers import check_if_element_exists

USERNAME_XPATH = "//*[@id='user-name']"
USERNAME_CSS = "#user-name"

PASSWORD_XPATH = "//*[@id='password']"
PASSWORD_CSS = "#password"

LOGIN_BUTTON_XPATH = "//*[@id='login-button']"
LOGIN_BUTTON_CSS = "#login-button"

PRODUCTS_LABEL_XPATH = "//*[@id='header_container']/div[2]/span"
PRODUCTS_LABEL_CSS = "#header_container > div.header_secondary_container > span"


# If the login was successful we should see the label PRODUCTS_LABEL_XPATH
def test_if_login_successful(driver):
    assert check_if_element_exists(driver, PRODUCTS_LABEL_XPATH) == True
    print("'check_if_element_exists'..........PASSED")
