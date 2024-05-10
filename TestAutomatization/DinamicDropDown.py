import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service =Service("./edgedriver.exe")

driver= webdriver.Edge(service=service)
driver.maximize_window()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.ucuzabilet.com/")

where= driver.find_element(By.ID,"from_text")
where.send_keys("avust")
time.sleep(2)
graz= driver.find_element(By.XPATH,"//li[contaiins(text(),'GRZ')]")
graz.click()

time.sleep(2)
driver.quit()
