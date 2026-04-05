import streamlit as st
import joblib
import cv2
import numpy as np
from PIL import Image

# Load trained model
model = joblib.load("pneumonia_model.pkl")

st.set_page_config(page_title="Radiology Assistant", layout="centered")

st.title("AI-Powered Radiology Assistant")
st.write("Upload a chest X-ray image to predict whether it is Normal or Pneumonia.")

uploaded_file = st.file_uploader("Upload X-ray Image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded X-ray Image", use_container_width=True)

    img = np.array(image)

    # IMPORTANT: must match training size
    img = cv2.resize(img, (224, 224))

    img = img / 255.0

    img_flat = img.reshape(1, -1)

    prediction = model.predict(img_flat)[0]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("Pneumonia Detected")
    else:
        st.success("Normal")

    if hasattr(model, "predict_proba"):
        prob = model.predict_proba(img_flat)[0]
        st.write("Confidence:")
        st.write({
            "Normal": float(prob[0]),
            "Pneumonia": float(prob[1])
        })

    st.info("This system is an AI support tool and should not replace professional medical diagnosis.")