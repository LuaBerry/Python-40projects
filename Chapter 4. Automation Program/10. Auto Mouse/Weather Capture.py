import pyautogui
import time
import os

regions = ['Los Angeles', 'Seattle', 'New York', 'San Francisco']

for city in regions:
    pyautogui.moveTo(1200, 64, 0.2)
    pyautogui.click()
    time.sleep(0.2)

    pyautogui.typewrite("google.com", interval=0.1)
    pyautogui.typewrite(['enter'])
    time.sleep(0.5)

    pyautogui.moveTo(1430, 510, 0.2)
    pyautogui.click()
    pyautogui.typewrite(city + " Weather", interval=0.1)
    time.sleep(0.2)

    pyautogui.typewrite(['enter'])
    time.sleep(2)

    start_x = 980; start_y = 280
    end_x = 1650; end_y = 670

    dir_path = os.path.dirname(os.path.abspath(__file__))
    file_path = dir_path + "\\" + city + " Weather.png"
    pyautogui.screenshot(file_path, region=(start_x, start_y, end_x-start_x, end_y-start_y))