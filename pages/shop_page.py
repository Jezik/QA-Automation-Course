from helpers import check_if_element_exists
from helpers import get_elem_text

ADD_TO_CART_SECOND_ITEM_XPATH = "//*[@id='add-to-cart-sauce-labs-bike-light']"
ADD_TO_CART_SECOND_ITEM_CSS = "#add-to-cart-sauce-labs-bike-light"

SHOPPING_CART_BADGE_XPATH = "//*[@id='shopping_cart_container']/a/span"
SHOPPING_CART_BADGE_CSS = "#shopping_cart_container > a > span"


def test_item_added_to_cart(driver):
    assert check_if_element_exists(driver, SHOPPING_CART_BADGE_XPATH)
    assert get_elem_text(driver, SHOPPING_CART_BADGE_XPATH) == "1"
    print("'test_item_added_to_cart'..........PASSED")
