from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_chrome_options():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    return chrome_options

def get_chrome_mobile_options():
    mobile_emulation = { "deviceName": "Pixel 5" }
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    chrome_options.add_experimental_option("windowTypes", ["webview"])
    chrome_options.add_argument("start-maximized")   
    return chrome_options 


def before_scenario(context, scenario):
    if "mobile" in scenario.name:
        context.driver = webdriver.Chrome(options=get_chrome_mobile_options())
    else:
        context.driver = webdriver.Chrome(chrome_options=get_chrome_options())


def after_scenario(context, scenario):
    context.driver.quit()
