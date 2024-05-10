from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

service = Service("./edgedriver.exe")
driver= webdriver.Edge(service=service)
driver.maximize_window()
driver.get("https://tr.wikipedia.org/wiki/Anasayfa")
searchlabel= driver.find_element(By.ID,"mf-tfp")
searchlabel_yazısı=searchlabel.text
searchlabel_yazısı=searchlabel_yazısı.split(",")[0]
print("seçkin madde:" + searchlabel_yazısı)
driver.quit()
