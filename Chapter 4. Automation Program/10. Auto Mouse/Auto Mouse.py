import pyautogui
import time

pyautogui.moveTo(1425, 431, 0.2)
pyautogui.click()
time.sleep(0.5)

pyautogui.typewrite("LA Weather", interval = 0.1)
time.sleep(0.5)

pyautogui.write(["enter"])
time.sleep(1)