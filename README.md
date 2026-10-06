# 🌱 AI-Based Crop Disease Detection System

## 📌 Project Overview

The AI-Based Crop Disease Detection System is a machine learning application that helps farmers and agricultural experts identify crop diseases from leaf images. Users can upload an image of a plant leaf, and the system predicts whether the crop is healthy or affected by a disease.

The project provides disease detection, confidence scores, disease information, and basic recommendations for crop management.

---

## 🎯 Features

* Upload crop leaf images
* Detect plant diseases using AI/ML models
* Display prediction confidence
* Show disease information
* Provide crop care recommendations
* User-friendly Streamlit interface

---

## 🛠️ Technologies Used

* Python
* Streamlit
* TensorFlow / Keras
* NumPy
* Pillow (PIL)
* Machine Learning
* Computer Vision

---

## 📂 Project Structure

```text
crop_detection/
│
├── app.py                 # Main Streamlit application
├── model.h5               # Trained disease detection model
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
└── sample_images/         # Test images
```

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/aaduritherisha-gif/crop_detection.git
cd crop_detection
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

---

## 📸 How It Works

1. Upload a crop leaf image.
2. The image is preprocessed.
3. The AI model analyzes the image.
4. The system predicts the disease.
5. Results and recommendations are displayed.

---

## 🌾 Applications

* Smart Agriculture
* Precision Farming
* Crop Monitoring
* Early Disease Detection
* Farmer Assistance Systems

---

## 🔮 Future Enhancements

* Multiple crop support
* Real-time camera detection
* Disease severity estimation
* Treatment recommendations
* Multi-language support
* Cloud deployment

---

## 👩‍💻 Author

**Therisha Aaduri**

LinkedIn: https://www.linkedin.com/in/therisha-aaduri-9040ba3b

---

## 📜 License

This project is developed for educational and research purposes.
