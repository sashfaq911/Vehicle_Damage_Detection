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
  <a href="#installation">Installation</a> •
  <a href="#acknowledgements">Acknowledgements</a> •
  <a href="#license">License</a>
</p>


## 📌 Problem Statement  <a name="problem-statement"></a>


## 💡 Solution Statement  

## ✨ Features <a name="features"></a>
- Upload a car image and get instant damage classification.
- Images are classified into 6 classes:
  - Front Normal
  - Front Crushed
  - Front Breakage
  - Rear Normal
  - Rear Crushed
  - Rear Breakage
- Uses a fine-tuned **Deep Learning model** (ResNet50) to detect car damage types.
- Uses a **Streamlit frontend** for an interactive web UI.
- Uses a **FastAPI backend** serving predictions as an API.
- Device-agnostic (runs on both CPU and GPU).
- REST API tested with Postman for seamless integration.


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


## 🚀 Installation <a name="installation"></a>
The app is deployed on **Hugging Face Spaces** and accessible here:  
👉 [Live Demo](https://huggingface.co/spaces/sashfaq911/Car_Damage_Detector)  

Or run locally: 
### Prerequisites:  
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
    Open a decond terminal and run:   
   ```commandline
    streamlit run app.py
   ```

### 🐳 Run with Docker

If you prefer containers:
# Build the image
docker build -t car-damage-app .

# Run container exposing both ports
docker run -p 8000:8000 -p 8501:8501 car-damage-app


## 🙏 Acknowledgements <a name="acknowledgements"></a>

A special thanks to [Dhaval Patel](https://www.linkedin.com/in/dhavalsays/) and [Hemanand Vadivel](https://www.linkedin.com/in/hemvad/) for their guidance through the [CodeBasics Gen AI & Data Science BootCamp](https://codebasics.io/bootcamps/dashboard/ai-data-science-bootcamp-with-virtual-internship). This project has been an invaluable learning experience and a key milestone in my data science journey!


## 📄 License <a name="license"></a>

This project is licensed under the **Apache License 2.0**. See the [LICENSE](./LICENSE) file for details.



## ❤️  Support

Contributions, issues, and suggestions are welcome!

Give a ⭐️ if you like this project!
