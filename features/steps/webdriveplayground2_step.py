import os

from features.helpers.helpers import *
from features.helpers.urls import *
from behave import given, then, when


OPEN_HIDDEN_TEXT_BUTTON_XPATH = "//button[@id='manual-testing-accordion']"

CABBAGE_XPATH = "//form[@id='radio-buttons-selected-disabled']/input[2]"

DROPDOWN_FIRST_XPATH = "//select[@id='dropdowm-menu-1']"

SPINNER_XPATH = "//*[@id='loader']"
HIDDEN_BUTTON_XPATH = "//*[@id='button1']/p"
HIDDEN_WAIT_HEADER_XPATH = "//*[@id='myModalClick']/div/div/div[1]/h4"

CHOOSE_FILE_BUTTON_XPATH = "//*[@id='myFile']"
SEND_FILE_BUTTON_XPATH = "//*[@id='submit-button']"

WORKING_DIR = os.getcwd()
FILENAME = "anti_sonik.png"
IMAGE_FILEPATH = WORKING_DIR + "\\features\\test_data\\" + FILENAME


@given("User opened the page for attributes testing")
def to_do_list_page_open(context):
    context.driver.get(attribute_test_page)


@when("User click plus sign")
def open_hidden_text(context):
    click_on_element(context, OPEN_HIDDEN_TEXT_BUTTON_XPATH)


@then("The class attribute of a button should change to correct one")
def check_text_attributes(context):
    text_in_element_attribute(context, OPEN_HIDDEN_TEXT_BUTTON_XPATH, "class", "accordion active")


@given("User opened the page for Checkboxes")
def checkboxes_page_open(context):
    context.driver.get(checkboxes_test_page)


@then("The field Cabbage should be disabled")
def check_field_diasabled(context):
    assert get_elem_state(context, CABBAGE_XPATH) == True


@when("User openes the first menu item and selects Python")
def select_desired_language(context):
    select_dropdown_item_by_text(context, DROPDOWN_FIRST_XPATH, "Python")


@then("User should see the Python in a first dropdown item")
def check_first_item(context):
    pass
    # assert get_elem_text(context, DROPDOWN_FIRST) == "Python"


@given("User opened a page with spinner")
def spinner_page_open(context):
    context.driver.get(ajax_spinner_page)


@when("The wait is over")
def wait_content_loaded(context):
    wait_elem_to_disappear(context, SPINNER_XPATH)


@then("The user should see a button")
def check_button_is_here(context):
    assert check_if_element_exists(context, HIDDEN_BUTTON_XPATH) == True


@when("The user clicks on this button")
def click_hidden_button(context):
    click_on_element(context, HIDDEN_BUTTON_XPATH)


@then("The correct text should be shown")
def check_shown_header(context):
    assert get_elem_text(context, HIDDEN_WAIT_HEADER_XPATH) == "Well Done For Waiting....!!!"


@given("User opened a page for image uploading")
def image_upload_page_open(context):
    context.driver.get(image_upload_page)


@when("User uploads an image")
def upload_image(context):
    upload_file(context, CHOOSE_FILE_BUTTON_XPATH, IMAGE_FILEPATH)


@when("User clicks on upload button")
def push_image(context):
    click_on_element(context, SEND_FILE_BUTTON_XPATH)


@then("The popup with success message appears")
def check_popup_and_url(context):
    assert get_alert_text(context) == "Your file has now been uploaded!"
    assert check_current_url_against_pattern(context, "?filename=" + FILENAME) == True
