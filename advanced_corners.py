import cv2
import numpy as np

img = cv2.imread("dataset/State-wise_OLX/DL/DL1.jpg")
img = cv2.resize(img, (600, 400))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 50, 0.01, 10)

if corners is not None:
    corners = corners.astype(int)

    for i in corners:
        x, y = i.ravel()
        cv2.circle(img, (x, y), 4, (0, 255, 0), -1)

cv2.imwrite("outputs/advanced_corners.jpg", img)

print("Advanced Corner Detection Complete")