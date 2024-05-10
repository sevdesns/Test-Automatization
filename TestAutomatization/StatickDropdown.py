import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select  import Select

service =Service("./edgedriver.exe")

driver= webdriver.Edge(service=service)
driver.maximize_window()
driver.get("https://tomspizzeria.b4a.app/")
dropdown= driver.find_element(By.ID,"odeme-tipi")
pay= Select(dropdown)
pay_type = pay.options #web element list , for each option tag

for tip in pay_type:
    print(tip.text)
time.sleep(2)
pay.select_by_index(3)
time.sleep(2)
driver.quit()

