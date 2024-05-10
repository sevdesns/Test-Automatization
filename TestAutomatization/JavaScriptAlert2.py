import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select  import Select
from selenium.webdriver.support.wait import WebDriverWait

service =Service("./edgedriver.exe")

driver= webdriver.Edge(service=service)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
buton2= driver.find_element(By.XPATH,"(//button)[3]")
buton2.click()
WebDriverWait(driver,3).until(expected_conditions.alert_is_present())
alert =Alert(driver)
time.sleep(1)
message=alert.text
alert.send_keys("selenium alert test")
time.sleep(2)
alert.accept()

result= driver.find_element(By.ID,"result").text
print("mesaj:"+message)
print("sonuç:"+ result)

driver.quit()