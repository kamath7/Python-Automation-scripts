from selenium import webdriver

driver = webdriver.Chrome('./chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument("disable-infobars") #disabling alerts/popups
options.add_argument("start-maximized")
options.add_argument('disable-dev-shm-usage') #to avoid other kinds of issues
options.add_argument("no-sandbox") #to get the greater priveleges
options.add_experimental_option("excludeSwitches",["enable-automation"])  #to avoid detection
options.add_experimental_option("disable-blink-features=AutomationControlled")


driver.get("https://google.com")
