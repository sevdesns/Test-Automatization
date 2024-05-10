from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service =Service("./edgedriver.exe")
driver= webdriver.Edge(service=service)
driver.maximize_window()

""" # 1. istenileni yapıyor mu ? pozitif test
# 2. istenmeyeni yapıyor mu ? negatif test

# internet login sayfasına git https://the-internet.herokuapp.com/login
driver.get("https://the-internet.herokuapp.com/login")
# kullanıcı adı gir
driver.find_element(By.ID,"username").send_keys("test")
#şifre gir
driver.find_element(By.ID,"password").send_keys("asdf")
# log in düğmesine tıkla
driver.find_element(By.CSS_SELECTOR,"button.radius").click()
# yanlış kullanıcı adı Your username is invalid!
mesaj = driver.find_element(By.ID,"flash").text

if "Your password is invalid!" in mesaj:
    print("Ok, yanlış kullanıcı adı doğru çalışıyor ")
else:
    print("hata: yanlış kullanıcı adı çalışmıyor")
# yanlış şifre girince : Your password is invalid!
driver.get("https://the-internet.herokuapp.com/login")
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID,"password").send_keys("asdf")
driver.find_element(By.CSS_SELECTOR,"button.radius").click()
mesaj2 = driver.find_element(By.ID,"flash").text
print("yanlış şifre mesajı:" +mesaj2)

if "Your password is invalid!" in mesaj:
    print("Ok, yanlış şifre doğru çalışıyor ")
else:
    print("hata: yanlış şifre çalışmıyor")
driver.find_element(By.XPATH, "//i[contains(text(),'Logout')]").click()

# ikisi de doğru ise : mesaj : You logged into a secure area! link secure içerecek sayfa da secure area

driver.get("https://the-internet.herokuapp.com/login")
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID,"password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR,"button.radius").click()
mesaj3 = driver.find_element(By.ID,"flash").text
print("mesaj 3 :" + mesaj3)

if "Your logged into a secure area!" in mesaj3:
    print("Ok, doğru bilgiler kullanıcı adı doğru çalışıyor ")
else:
    print("hata: doğru bilgiler çalışmıyor")

link= driver.current_url
if "secure" in link :
    print("OK link secure içeriyor")
else:
    print("HATA: link secure içermiyor ")

dogru_mesaj = driver.find_element(By.CSS_SELECTOR,"h2 i").text
print("doğru mesaj:"+ dogru_mesaj)
if "Secure Area" in dogru_mesaj:
    print("OK, Sayfa başlığı doğru")
else:
    print("Hata: sayfa başlığı yanlış ")

#logout dugmesine tıkla
driver.find_element(By.XPATH, "//i[contains(text(),'Logout')]").click()

# sayfa linkini doğrula
if " login" in driver.current_url:
    print("OK. login sayfasına döndük")
else: print("Hata: login sayfasına dönmedi ")
"""


def login(username, password):
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID,"username").send_keys(username)
    driver.find_element(By.ID,"password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR,"button.radius").click()
    mesaj = driver.find_element(By.ID,"flash").text
    return mesaj
mesaj = login("asdf","xyz")

if "Your password is invalid!" in mesaj:
    print("Ok, yanlış kullanıcı adı doğru çalışıyor ")
else:
    print("hata: yanlış kullanıcı adı çalışmıyor")

mesaj = login("tomsmith","asdf")

if "Your password is invalid!" in mesaj:
    print("Ok, yanlış kullanıcı adı doğru çalışıyor ")
else:
    print("hata: yanlış kullanıcı adı çalışmıyor")

mesaj = login("tomsmith","SuperSecretPassword!")

if "Your logged into a secure area!" in mesaj:
    print("Ok, doğru bilgiler kullanıcı adı doğru çalışıyor ")
else:
    print("hata: doğru bilgiler çalışmıyor")



driver.quit()


