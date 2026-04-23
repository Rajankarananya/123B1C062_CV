import cv2
import imutils
import easyocr
import numpy as np
import csv
from datetime import datetime

reader = easyocr.Reader(['en'])

states = {
    "DL":"Delhi",
    "MH":"Maharashtra",
    "PB":"Punjab",
    "KA":"Karnataka",
    "UP":"Uttar Pradesh",
    "TN":"Tamil Nadu",
    "RJ":"Rajasthan",
    "WB":"West Bengal"
}

stolen = ["DL1", "MH14AB1234", "PB7"]

img_path = "dataset/State-wise_OLX/DL/DL1.jpg"
code = img_path.split("/")[-2]

img = cv2.imread(img_path)
img = imutils.resize(img, width=600)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17)

edged = cv2.Canny(gray, 30, 200)

cnts = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:20]

plate = None
detected_text = "Unreadable"
result = []

for c in cnts:
    x, y, w, h = cv2.boundingRect(c)
    ratio = w / h

    if ratio > 2 and ratio < 6 and w > 100:
        plate = img[y:y+h, x:x+w]
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        break

cv2.imwrite("outputs/detected_plate.jpg", img)

if plate is not None:

    plate_gray = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY)
    plate_gray = cv2.resize(plate_gray, None, fx=3, fy=3)
    plate_gray = cv2.GaussianBlur(plate_gray, (3,3), 0)

    _, plate_thresh = cv2.threshold(
        plate_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    cv2.imwrite("outputs/cropped_plate.jpg", plate_thresh)

    result = reader.readtext(
        plate_thresh,
        allowlist='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    )

if result:
    detected_text = result[0][1]
else:
    result2 = reader.readtext(
        img,
        allowlist='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    )
    if result2:
        detected_text = result2[0][1]

print("Detected Plate:", detected_text)
print("State Code:", code)
print("Detected State:", states.get(code, "Unknown"))

if detected_text in stolen or code in stolen:
    print("STOLEN VEHICLE ALERT")
else:
    print("Vehicle Clear")

duplicate = False

try:
    with open("vehicle_log.csv", "r") as file:
        if detected_text in file.read():
            duplicate = True
except:
    pass

if duplicate:
    print("Duplicate Vehicle Detected")
else:
    print("New Vehicle Entry")

with open("vehicle_log.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        detected_text,
        code,
        states.get(code, "Unknown"),
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ])

print("Log Saved")
try:
    with open("vehicle_log.csv", "r") as file:
        total = len(file.readlines())
except:
    total = 0

slots = 50
occupied = total
available = slots - occupied

print("Occupied Slots:", occupied)
print("Available Slots:", available)
try:
    with open("vehicle_log.csv", "r") as file:
        lines = file.readlines()
        unique = set()

        for line in lines:
            plate = line.split(",")[0].strip()
            unique.add(plate)

    print("Unique Vehicles:", len(unique))

except:
    print("Unique Vehicles: 0")