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
#driver implicitity_wait(30)
#driver nesnesi ile çalışıyor
driver.get("https://pynishant.github.io/Selenium-python-waits.html")
tryit= driver.find_element(By.XPATH,"//button[contains(text(), 'Try it')]").click()

WebDriverWait(driver,45,0.1,ignored_exceptions=[NoSuchElementException]).until(expected_conditions.presence_of_element_located((By.XPATH,"//button[contains(text(),'CLICK ME')]")))
clickme=driver.find_element(By.XPATH,"//button[contains(text(),'CLICK ME')]").click()

WebDriverWait(driver,3).until(expected_conditions.alert_is_present())
alert =Alert(driver)
alert.accept()

#presence vs visibility
#implicit wait - gizli bekleme
#explicit wait - açıktan bekleme
#fluent wait

driver.quit()