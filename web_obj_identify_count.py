from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()
driver.get("")

web_object_elements = ['object', 'embed', 'img', 'a', 'textarea', 'audio', 'video', 'iframe', 'table', 'input']
# print("Count of web_object_elements", len(web_object_elements))

web_page_elements = set()
wait = WebDriverWait(driver, 1000)
wait.until(EC.presence_of_all_elements_located((By.XPATH,"//*")))
elements = driver.find_elements(By.XPATH, "//*")
for element in elements:
    if element.tag_name in web_object_elements:
        if element.tag_name == "input":
            web_page_elements.add(element.get_attribute("type"))
        web_page_elements.add(element.tag_name)


print(web_page_elements)
print("The count is:", len(web_page_elements))
driver.close()