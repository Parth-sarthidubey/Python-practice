from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime as dt
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

def text_saving(text):
    filename = f"./{dt.now().strftime('%Y-%m-%d.%H-%M-%S')}.txt"
    with open(filename, 'w') as file:
        file.write(text)

def main():
    driver = get_driver()
    count=1
    while True:
        count+=1
        if count>10:
            break
        time.sleep(2)
        element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
        text_saving(str(text_cleaner(element.text)))
        
        

print(main())