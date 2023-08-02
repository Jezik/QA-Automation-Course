import requests

from features.helpers.helpers import *
from behave import given, then, when


@given("User perform GET request to a https://jsonplaceholder.typicode.com/users with username=Antonette")
def perform_get_request(context):
    payload = {"username": "Antonette"}
    context.response = requests.get("https://jsonplaceholder.typicode.com/users", params=payload)


@when("User takes id from the response and use it in the POST request")
def perform_post_request(context):
    data = context.response.json()
    userId = data[0]["id"]

    payload = {"userId": userId, "title": "make the homework", "completed": True}
    context.post_response = requests.post("https://jsonplaceholder.typicode.com/todos", data=payload)


@then("The server response should contain correct data")
def check_server_post_response(context):
    data = context.post_response.json()
    assert (data["userId"]) == "2"
    assert data["title"] == "make the homework"
    assert data["completed"] == "True"
