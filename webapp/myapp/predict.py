import tensorflow as tf
import numpy as np
import cv2


model = tf.keras.models.load_model("../models/braintumorclassidication.h5")
classNames = ['Glioma', 'Meningioma', 'Pituitary', 'no_tumor']

def load_image(path):
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def predict(image):
    image = np.asarray(image)
    image = cv2.resize(image, (224, 224))
    image = image / 255.0  
    pred = model.predict(image)
    predicted_class = classNames[np.argmax(pred)]
    return predicted_class



