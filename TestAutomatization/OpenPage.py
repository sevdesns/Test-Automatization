import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


service =Service("./edgedriver.exe")

driver= webdriver.Edge(service=service)
driver.maximize_window()
driver.maximize_window()
driver.get("https://www.apple.com")
time.sleep(1)
print(driver.title)
apple = driver.current_window_handle
driver.switch_to.new_window("tab")
driver.get("https://www.tesla.com")
time.sleep(2)
print(driver.title)
tesla= driver.window_handles[1]
driver.switch_to.window(apple)
print(driver.title)
time.sleep(2)
driver.switch_to.window(tesla)
print(driver.title)
driver.switch_to.window(apple)
time.sleep(1)
driver.quit()

""" 
def  change_page(title):
   for page in driwer.window_handles:
       driver.switch_to.window(sayfa)
       if title in driver.title.lower(): 
          break
"""