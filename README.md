<div align="center">

  
<h1 align="center"> 🚗 Vehicle Damage Detection App </h1>

This app let's you drag and drop an image of a car and it will tell you what kind of damage it has.
The model is trained on third quarter front and rare view hence the picture should capture the third quarter front or rare view of a car. 

![app](app_screenshot.png)

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

Try the app here: **[Vehicle Damage Detection](https://premium-predictor-app.streamlit.app/)**


## 🛠️ Tech Stack

- **Python**, **PyTorch**
- **FastAPI** (backend)
- **Streamlit** (frontend)
- **Docker** (optional for deployment)  


## 📦 Project Structure

```bash
Health_Insurance_Premium_Predictor/
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


## 🚀 Deployment <a name="deployment"></a>
The app is deployed on **Render** and accessible here:  
👉 [Live Demo](https://your-app-url.onrender.com)  

Or run locally: 
### Prerequisites:  
- Python 3.10+

1. **Clone the repo**:
   ```bash
   git clone https://github.com/sashfaq911/health-insurance-premium-predictor.git
   cd health-insurance-premium-predictor
   ```
2. **Install dependencies**:   
   ```commandline
    pip install -r requirements.txt
   ```
3. **Run PastAPI backend**:   
   ```commandline
    uvicorn app:app --reload
   ```
4. **Run the Streamlit frontend**:   
   ```commandline
    streamlit run app.py
   ```

## 📬 API Usage 

**Endpoint:** 
```commandline
/predict
```
**Method:** POST

**Body:** Image file 
```commandline
(multipart/form-data)
```
Example with curl:
```bash
curl -X POST "https://your-app-url.onrender.com/predict" \
  -F "file=@car.jpg"
```

## 🙏 Acknowledgements <a name="acknowledgements"></a>

A special thanks to [Dhaval Patel](https://www.linkedin.com/in/dhavalsays/) and [Hemanand Vadivel](https://www.linkedin.com/in/hemvad/) for their guidance through the [CodeBasics Gen AI & Data Science BootCamp](https://codebasics.io/bootcamps/dashboard/ai-data-science-bootcamp-with-virtual-internship). This project has been an invaluable learning experience and a key milestone in my data science journey!


## 📄 License <a name="license"></a>

This project is licensed under the **Apache License 2.0**. See the [LICENSE](./LICENSE) file for details.



## ❤️  Support

Contributions, issues, and suggestions are welcome!

Give a ⭐️ if you like this project!
