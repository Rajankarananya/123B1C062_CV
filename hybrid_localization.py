import cv2
import imutils
import numpy as np

img = cv2.imread("dataset/State-wise_OLX/DL/DL1.jpg")
img = imutils.resize(img, width=600)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Segmentation
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# Contours
cnts = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

for c in cnts:
    x, y, w, h = cv2.boundingRect(c)
    ratio = w / h

    if ratio > 2 and ratio < 6 and w > 100:

        roi = gray[y:y+h, x:x+w]

        corners = cv2.goodFeaturesToTrack(roi, 20, 0.01, 5)

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

        if corners is not None:
            corners = corners.astype(int)

            for i in corners:
                cx, cy = i.ravel()
                cv2.circle(img, (x+cx, y+cy), 3, (0,0,255), -1)

        break

cv2.imwrite("outputs/hybrid_localization.jpg", img)

print("Hybrid Localization Complete")