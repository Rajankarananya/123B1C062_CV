import cv2
import numpy as np

img = cv2.imread("dataset/State-wise_OLX/DL/DL1.jpg")
img = cv2.resize(img, (600,400))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

h, w = gray.shape
seed = (w//2, h//2)

mask = np.zeros((h+2, w+2), np.uint8)

cv2.floodFill(gray, mask, seedPoint=seed, newVal=255, loDiff=20, upDiff=20)

cv2.imwrite("outputs/region_growing.jpg", gray)

print("Region Growing Complete")