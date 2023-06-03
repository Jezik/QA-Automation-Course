from features.helpers.helpers import *
from behave import then, when


PRODUCTS_LABEL_XPATH = "//*[@id='header_container']/div[2]/span"
PRODUCTS_LABEL_CSS = "#header_container > div.header_secondary_container > span"

ADD_TO_CART_SECOND_ITEM_XPATH = "//*[@id='add-to-cart-sauce-labs-bike-light']"
ADD_TO_CART_SECOND_ITEM_CSS = "#add-to-cart-sauce-labs-bike-light"

SHOPPING_CART_BADGE_XPATH = "//*[@id='shopping_cart_container']/a/span"
SHOPPING_CART_BADGE_CSS = "#shopping_cart_container > a > span"


@then("The user can see a shop layout")
def check_if_user_see_shop_layout(context):
    check_if_element_exists(context, PRODUCTS_LABEL_XPATH)


@when("The user click on add to cart button")
def click_on_add_to_cart_button(context):
    click_on_element(context, ADD_TO_CART_SECOND_ITEM_XPATH)


@then("The item adds to cart and the cart icon shows the number 1")
def check_item_added_to_cart(context):
    assert get_elem_text(context, SHOPPING_CART_BADGE_XPATH) == "1"
