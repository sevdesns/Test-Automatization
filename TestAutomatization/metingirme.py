from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

service = Service("./edgedriver.exe")
driver= webdriver.Edge(service=service)
driver.get("https://google.com")
searchlabel= driver.find_element(By.NAME,"q")
searchlabel.send_keys("selenium")
searchlabel.send_keys(Keys.ENTER)
