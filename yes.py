from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"

service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Get user input
TheItem = input("Enter Item name: ")
TheLevel = input("Enter difficulty: ")
ThePrompt = f"Write me a blog post about {TheItem} for beginners {TheLevel}"

# Open OpenAI Chat platform
driver.get("https://chat.openai.com")

# Wait for page to load
time.sleep(5)

# Find and input prompt
prompt_textarea = driver.find_element(By.ID, "prompt-textarea")
prompt_textarea.send_keys(ThePrompt)

# Close browser after 10 seconds
time.sleep(10)
driver.close()
