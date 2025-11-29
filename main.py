from flask import Flask, render_template, request, redirect
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
import matplotlib.pyplot as plt
import numpy as np
import os
import cv2 
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from tensorflow.keras import layers
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras import layers, models
from tensorflow.keras.utils import load_img, img_to_array

UPLOAD_FOLDER = 'static/uploads/'



app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = '1a2b3c4d5e'


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif','tif'])
class_names = ['Authenticated/Original', 'Tampered']
img_height = 224
img_width = 224
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# http://localhost:5000/pythinlogin/home - this will be the home page, only accessible for loggedin users
@app.route('/')
def home():
    # Check if user is loggedin
        
        # User is loggedin show them the home page
    return render_template('index.html')
    # User is not loggedin redirect to login page

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/home')
def home1():
    return render_template('home.html')
    # User is not loggedin redirect to login page



@app.route('/upload_image', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    print(file)
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        print(path)
        num_classes = 2
        model = models.Sequential([
        layers.Rescaling(1./255, input_shape=(img_height, img_width, 3)),
        layers.Conv2D(16, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(32, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(64, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(num_classes)
        ])
        model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

        model.load_weights("Image_forgery.h5")

        test_data_path = path

        img = load_img(
            test_data_path, target_size=(img_height, img_width)
        )
        img_array = img_to_array(img)
        img_array = tf.expand_dims(img_array, 0) # Create a batch

        predictions = model.predict(img_array)
        score = tf.nn.softmax(predictions[0])

        print(
            "This image is {} with a {:.2f} percent confidence."
            .format(np.argmax(score), 100 * np.max(score))
        )
        if np.argmax(score)==0:
             class1="This image  Authenticated/Original with a confidence of"
        else:
             class1="This image is Forged/Tampered with a confidence of"
        
        plot = get_plot(path)
        plot.savefig(os.path.join('static', 'images', 'plot.png'))


        return render_template('home.html', aclass=class1,ascore=100 * np.max(score),class2=np.argmax(score))
def compute_ela_cv(path, quality):
    temp_filename = 'temp_file_name.jpg'
    SCALE = 15
    orig_img = cv2.imread(path)
    orig_img = cv2.cvtColor(orig_img, cv2.COLOR_BGR2RGB)
    
    cv2.imwrite(temp_filename, orig_img, [cv2.IMWRITE_JPEG_QUALITY, quality])

    # read compressed image
    compressed_img = cv2.imread(temp_filename)

    # get absolute difference between img1 and img2 and multiply by scale
    diff = SCALE * cv2.absdiff(orig_img, compressed_img)
    return diff


def convert_to_ela_image(path, quality):
    temp_filename = 'temp_file_name.jpg'
    ela_filename = 'temp_ela.png'
    image = Image.open(path).convert('RGB')
    image.save(temp_filename, 'JPEG', quality = quality)
    temp_image = Image.open(temp_filename)

    ela_image = ImageChops.difference(image, temp_image)

    extrema = ela_image.getextrema()
    max_diff = max([ex[1] for ex in extrema])
    if max_diff == 0:
        max_diff = 1

    scale = 255.0 / max_diff
    ela_image = ImageEnhance.Brightness(ela_image).enhance(scale)
    
    return ela_image


def get_plot(path):
    orig = cv2.imread(path)
    orig = cv2.cvtColor(orig, cv2.COLOR_BGR2RGB) / 255.0
    init_val = 100
    columns = 3
    rows = 3

    fig=plt.figure(figsize=(15, 10))
    for i in range(1, columns*rows +1):
        quality=init_val - (i-1) * 3
        img = compute_ela_cv(path=path, quality=quality)
        if i == 1:
            img = orig.copy()
        ax = fig.add_subplot(rows, columns, i) 
        ax.title.set_text(f'q: {quality}')
        plt.imshow(img)
    return plt
        
@app.route('/segmentation')
def segmentation():
    print("calling")
    return render_template('preview.html')

    
if __name__ =='__main__':
	app.run()
