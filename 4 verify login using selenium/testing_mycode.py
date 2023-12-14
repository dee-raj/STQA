import time
from selenium import webdriver
from selenium.webdriver.common.by import By
def main():
   driver = webdriver.Chrome()
   url = 'http://127.0.0.1:5500/4%20verify%20login%20using%20selenium/myLoginPage.html'
   driver.get(url)
   time.sleep(1)
   email = driver.find_element(By.ID, 'username')
   email.send_keys("youremail@gmail.com")
   time.sleep(1)
   password =driver.find_element(By.ID, "password")
   password.send_keys("yourpassword")
   time.sleep(1)
   btn =driver.find_element(By.XPATH , '/html/body/div/button')
   btn.click()
   time.sleep(40)
main()
