import streamlit as st
import cv2
import easyocr
import imutils
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Number Plate Recognition", layout="wide")

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

st.title("🚗 Intelligent Number Plate Recognition System")
st.markdown("### Smart Parking & Vehicle Analytics Dashboard")

uploaded = st.file_uploader("Upload Vehicle Image", type=["jpg","png","jpeg"])

if uploaded:

    file_bytes = uploaded.read()

    with open("temp.jpg", "wb") as f:
        f.write(file_bytes)

    img = cv2.imread("temp.jpg")
    img = imutils.resize(img, width=600)

    col1, col2 = st.columns(2)

    with col1:
        st.image(img, channels="BGR", caption="Uploaded Vehicle Image")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)

    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    result = reader.readtext(
        thresh,
        allowlist='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    )

    plate = "Unreadable"

    if result:
        plate = result[0][1]

    code = plate[:2]
    state = states.get(code, "Unknown")

    with col2:
        st.success(f"Detected Plate: {plate}")
        st.info(f"Detected State: {state}")
        st.warning("Status: Vehicle Clear")

    # Log File
    data = {
        "Plate":[plate],
        "State":[state],
        "Time":[datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
    }

    df = pd.DataFrame(data)

    try:
        old = pd.read_csv("vehicle_log.csv")
        df = pd.concat([old, df], ignore_index=True)
    except:
        pass

    df.to_csv("vehicle_log.csv", index=False)

    st.markdown("---")
    st.subheader("📊 Parking Analytics")

    total = len(df)
    unique = df["Plate"].nunique()
    slots = 50
    available = slots - total

    c1, c2, c3 = st.columns(3)

    c1.metric("Occupied Slots", total)
    c2.metric("Available Slots", available)
    c3.metric("Unique Vehicles", unique)

    st.markdown("---")
    st.subheader("📁 Vehicle Entry Logs")
    st.dataframe(df, use_container_width=True)