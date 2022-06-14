from selenium import webdriver
import time

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
    driver.get('https://titan22.com/')
    return driver


def main():
    driver = get_driver()
    driver.find_element(by="xpath",value="/html/body/footer/div/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a").click()
    time.sleep(2)
    driver.find_element(by="id",value="ContactFormEmail").send_keys("lallenata@gmail.com")
    time.sleep(100)

main()