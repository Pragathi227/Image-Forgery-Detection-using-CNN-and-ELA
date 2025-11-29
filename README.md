Image Forgery Detection using ELA & CNN

This project detects forged (tampered) images using Error Level Analysis (ELA) and a Convolutional Neural Network (CNN).
A lightweight Flask web application allows users to upload an image and instantly view:

Whether the image is Authentic or Tampered

The confidence score

The ELA visualization highlighting suspicious regions

This system is built using Python, TensorFlow/Keras, OpenCV, and Flask.

🚀 Features

✔ Automated image forgery detection

✔ Error Level Analysis (ELA) preprocessing

✔ Custom-trained CNN model

✔ Flask-based web interface

✔ Real-time prediction

✔ ELA heatmaps for visual forensics

✔ Supports JPG, PNG, JPEG, GIF, TIF

📂 Project Structure
image-forgery-detection-ELA-CNN/
│
├── main.py
├── requirements.txt
├── templates/
│   ├── index.html
│   ├── upload.html
│   ├── about.html
│   └── result.html
│
├── static/
│   ├── uploads/
│   └── output/
│
└── (Model file must be added manually – see below)

🔥 Download Model File (Required)

The trained CNN model (Image_forgery.h5) is stored on Google Drive due to GitHub file size limits.

📥 Download the Model File
👉 https://drive.google.com/file/d/1CogtgM-yE-mBgIqFpbUB0v3oRi_nAQvi/view?usp=drive_link

After downloading, place it in your project root folder:

/image-forgery-detection-ELA-CNN/Image_forgery.h5

🧠 How the System Works

User uploads an image

System performs Error Level Analysis (ELA)

ELA image is passed to CNN

CNN predicts Original / Tampered

Flask displays prediction + ELA heatmap

⚙️ Installation
1. Clone the repository
git clone https://github.com/yourusername/image-forgery-detection-ELA-CNN.git

2. Install dependencies
pip install -r requirements.txt

3. Add the model file

Place the downloaded file here:

/Image_forgery.h5

4. Run the Flask app
python main.py


Open in browser:

http://127.0.0.1:5000/

📸 Screenshots

Home Page 
<img width="2710" height="1385" alt="image" src="https://github.com/user-attachments/assets/6a7e14b7-0236-43a3-8b79-ef82a419c00c" />

About Page
<img width="2623" height="1385" alt="image" src="https://github.com/user-attachments/assets/386427a9-ace2-40f4-8268-80115727b323" />

Result Page - Original Image
<img width="2560" height="1360" alt="image" src="https://github.com/user-attachments/assets/67ee4fdf-25d6-44dd-8186-99cb0c01448e" />

Result Page - Tampered Image
<img width="2623" height="1385" alt="image" src="https://github.com/user-attachments/assets/cc647770-0389-430a-9d74-ddea0b4c6d6b" />


📘 Technologies Used

Python

Flask

TensorFlow / Keras

OpenCV

Matplotlib

Numpy

PIL (Python Imaging Library)

🧪 Dataset

Training dataset includes two categories:

Authentic Images

Tampered/Forged Images

Dataset collected and compiled from multiple open sources and ELA-generated modifications.

🛑 Note

The CNN model is not included in the GitHub repository due to size constraints.
Please download it from the provided Google Drive link.

📄 License

This project is for academic and educational purposes.
