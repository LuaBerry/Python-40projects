import pyautogui
import time
import os

dir_path = os.path.dirname(os.path.abspath(__file__))

picPos = pyautogui.locateOnScreen(dir_path + '\\pic0.png')
print(picPos)

if picPos == None:
    picPos = pyautogui.locateOnScreen(dir_path + '\\pic1.png')
    print(picPos)
if picPos == None:
    picPos = pyautogui.locateOnScreen(dir_path + '\\pic2.png')
    print(picPos)
if picPos == None:
    exit()

clickPos = pyautogui.center(picPos)
pyautogui.moveTo(clickPos)
pyautogui.doubleClick()


pyautogui.typewrite('This message is automatically sent.', 0.1)
time.sleep(1)

pyautogui.write(['enter'])
time.sleep(1)

pyautogui.write(['escape'])