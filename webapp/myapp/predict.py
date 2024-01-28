import tensorflow as tf
import numpy as np
import cv2




def load_image(path):
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def predict(image):
    model = tf.keras.models.load_model("../models/braintumorclassidication.h5")
    classNames = ['Glioma', 'Meningioma', 'Pituitary', 'no_tumor']
    image = np.asarray(image)
    image = cv2.resize(image, (224, 224))
    image = image / 255.0  
    image = np.expand_dims(image, axis=0)  
    pred = model.predict(image)
    i = np.argmax(pred)
    predicted_class = classNames[i]
    return (predicted_class, pred[i])



