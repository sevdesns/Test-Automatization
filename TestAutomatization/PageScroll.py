import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select  import Select

service =Service("./edgedriver.exe")

driver= webdriver.Edge(service=service)
driver.maximize_window()
driver.get("https://www.homeexchange.com/")
driver.execute_script("window.scrollBy(0,300)","")
time.sleep(2)
driver.execute_script("window.scrollBy(0,3000)","")
time.sleep(3)


