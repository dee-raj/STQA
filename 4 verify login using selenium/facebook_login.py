import time
from selenium import webdriver
from selenium.webdriver.common.by import By
def main():
   driver = webdriver.Chrome()
   url = 'https://www.facebook.com/'
   driver.get(url)
   time.sleep(1)
   email = driver.find_element(By.ID, 'email')
   email.send_keys("youremail@gmail.com")
   time.sleep(1)
   password =driver.find_element(By.ID, "pass")
   password.send_keys("#yourPassw0rd")
   time.sleep(1)
   btn =driver.find_element(By.XPATH , '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')
   btn.click()
   time.sleep(40)
main()
