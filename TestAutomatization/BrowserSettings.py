import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

service =Service("./edgedriver.exe")
options= Options()
options.add_experimental_option("excludeSwitches",["enable-automation"])
options.add_experimental_option("useAutomationExtension",False)
options.add_argument("--disable-infobars")
options.add_argument("--alow-running-insecure-content")
options.add_argument("--disable-notifications")
options.add_argument("--disable-save-password")
options.add_argument("--disable-extensions")
options.add_argument("dowload.default_directory=C:/Downloads")
options.add_argument("--window-size=768,1024")
options.add_argument("--disable-popup-blocking")
driver= webdriver.Edge(service=service)
#driver.maximize_window()
driver.implicitly_wait(10)
#driver.get("http://www.google.com")
driver.get("https://www.ucuzabilet.com/")
time.sleep(2)
driver.quit()