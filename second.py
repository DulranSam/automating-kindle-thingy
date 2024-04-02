from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Specify the path to chromedriver.exe
service = Service(executable_path="C:/Program Files/Google/Chrome/Application/chrome.exe")


# Initialize the Chrome webdriver with the specified service
driver = webdriver.Chrome(service=service)

# Open Google
driver.get("https://www.google.com/")

# Find the search input element using its name attribute
input_element = driver.find_element(By.NAME, "q")

# Input the search query
input_element.send_keys("Veloxal", Keys.ENTER)

# Wait for 10 seconds (you may adjust this as needed)
time.sleep(10)

# Close the browser window
driver.quit()
