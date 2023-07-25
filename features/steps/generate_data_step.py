import requests

from features.helpers.helpers import *
from features.helpers.urls import *
from behave import given, then, when


@given("User send proper request to Moccaro")
def send_request_to_moccaro(context):
    context.r = requests.get("https://my.api.mockaroo.com/shop_data.json?key=c09ef3e0")


@then("Request return with proper status code")
def check_request(context):
    assert context.r.status_code == 200


@when("User picks address from json")
def take_address_from_json(context):
    context.token = context.r.json()
    context.address = context.token["address"]
    

@then("Correct address should be printed out")
def print_address_json(context):
    print(context.address)
    

@given("User generates some data with Faker")
def generate_test_user_data(context):
    generate_user_data(context)


@then("Generated data is saved in a .json file inside test_data folder")
def save_generated_data_to_file(context):
    save_data_to_json_file(context)


@then("Address value from .json file is printed out")
def print_address_file(context):
    print(get_data_from_json())
