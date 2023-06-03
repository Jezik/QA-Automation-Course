from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options


def get_chrome_options():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    return chrome_options


def get_driver(context):
    context.driver = webdriver.Chrome(chrome_options=get_chrome_options())
    return context.driver


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
    return context.driver.find_element(By.XPATH, selector).text
