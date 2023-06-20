from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_chrome_options():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    return chrome_options


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(chrome_options=get_chrome_options())


def after_scenario(context, scenario):
    context.driver.quit()
    