from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


USERNAME_XPATH = '//*[@id="user-name"]'
USERNAME_CSS = "#user-name"

PASSWORD_XPATH = "//*[@id='password']"
PASSWORD_CSS = "#password"

LOGIN_BUTTON_XPATH = "//*[@id='login-button']"
LOGIN_BUTTON_CSS = "#login-button"


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


    #Some buteauful function
    
