from selenium import webdriver
from selenium.webdriver.edge.service import Service

service = Service("./edgedriver.exe")
driver= webdriver.Edge(service=service)
driver.get("http://www.apple.com")
