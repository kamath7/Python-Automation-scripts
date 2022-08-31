from selenium import webdriver

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
    driver.get('https://www.amazon.com/PF-WaterWorks-PF0989-Disposal-Installation/dp/B078H38Q1M/')
    return driver

def cleanText(text):
    return float(text.split(': ')[1])

def main():
    driver = get_driver()
    elem = driver.find_element(by="xpath", value='/html/body/div[1]/div[2]/div[9]/div[6]/div[4]/div[9]/div[1]/div[1]/span/span[2]/span[2]')
    return elem.text

print(main())