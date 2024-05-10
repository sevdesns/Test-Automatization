import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service =Service("./edgedriver.exe")

driver= webdriver.Edge(service=service)
driver.maximize_window()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/upload")
file = "C:\\Users\\lenovo\\Desktop\\TestAutomatization\\edgedriver.exe"

upload_file = driver.find_element(By.ID,'file-upload')
time.sleep(2)
upload_file.send_keys(file)

driver.find_element(By.ID,"file-submit").click()
WebDriverWait(driver,30).until(expected_conditions.presence_of_element_located((By.TAG_NAME,"h3")))
title = driver.find_element(By.TAG_NAME,"h3").text
print(title)

file= driver.find_element(By.ID,"uploaded-files").text
print(file)
time.sleep(2)
driver.quit()