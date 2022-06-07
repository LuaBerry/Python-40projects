import pyautogui
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