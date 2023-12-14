from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://linkedin.com/")
time.sleep(2)   
email = driver.find_element(By.ID , "session_key")
email.send_keys("uremail@gmail.com")
time.sleep(2)
password = driver.find_element(By.ID , "session_password")
password.send_keys("pass#69")
time.sleep(2)
btn = driver.find_element(By.XPATH , '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')
btn.click()
time.sleep(222)
