import streamlit as st
import cv2
import easyocr
import imutils

reader = easyocr.Reader(['en'])

states = {
    "DL":"Delhi",
    "MH":"Maharashtra",
    "PB":"Punjab",
    "KA":"Karnataka",
    "UP":"Uttar Pradesh",
    "TN":"Tamil Nadu"
}

st.title("🚗 Intelligent Number Plate Recognition System")

uploaded = st.file_uploader("Upload Vehicle Image", type=["jpg","png","jpeg"])

if uploaded:

    file_bytes = uploaded.read()

    with open("temp.jpg", "wb") as f:
        f.write(file_bytes)

    img = cv2.imread("temp.jpg")
    img = imutils.resize(img, width=600)

    st.image(img, channels="BGR", caption="Uploaded Image")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    result = reader.readtext(thresh)

    plate = "Unreadable"

    if result:
        plate = result[0][1]

    code = plate[:2]

    st.success(f"Detected Plate: {plate}")
    st.info(f"Detected State: {states.get(code,'Unknown')}")