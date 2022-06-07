import pyautogui
import time
import threading
import os
import schedule
dir_path = os.path.dirname(os.path.abspath(__file__))


def send_message():
    #threading.Timer(20, send_message).start()

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


    pyautogui.typewrite('This message is automatically sent.', 0.07)
    time.sleep(1)

    pyautogui.write(['enter'])
    time.sleep(1)

    pyautogui.write(['escape'])
    time.sleep(1)

send_message()
schedule.every(20).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)