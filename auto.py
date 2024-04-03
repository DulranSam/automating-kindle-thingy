from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
import time

# Path to your ChromeDriver executable
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

jsonArray = [{"id": 1, "username": "buzz", "password": "velo123"},
             {"id": 2, "username": "vex", "password": "kek"}]

driver.get("https://chat.openai.com/")
time.sleep(5)  # Adjust as needed for page load
prompt_textarea = driver.find_element(By.ID, "prompt-textarea")
prompt_textarea.send_keys(f"${jsonArray}" + (Keys.SHIFT + Keys.ENTER) * 2 + "Put the data inside returnData into a nice readable format like an ebook. Only give me the outcome")
prompt_textarea.send_keys(Keys.CONTROL, 'a')  # Select all text
prompt_textarea.send_keys(Keys.CONTROL, 'c')  # Copy text to clipboard

