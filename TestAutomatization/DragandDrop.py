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
driver.get("https://demoqa.com/droppable/")

source = driver.find_element(By.CSS_SELECTOR,"div#simpleDropContainer div")
target= driver.find_element(By.CSS_SELECTOR, "div#simpleDropContainer div.drop-box")

print("Önce: "+ target.text)
action = ActionChains(driver)
action.drag_and_drop(source,target).perform()
time.sleep(2)
print("Sonra: "+target.text)
time.sleep(2)
driver.quit()