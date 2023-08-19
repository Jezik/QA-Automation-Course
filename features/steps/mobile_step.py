from features.helpers.helpers import *
from features.helpers.urls import *
from time import sleep
from behave import given, then, when


CLOSE_COOKIES_XPATH = "//*[@class='hsMuBe']/div/span"
HAMBURGER_MENU_XPATH = "//*[@id='s9iPrd']"
FIRST_LINK_XPATH = "//*[@id='yuynLe']/ul/li[1]/div/div/a"
SECOND_LINK_XPATH = "//*[@id='yuynLe']/ul/li[2]/div/div/a"
THIRD_LINK_XPATH = "//*[@id='yuynLe']/ul/li[3]/div/div/a"
ROLL_DOWN_DOWNLOADS_XPATH = "//*[@id='yuynLe']/ul/li[5]/div[1]/div/div"
VERSION_SELECTION_LINK = "//*[@id='yuynLe']/ul/li[5]/div[2]/ul/li/div/div/a"
TEXT_TO_VERIFY_XPATH = "//*[@id='h.e02b498c978340a_114']/div/div/p[7]/span"
TEXT_TO_VERIFY = "We always provide ChromeDriver for the current Stable and Beta versions of Chrome. However, if you use Chrome from Dev or Canary channel, or build your own custom version of Chrome, It is possible that there is no available ChromeDriver that officially supports it. In this case, please try the following:"


@given("Open google on mobile")
def open_mobile(context):
    context.driver.get(mobile_emulation_page)
 

@then("Check url")
def check_url(context):
    assert context.driver.current_url == "https://chromedriver.chromium.org/mobile-emulation"
    sleep(5)


@given("User opens chromedriver url on mobile device")
def open_chromedriver_url(context):
    context.driver.get(chromedriver_mobile_page)
    sleep(2)


@when("User closes cookies popup")
def close_popup(context):
    if check_if_element_exists(context, CLOSE_COOKIES_XPATH):
        click_on_element(context, CLOSE_COOKIES_XPATH)


@when("User opens 'hamburger menu'")
def open_hamb_menu(context):
    click_on_element(context, HAMBURGER_MENU_XPATH)


@then("First three links should be visible")
def check_if_first_links_visible(context):
    assert get_elem_text(context, FIRST_LINK_XPATH) == "ChromeDriver"
    assert get_elem_text(context, SECOND_LINK_XPATH) == "Capabilities & ChromeOptions"
    assert get_elem_text(context, THIRD_LINK_XPATH) == "Chrome Extensions"


@when("User rolls down 'Downloads' link")
def roll_down_links(context):
    click_on_element(context, ROLL_DOWN_DOWNLOADS_XPATH)
    sleep(1)


@when("User clicks on 'version selection' link")
def move_to_new_page(context):
    click_on_element(context, VERSION_SELECTION_LINK)


@then("User should be on 'https://chromedriver.chromium.org/downloads/version-selection' page")
def check_mobile_url(context):
    assert context.driver.current_url == "https://chromedriver.chromium.org/downloads/version-selection"


@when("User scrolls down till the bottom")
def scroll_to_bottom(context):
    scroll_page_to_bottom(context)


@then("The correct text should be visible to user")
def check_visible_text(context):
    assert get_elem_text(context, TEXT_TO_VERIFY_XPATH) == TEXT_TO_VERIFY
