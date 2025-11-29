# Image Forgery Detection using Error Level Analysis (ELA) & CNN

This project detects forged (tampered) images using **Error Level Analysis (ELA)** and a **Convolutional Neural Network (CNN)**.  
The Flask-based interface allows users to upload an image and instantly receive:

- Authentic or Tampered classification  
- Confidence score  
- ELA visualization highlighting suspicious image regions  

This system is developed using Python, TensorFlow/Keras, OpenCV, Flask, Matplotlib, and supporting libraries.

---

## 🚀 Features

- Real-time automated forgery detection  
- Error Level Analysis (ELA) preprocessing  
- Convolutional Neural Network (CNN)–based classification  
- Clean and user-friendly Flask web interface  
- Accurate confidence percentage  
- Visual display: Original Image + ELA Image  
- Supports JPG, JPEG, PNG, GIF, TIF formats  

---

## 📂 Project Structure

```bash
image-forgery-detection-ELA-CNN/
│
├── main.py                     # Flask Application Entry Point
├── requirements.txt            # Python Dependencies
├── Image_forgery.h5            # Trained CNN Model (Downloaded Separately)
│
├── templates/                  # HTML Templates for Flask
│   ├── index.html
│   ├── upload.html
│   ├── about.html
│   └── result.html
│
├── static/
│   ├── uploads/                # User Uploaded Images
│   └── output/                 # ELA Visualizations & Results
│
└── README.md

---

## 📥 Download Trained Model (Required)

The trained model file **Image_forgery.h5** is not included in this repository because GitHub does not allow large binary files.

👉 **Download the trained model here:**
https://drive.google.com/file/d/1CogtgM-yE-mBgIqFpbUB0v3oRi_nAQvi/view?usp=drive_link


After downloading, place the file in your project root:

```bash
image-forgery-detection-ELA-CNN/
└── Image_forgery.h5
```

> ⚠️ The app will NOT run without this file.
> Make sure the filename remains EXACTLY: **Image_forgery.h5**

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/image-forgery-detection-ELA-CNN.git
cd image-forgery-detection-ELA-CNN
```

### 2️⃣ Install Required Packages

```bash
pip install -r requirements.txt
```

### 3️⃣ Add the Model File

Place the downloaded `Image_forgery.h5` file into the project root.

### 4️⃣ Run the Flask Application

```bash
python main.py
```

Open the application in your browser:

```
http://127.0.0.1:5000/
```

---

## 🧠 How It Works

1. User uploads an image using the web interface.
2. The image is validated and stored in the server directory.
3. System performs **Error Level Analysis (ELA)**:

   * Image is re-saved at 90% quality
   * Difference between original vs. recompressed is extracted
   * ELA highlights inconsistencies caused by tampering
4. ELA image is resized, normalized, and fed into the CNN model.
5. CNN predicts:

   * **Original** or **Tampered**
   * Confidence percentage
6. The result page displays:

   * Original image
   * ELA output
   * Prediction + confidence score

---

## 🛠 Technologies Used

* **Python**
* **Flask**
* **TensorFlow / Keras**
* **OpenCV**
* **Pillow (PIL)**
* **Matplotlib**
* **NumPy**
* **Scikit-Learn**

---

## 🧪 Dataset

This model was trained using a dataset containing:

* Authentic (original) images
* Tampered (forged) images

Forgery types include:

* Copy-move
* Splicing
* Region manipulation
* Color & lighting edits

All training images undergo ELA preprocessing before feeding into the CNN.

---

## 📸 Screenshots (Optional)

Add your screenshots here if needed:

```
![Home Page](<img width="623" height="385" alt="image" src="https://github.com/user-attachments/assets/386427a9-ace2-40f4-8268-80115727b323" />)
![Result Page - Original Image](<img width="560" height="360" alt="image" src="https://github.com/user-attachments/assets/67ee4fdf-25d6-44dd-8186-99cb0c01448e" />)
![Result Page - Tampered Image](<img width="623" height="385" alt="image" src="https://github.com/user-attachments/assets/cc647770-0389-430a-9d74-ddea0b4c6d6b" />)
```



---

## 📌 Future Enhancements

* Deepfake image/video detection
* Bounding box tamper localization
* Transfer learning with VGG16, ResNet, EfficientNet
* Cloud deployment and API support
* Multi-format forensic analysis
* PRNU-based noise pattern detection

---


---

## 📄 License

This project is intended for academic and research use only.

```
