import pyautogui
import time

# Open Microsoft Word
pyautogui.hotkey('win', 'r')
time.sleep(1)
pyautogui.write('winword')
pyautogui.press('enter')
time.sleep(5)  # Adjust as needed for Word to open

# Select Blank Document
pyautogui.hotkey('ctrl', 'n')  # Open a new document (assuming no documents are open)
time.sleep(2)  # Adjust as needed for Word to open a new document

# Click on the Layout tab in Word
pyautogui.click(100, 100)  # Adjust the coordinates as per your Word interface
pyautogui.moveTo(300, 200, duration=0.5)  # Assuming the layout tab is at (300, 200)
pyautogui.click()

# Select Size
pyautogui.moveTo(400, 300, duration=0.5)  # Assuming the size dropdown is at (400, 300)
pyautogui.click()
time.sleep(0.5)

# Select A4
pyautogui.moveTo(400, 350, duration=0.5)  # Assuming A4 option is at (400, 350)
pyautogui.click()

# Paste content from clipboard
pyautogui.hotkey('ctrl', 'v')

# Close Word (optional)
# pyautogui.hotkey('alt', 'f4')
