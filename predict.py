import argparse
import tensorflow as tf
import numpy as np
import cv2

# Load the model
model = tf.keras.models.load_model("./models/braintumorclassidication.h5")
classNames = ['Glioma', 'Meningioma', 'Pituitary', 'no_tumor']

def load_image(path):
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def predict(image):
    image = image / 255.0  # Normalize pixel values
    pred = model.predict(image)
    predicted_class = classNames[np.argmax(pred)]
    return predicted_class

# Create an argument parser
parser = argparse.ArgumentParser(description="Brain Tumor Classification")
parser.add_argument("--image_path", required=True, help="Path to the image file")

# Parse the arguments
args = parser.parse_args()

# Load the image
image = load_image(args.image_path)

# Make prediction
predicted_class = predict(image)

# Print the prediction
print("Predicted class:", predicted_class)
