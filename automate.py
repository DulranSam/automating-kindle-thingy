from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from  selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path="chromedriver.exe");
driver = webdriver.Chrome(service=service);


Title = input("Enter book title : ")
Subtitle = input("Enter Subtitle : ")
Edition = input("Enter Edition : ")

driver.get("https://kdp.amazon.com/en_US/title-setup/kindle/new/details?ref_=cr_ti")
input_element = driver.find_element(By.CLASS_NAME,"a-input-text a-form-normal jele-character-counter-input lock-needs-hidden")
input_element.send_keys(Title)
input_element = driver.find_element(By.CLASS_NAME,"a-input-text a-form-normal jele-character-counter-input lock-needs-hidden")
input_element.send_keys(Subtitle)
input_element = driver.find_element(By.CLASS_NAME,"a-input-text a-form-normal jele-character-counter-input lock-needs-hidden")
input_element.send_keys(Edition)

time.sleep(10)
driver.quit()