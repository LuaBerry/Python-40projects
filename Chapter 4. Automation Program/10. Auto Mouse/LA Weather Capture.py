import pyautogui
import time
import os

pyautogui.moveTo(1425, 431, 0.2)
pyautogui.click()
time.sleep(0.5)

pyautogui.typewrite("LA Weather", interval=0.1)
time.sleep(0.5)

pyautogui.typewrite(['enter'])
time.sleep(1)

start_x = 980; start_y = 280
end_x = 1650; end_y = 670

dir_path = os.path.dirname(os.path.abspath(__file__))
pyautogui.screenshot(dir_path + '\\LA Weather.png',
    region=(start_x, start_y, end_x-start_x, end_y-start_y))