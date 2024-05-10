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
driver.get("https://the-internet.herokuapp.com/hovers")

user= driver.find_element(By.CSS_SELECTOR,"div.figure")
name= driver.find_element(By.CSS_SELECTOR,"div.figcaption h5")
link= driver.find_element(By.CSS_SELECTOR,"div.figcaption a ")
print(user.is_displayed())
print("isim:"+name.text)
time.sleep(2)
move= ActionChains(driver)
move.move_to_element(user)
move.perform()
time.sleep(2)
print("------")
print(user.is_displayed())
print("isim:" +name.text)
link.click()
