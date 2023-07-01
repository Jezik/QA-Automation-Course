from features.helpers.helpers import *
from features.helpers.urls import *
from behave import given, then, when

SCROLL_TO_XPATH = "//*[@id='zone4']"
CHECK_XPATH = "//*[@id='zone4']/h1"


@given("User opened a page for Scrolling")
def step_imp(context):
    context.driver.get(scrolling_page)


@when("User scrolls till the end of page")
def scroll_imp(context):
    scroll_page(context, SCROLL_TO_XPATH)


@then("User will see some feedback")
def check_feedback(context):
    assert check_if_element_exists(context, CHECK_XPATH) == False
