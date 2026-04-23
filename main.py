import cv2
import imutils
import easyocr

reader = easyocr.Reader(['en'])

# -------------------------
# STATE MAP
# -------------------------
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

# stolen db
stolen = ["DL1", "MH14AB1234", "PB7"]

# -------------------------
img_path = "dataset/State-wise_OLX/DL/DL1.jpg"

code = img_path.split("/")[-2]

img = cv2.imread(img_path)
img = imutils.resize(img, width=600)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17)

_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

cnts = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:20]

plate = None
detected_text = "Unreadable"

for c in cnts:
    x, y, w, h = cv2.boundingRect(c)
    ratio = w / h

    if ratio > 2 and ratio < 6 and w > 100:
        plate = img[y:y+h, x:x+w]
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        break

cv2.imwrite("outputs/detected_plate.jpg", img)

if plate is not None:
    gray_plate = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY)
    gray_plate = cv2.resize(gray_plate, None, fx=2, fy=2)
    _, plate_thresh = cv2.threshold(gray_plate, 120, 255, cv2.THRESH_BINARY)

    result = reader.readtext(plate_thresh)

    if result:
        detected_text = result[0][1]

# -------------------------
print("Detected Plate:", detected_text)
print("State Code:", code)
print("Detected State:", states.get(code, "Unknown"))

if detected_text in stolen or code in stolen:
    print("🚨 STOLEN VEHICLE ALERT 🚨")
else:
    print("Vehicle Clear")