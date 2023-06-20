from features.helpers.helpers import *
from features.helpers.urls import *
from behave import given, then, when


TO_DO_ELEMS_XPATH = "//*[@id='container']/ul/li"
ADD_NEW_TASK_XPATH = "//*[@id='container']/input"
TRASH_FIRST_XPATH = "//*[@id='container']/ul/li[1]/span/i"  
TRASH_SECOND_XPATH = "//*[@id='container']/ul/li[2]/span/i"

IFRAME_ID = "frame"
FIRST_HEADER = "/html/body/div[1]/div/div/div[2]/div[1]/div/div[1]/p"
SECOND_HEADER = "/html/body/div[1]/div/div/div[2]/div[3]/div/div[1]/p"
THIRD_HEADER = "/html/body/div[1]/div/div/div[2]/div[2]/div/div[1]/p"


@given("User has opened the page with to-do list")
def to_do_list_page_open(context):
    context.driver.get(to_do_list_page)


@then("User can see 3 default tasks in a list")
def check_default_tasks(context):
    assert get_list_length(context, TO_DO_ELEMS_XPATH) == 3


@when("User adds 2 more tasks in a list")
def add_two_tasks_to_list(context):
    add_item_to_list(context, ADD_NEW_TASK_XPATH, "Learn Avada Kedavra")
    add_item_to_list(context, ADD_NEW_TASK_XPATH, "Kill Lord Voldemort")


@then("List should contains 5 tasks with correct names")
def check_list_content(context):
    assert get_list_length(context, TO_DO_ELEMS_XPATH) == 5
    texts = get_text_of_list_elems(context, TO_DO_ELEMS_XPATH)
    assert texts[0] == "Go to potion class"
    assert texts[1] == "Buy new robes"
    assert texts[2] == "Practice magic"
    assert texts[3] == "Learn Avada Kedavra"
    assert texts[4] == "Kill Lord Voldemort"


@when("User marks all 3 default tasks as done")
def mark_all_tasks_done(context):
    elem_lst = get_elem_list(context, TO_DO_ELEMS_XPATH)
    for elem in elem_lst:
        mark_list_elem(context, elem)


@then("All default tasks should become strikethrough")
def check_list_elems_done(context):
    elem_lst = get_elem_list(context, TO_DO_ELEMS_XPATH)
    for elem in elem_lst:
        assert elem.get_attribute("class") == "completed"


@when("User removes the 1st and the 3rd tasks")
def remove_tasks(context):
    remove_list_item(context, TRASH_FIRST_XPATH)
    remove_list_item(context, TRASH_SECOND_XPATH)


@then("List contains only the 2nd default task")
def check_list_content(context):
    assert get_list_length(context, TO_DO_ELEMS_XPATH) == 1
    texts = get_text_of_list_elems(context, TO_DO_ELEMS_XPATH)
    assert texts[0] == "Buy new robes"


@given("User has opened the page with iFrame")
def open_iFrame_page(context):
    context.driver.get(iFrame_page)


@then("User should be able to see three headers Who we are? Why Choose us? Greate service!")
def check_if_headers_exist(context):
    switch_to_iFrame(context, IFRAME_ID)
    assert check_if_element_exists(context, FIRST_HEADER) == True
    assert check_if_element_exists(context, SECOND_HEADER) == True
    assert check_if_element_exists(context, THIRD_HEADER) == True
