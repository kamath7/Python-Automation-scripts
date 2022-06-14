from datetime import datetime
from app import get_driver
import time
from selenium.webdriver.common.keys import Keys 
from selenium import webdriver
from datetime import datetime as dt



def get_driver():
    
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars") #disabling alerts/popups
    options.add_argument("start-maximized")
    options.add_argument("--headless")
    options.add_argument('disable-dev-shm-usage') #to avoid other kinds of issues
    options.add_argument("no-sandbox") #to get the greater priveleges
    options.add_experimental_option("excludeSwitches",["enable-automation"])  #to avoid detection
    options.add_argument("disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome('./chromedriver.exe', options=options)
    driver.get('https://automated.pythonanywhere.com/login')
    return driver


def clean_text(text):
    return float(text.split(': ')[1])

def save_to_file(content):
    f1 = open(f"{dt.now().strftime('%Y-%m-%d.%H-%M-%S')}.txt","a")
    f1.write(str(content)+"\n")
    f1.close()


def main():
    driver = get_driver()
    driver.find_element(by="id", value="id_username").send_keys("automated") #env in the future
    time.sleep(3)
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated"+ Keys.RETURN)
    driver.find_element(by="xpath",value="/html/body/nav/div/a").click()
    time.sleep(5)
    element2 = driver.find_element(by='xpath', value='/html/body/div[1]/div/h1[2]')
    time.sleep(5)
    for i in range(0,10):
        element2 = driver.find_element(by='xpath', value='/html/body/div[1]/div/h1[2]')
        time.sleep(2)
        text = clean_text(element2.text)
        save_to_file(text)

print(main())