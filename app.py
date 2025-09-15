import os 
import requests
import streamlit as st
from model_helper import predict as local_predict # local fallback

# Page configuration
st.set_page_config(
    page_title="Car Damage Prediction",
    page_icon="🚗",
    layout="wide"
)

# Custom CSS styling for a polished look
st.markdown(
    """
    <style>
    .main {
        background-color: #f8f9fa;
        border-radius: 12px;
        padding: 8px;
    }
    .uploadedFile {
        border: 2px dashed #4CAF50;
        border-radius: 8px;
        padding: 15px;
        text-align: center;
    }
    .prediction-box {
        background-color: #ffffff;
        padding: 12px;
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        margin-top: 6px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header section
st.title("🚗 Vehicle Damage Detector")
st.caption(
    """
    Let AI detect the type of damage to your car instantly from just an image.  
    """
)

# Read API_URL from env (set this in Hugging Face Space Settings -> Secrets)
API_URL = os.environ.get("API_URL", "").strip()

# File uploader
uploaded_file = st.file_uploader("Upload your car damage image 👇🏼", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image_path = "temp_file.jpg"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.image(uploaded_file, caption="📸 Uploaded Image", width='stretch')

# Predict using external API if provided, otherwise use local model
    with st.spinner("🔍 Analyzing..."):
        prediction = None
        if API_URL:
            try:
                # Send file to external FastAPI endpoint
                with open(image_path, "rb") as f:
                    files = {"file": ("temp_file.jpg", f, "image/jpg")}
                    resp = requests.post(API_URL, files=files, timeout=30)
                if resp.status_code == 200:
                    # Try to parse JSON result (flexible keys)
                    try:
                        data = resp.json()
                        # common keys: "prediction", "predicted_class", "label"
                        prediction = (
                            data.get("prediction")
                            or data.get("predicted_class")
                            or data.get("label")
                            or str(data)
                        )
                    except Exception:
                            # Non-JSON response, show raw text
                            prediction = resp.text
                else:
                    prediction = f"API error {resp.status_code}: {resp.text}"
            except Exception as e:
                prediction = f"Failed to call API: {e}"
        else:
            # local fallback
            try:
                prediction = local_predict(image_path)
            except Exception as e:
                prediction = f"Local model error: {e}"

   
    # Display result in a styled box
    st.markdown(
        f"""
        <div class="prediction-box">
            <h3 style="color:#4CAF50;">✅ Predicted Damage Category: <span style="color:#000000;">{prediction}</span></h3>
        </div>
        """,
        unsafe_allow_html=True
    )

# Footer
st.caption(
    """
    ---
    👩‍💻 **Author:** *Developed by Soobiya Ashfaq*
    """
)
