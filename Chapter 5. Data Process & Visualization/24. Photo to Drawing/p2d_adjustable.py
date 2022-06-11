import numpy as np
import cv2
import os
import time

dir_path = os.path.dirname(os.path.abspath(__file__))
ff = np.fromfile(dir_path + '\\pic.png', np.uint8)
img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)
img = cv2.resize(img, dsize=(0,0), fx=1.0, fy=1.0, interpolation=cv2.INTER_LINEAR)

def onChange(pos):
    pass

cv2.namedWindow("Trackbar Windows")

cv2.createTrackbar("sigma_s", "Trackbar Windows", 0, 200, onChange)
cv2.createTrackbar("sigma_r", "Trackbar Windows", 0, 100, onChange)

cv2.setTrackbarPos("sigma_s", "Trackbar Windows", 100)
cv2.setTrackbarPos("sigma_r", "Trackbar Windows", 10)

sigma_s_hist = 0
sigma_r_hist = 0
while True:
    if cv2.waitKey(100) == ord('q'):
        break

    sigma_s_value = cv2.getTrackbarPos("sigma_s", "Trackbar Windows")
    sigma_r_value = cv2.getTrackbarPos("sigma_r", "Trackbar Windows") / 100.0

    if((sigma_s_value != sigma_s_hist) | (sigma_s_value != sigma_r_hist)):
        cartoon_img = cv2.stylization(img, sigma_s=sigma_s_value, sigma_r=sigma_r_value)
        cv2.imshow("Trackbar Windows", cartoon_img)

    sigma_s_hist, sigma_r_hist = sigma_s_value, sigma_r_value

cv2.destroyAllWindows()