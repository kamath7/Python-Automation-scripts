from selenium import webdriver
import time

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
    driver.get('https://automated.pythonanywhere.com/')
    return driver

def cleanText(text):
    return float(text.split(': ')[1])

def main():
    driver = get_driver()
    element = driver.find_element(by='xpath',value='/html/body/div[1]/div/h1[1]')
    time.sleep(2)
    element2 = driver.find_element(by='xpath', value='/html/body/div[1]/div/h1[2]')
    return element.text,cleanText(element2.text)

print(main())
