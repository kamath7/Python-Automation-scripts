#clicking on buttons and adding input

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys 

def get_driver():
    
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars") #disabling alerts/popups
    options.add_argument("start-maximized")
    # options.add_argument("--headless")
    options.add_argument('disable-dev-shm-usage') #to avoid other kinds of issues
    options.add_argument("no-sandbox") #to get the greater priveleges
    options.add_experimental_option("excludeSwitches",["enable-automation"])  #to avoid detection
    options.add_argument("disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome('./chromedriver.exe', options=options)
    driver.get('https://automated.pythonanywhere.com/login')
    return driver

def main():
    driver = get_driver()
    driver.find_element(by="id", value="id_username").send_keys("automated") #env in the future
    time.sleep(3)
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated"+ Keys.RETURN)
    driver.current_url #to stop window from closing


print(main())