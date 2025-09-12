<div align="center">

  
<h1 align="center"> 🚗 Vehicle Damage Detection App </h1>

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Live%20Demo-Streamlit-blue)](https://huggingface.co/spaces/sashfaq911/Car_Damage_Detector)

An end-to-end AI application for vehicle damage classification using **FastAPI** (backend), **Streamlit** (frontend), and **PyTorch** (deep learning).

This app let's you drag and drop an image of a car and it will tell you what kind of damage it has.
The model is trained on third quarter front and rare view hence the picture should capture the third quarter front or rare view of a car. 

</div>

<p align="center">
  <a href="#problem-statement">Problem Statement</a> •
  <a href="#features">Features</a> •
  <a href="#app-overview-&-usage">App Overview & Usage</a> •
  <a href="#live-demo">Live Demo</a> •
  <a href="#installation-&-deployment">Installation</a> •
  <a href="#acknowledgements">Acknowledgements</a> •
  <a href="#license">License</a>
</p>


## 🛑 Problem Statement  <a name="problem-statement"></a>
Vehicle accidents often result in damages that need quick assessment for insurance claims and repair cost estimation. Manual inspection is time-consuming, subjective, and prone to human error. There is a need for an automated solution that can classify the type of car damage accurately and efficiently, making the claims and repair process faster and more reliable.

## 💡 Solution Statement  
This project provides an AI-powered vehicle damage detection system built on a ResNet50 deep learning model. The system is deployed on Hugging Face Spaces, combining a FastAPI backend for inference and a Streamlit frontend for user interaction. Users can upload an image of a damaged car, and the application instantly classifies the type of damage, showcasing practical skills in computer vision, API design, and full-stack AI deployment.

## ✨ Features <a name="features"></a>
- **User-Friendly Interface** → Upload a car image and get instant damage classification through a clean **Streamlit UI**.  
- **Six-Class Classification** → Detects and classifies damages into:  
  - Front Normal  
  - Front Crushed  
  - Front Breakage  
  - Rear Normal  
  - Rear Crushed  
  - Rear Breakage  
- **Deep Learning Backbone** → Fine-tuned **ResNet50** model for accurate vehicle damage detection.  
- **Modern Architecture** →  
  - **FastAPI backend** serving predictions via REST API  
  - **Streamlit frontend** for interactive visualization  
- **Seamless Deployment** → End-to-end app deployed on **Hugging Face Spaces**, accessible from any browser.  
- **Cross-Device Compatibility** → Runs efficiently on both **CPU and GPU** environments.  
- **API Tested** → Backend validated with **Postman** for reliability and easy integration with other systems.  


## 🖥️ App Overview & Usage <a name="app-overview-&-usage"></a>

![app](app_screenshot.png)

### Model Details
1. Used ResNet50 for transfer learning
2. Model was trained on around 1700 images with 6 target classes
   1. Front Normal
   1. Front Crushed
   1. Front Breakage
   1. Rear Normal
   1. Rear Crushed
   1. Rear Breakage
9. The accuracy on the validation set was around 80%

## 🌐 Live Demo <a name="live-demo"></a>

Try the app here: **[Vehicle Damage Detection](https://huggingface.co/spaces/sashfaq911/Car_Damage_Detector)**


## 🛠️ Tech Stack

- **Python**, **PyTorch**
- **FastAPI** (backend)
- **Streamlit** (frontend)
- **Docker** (deployment)  


## 📦 Project Structure

```bash
Vehicle_Damage_Detection/
│
├── assets/                         
│   ├── demo.gif                    # Demo of the Streamlit web app
│   ├── screenshot.png              # Screenshot of Streamlit web app
│
├── artifacts/                      # Serialized models and scalers
│   ├── model_rest.joblib           # XGBoost Model for users > 25 years (adult users)
│   ├── model_young.joblib          # Linear Regression Model for users <= 25 years (younger users)
│   ├── scaler_rest.joblib          # StandardScaler for older group
│   └── scaler_young.joblib         # StandardScaler for younger group
│
├── LICENSE                         # Apache License file
├── README.md                       # Project documentation
├── main.py                         # Streamlit app logic
├── prediction_helper.py            # Preprocessing & prediction logic
└── requirements.txt                # Python dependencies
```


## 🚀 Installation & Deployment <a name="installation-&-deployment"></a>
The app is deployed on **Hugging Face Spaces** and accessible here:  
👉 [Live Demo](https://huggingface.co/spaces/sashfaq911/Car_Damage_Detector)  

You can run this project in two ways: locally (with Python & pip) or using Docker.

### ⚡ Option 1 — Run Locally

#### Prerequisites:  
- Python 3.10+

1. **Clone the repo**:
   ```bash
   git clone https://github.com/sashfaq911/Vehicle_Damage_Detection.git
   cd Vehicle_Damage_Detection
   ```
2. **Install dependencies**:   
   ```commandline
    pip install -r requirements.txt
   ```
3. **Run FastAPI backend**:
   Start the backend API server:  
   ```commandline
    uvicorn backend:app --reload --host 0.0.0.0 --port 8000
   ```
   - Swagger Docs → http://127.0.0.1:8000/docs
   - Prediction endpoint → POST http://127.0.0.1:8000/predict
     
5. **Run the Streamlit frontend**:
   Open a second terminal and run:   
   ```commandline
    streamlit run app.py
   ```

### 🐳 Option 2 — Run with Docker

Build the image
```commandline
docker build -t car-damage-app .
```

Run container exposing both ports
```commandline
docker run -p 8000:8000 -p 8501:8501 car-damage-app
```
- Backend → http://localhost:8000
- Frontend → http://localhost:8501


## 🙏 Acknowledgements <a name="acknowledgements"></a>

A special thanks to [Dhaval Patel](https://www.linkedin.com/in/dhavalsays/) and [Hemanand Vadivel](https://www.linkedin.com/in/hemvad/) for their guidance through the [CodeBasics Gen AI & Data Science BootCamp](https://codebasics.io/bootcamps/dashboard/ai-data-science-bootcamp-with-virtual-internship). This project has been an invaluable learning experience and a key milestone in my data science journey!


## 📄 License <a name="license"></a>

This project is licensed under the **Apache License 2.0**. See the [LICENSE](./LICENSE) file for details.



## ❤️  Support

Contributions, issues, and suggestions are welcome!

Give a ⭐️ if you like this project!
