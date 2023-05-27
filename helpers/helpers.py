from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options


def get_chrome_options():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    return chrome_options


def get_driver():
    driver = webdriver.Chrome(chrome_options=get_chrome_options())
    return driver


def type_text_to_input(driver, text, selector):
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, selector)))
    elem = driver.find_element(By.XPATH, selector)
    elem.click()
    elem.clear()
    elem.send_keys(text)
    elem.send_keys(Keys.RETURN)


def click_on_element(driver, selector):
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, selector)))
    driver.find_element(By.XPATH, selector).click()


def check_if_element_exists(driver, selector):
    try:
        driver.find_element(By.XPATH, selector)
    except NoSuchElementException:
        return False
    return True


def get_elem_text(driver, selector):
    return driver.find_element(By.XPATH, selector).text
