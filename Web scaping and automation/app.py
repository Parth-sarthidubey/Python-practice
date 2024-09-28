from selenium import webdriver
from selenium.webdriver.common.by import By
import time



def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("start-maximized")
    options.add_argument("no-sandbox")
    options.add_argument("disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches",["enable-automation"])


    driver = webdriver.Chrome(options=options)
    driver.get("http://automated.pythonanywhere.com")
    return driver

def text_cleaner(text):
    output=float(text.split(": ")[1])
    return output

def main():
    driver = get_driver()
    time.sleep(3)
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    return text_cleaner(element.text)

print(main())