import cv2
import numpy as np

img = cv2.imread("outputs/detected_plate.jpg")

h, w = img.shape[:2]

pts1 = np.float32([
    [20,20],
    [w-20,20],
    [20,h-20],
    [w-20,h-20]
])

pts2 = np.float32([
    [0,0],
    [w,0],
    [0,h],
    [w,h]
])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
result = cv2.warpPerspective(img, matrix, (w,h))

cv2.imwrite("outputs/perspective_fixed.jpg", result)

print("Perspective Correction Complete")