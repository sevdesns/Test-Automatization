import  time
from selenium import  webdriver
from  webdriver_manager.chrome import ChromeDriverManager

driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("http://www.google.com")
time.sleep(2)
driver.quit()