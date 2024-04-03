# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time


# service = Service(exeimport pyautogui
# import time

# # Open Microsoft Word
# pyautogui.hotkey('win', 'r')
# time.sleep(1)
# pyautogui.write('winword')
# pyautogui.press('enter')
# time.sleep(5)  # Adjust as needed for Word to open

# # Click on the Layout tab in Word
# pyautogui.click(100, 100)  # Adjust the coordinates as per your Word interface
# pyautogui.moveTo(300, 200, duration=0.5)  # Assuming the layout tab is at (300, 200)
# pyautogui.click()

# # Select A4 size
# pyautogui.moveTo(400, 300, duration=0.5)  # Assuming the size dropdown is at (400, 300)
# pyautogui.click()
# time.sleep(0.5)
# pyautogui.moveTo(400, 350, duration=0.5)  # Assuming A4 option is at (400, 350)
# pyautogui.click()

# # Paste content from clipboard
# pyautogui.hotkey('ctrl', 'v')

# # Close Wordservice = Service(
# pyautogui.hotkey('alt', 'f4')
# cutable_path="chromedriver.exe")
# driver = webdriver.Chrome(service=service)

# theTitle = input("Enter title : ")
# contents = [];
# # img

# driver.find_element(By.CLASS_NAME, "s_JGcg fFOiLQ eoXdOg CmLV0g yW_5QA tMP70Q").send_keys(
#     f"cover page ebooks for {theTitle}", Keys.ENTER)
