import time
import os
import json

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from faker import Faker


WORKING_DIR = os.getcwd()
FILENAME = "faker_generated_data.json"
FILEPATH = WORKING_DIR + "\\features\\test_data\\" + FILENAME


def type_text_to_input(context, text, selector):
    WebDriverWait(context.driver, 15).until(EC.visibility_of_element_located((By.XPATH, selector)))
    elem = context.driver.find_element(By.XPATH, selector)
    elem.click()
    elem.clear()
    elem.send_keys(text)
    elem.send_keys(Keys.RETURN)


def click_on_element(context, selector):
    WebDriverWait(context.driver, 15).until(EC.visibility_of_element_located((By.XPATH, selector)))
    context.driver.find_element(By.XPATH, selector).click()


def check_if_element_exists(context, selector):
    try:
        context.driver.find_element(By.XPATH, selector)
    except NoSuchElementException:
        return False
    return True


def get_elem_text(context, selector):
    WebDriverWait(context.driver, 15).until(EC.visibility_of_element_located((By.XPATH, selector)))
    return context.driver.find_element(By.XPATH, selector).text


def get_elem_list(context, selector):
    return context.driver.find_elements(By.XPATH, selector)


def get_list_length(context, selector):
    result_list = get_elem_list(context, selector)
    return len(result_list)


def get_text_of_list_elems(context, selector):
    result_list = context.driver.find_elements(By.XPATH, selector)
    texts = []
    for elem in result_list:
        elem_text = elem.text
        texts.append(elem_text)
    return texts


def add_item_to_list(context, selector, text):
    actions = ActionChains(context.driver)
    actions.move_to_element(context.driver.find_element(By.XPATH, selector))
    actions.click()
    actions.send_keys(text)
    actions.key_down(Keys.ENTER)
    actions.key_up(Keys.ENTER)
    actions.perform()


def mark_list_elem(context, element):
    actions = ActionChains(context.driver)
    actions.move_to_element(element)
    actions.click()
    actions.perform()


def remove_list_item(context, selector):
    actions = ActionChains(context.driver)
    actions.move_to_element(context.driver.find_element(By.XPATH, selector))
    actions.click(context.driver.find_element(By.XPATH, selector))
    actions.perform()
    time.sleep(1)


def switch_to_iFrame(context, selector):
    context.driver.switch_to.frame(selector)


def text_in_element_attribute(context, selector, attribute, text):
    WebDriverWait(context.driver, 20).until(EC.text_to_be_present_in_element_attribute((By.XPATH, selector), attribute, text))


def get_elem_state(context, selector):
    element = context.driver.find_element(By.XPATH, selector)
    prop = element.get_property("disabled")
    return prop


def select_dropdown_item_by_text(context, selector, visible_text):
    drop = Select(context.driver.find_element(By.XPATH, selector))
    drop.select_by_visible_text(visible_text)


def wait_elem_to_disappear(context, selector):
    WebDriverWait(context.driver, 15).until(EC.invisibility_of_element_located((By.XPATH, selector)))


def upload_file(context, selector, filepath):
    upload_elem = context.driver.find_element(By.XPATH, selector)
    upload_elem.send_keys(filepath)


def get_alert_text(context):
    alert = WebDriverWait(context.driver, 5).until(EC.alert_is_present())
    text = alert.text
    alert.accept()
    return text


def check_current_url_against_pattern(context, pattern):
    current_url = context.driver.current_url
    return current_url.endswith(pattern)


def scroll_page_to_bottom(context):
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    

def scroll_page(context, selector):
    element = context.driver.find_element(By.XPATH, selector)
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()


def generate_user_data(context):
    fake = Faker()
    context.first_name = fake.first_name()
    context.last_name = fake.last_name()
    context.email = fake.email()
    context.address = fake.address()
    context.phone_number = fake.phone_number()


def save_data_to_json_file(context):  
    user_data = {
        "first_name": f"{context.first_name}",
        "last_name": f"{context.last_name}",
        "email": f"{context.email}",
        "address": f"{context.address}",
        "phone": f"{context.phone_number}"
    }

    json_object = json.dumps(user_data, indent=4)

    with open(FILEPATH, "w") as out_json_file:
        out_json_file.write(json_object)


def get_data_from_json():
    with open(FILEPATH, "r") as json_data:
        user_data = json.load(json_data)
        
    return user_data["address"]
