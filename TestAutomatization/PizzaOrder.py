import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select  import Select

service =Service("./edgedriver.exe")

driver= webdriver.Edge(service=service)
driver.maximize_window()
driver.get("https://tomspizzeria.b4a.app/")

def siparisver():
    driver.find_element(By.ID,"siparis").click()
def mesajoku():
    return driver.find_element(By.ID, "mesaj").text
#müşteri ismi
siparisver()
mesaj= mesajoku()
assert mesaj== "Müşteri ismi girmediniz"
#Müşteri simi girmediniz
#pizza boyu
#pizza boyu seçmediniz
isim="Tom Cruise"
driver.find_element(By.ID,"musteri-adi").send_keys(isim)
siparisver()
mesaj= mesajoku()
assert mesaj== "Pizza boyu seçmediniz"
#ödeme şekli
#ödeme tipi seçmediniz
driver.find_element(By.CSS_SELECTOR,"input[value='Küçük").click()
siparisver()
mesaj= mesajoku()
assert mesaj== "Ödeme tipi seçmediniz"

zeytin =driver.find_element(By.CSS_SELECTOR,"input[value='zeytin'")
mantar= driver.find_element(By.CSS_SELECTOR,"input[value='mantar'")
zeytin.click()
mantar.click()
#siparişiniz alındı
dropdown = driver.find_element(By.ID,'odeme-tipi')
odeme= Select(dropdown)
odeme.select_by_index(2)
siparisver()
mesaj= mesajoku()
assert mesaj== "Siparişiniz alındı"

musteri= driver.find_element(By.ID,"musteri").text
boy= driver.find_element(By.ID,"pizzaboyu").text
ek= driver.find_element(By.ID,"pizzaustu").text
odeme= driver.find_element(By.ID,"odeme").text
tutar= driver.find_element(By.ID,"tutar").text

"""assert musteri == "Müşteri ismi:" + isim
assert boy == "Pizza boyu: Küçük"
assert ek == "Pizza üstü: zeytin,mantar"
assert odeme == "Ödeme tipi:Nakit "
assert tutar == "Tutar = 10 TL """""

driver.execute_script("window.scrollBy(0,150)","")
time.sleep(1)
driver.execute_script("window.scrollBy(0,-150)","")
driver.save_screenshot("./result.png")
driver.quit()

