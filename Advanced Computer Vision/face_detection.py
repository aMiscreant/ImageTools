import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

# Ensure the output directory exists
output_dir = 'output_advanced_cv'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function for object detection using Haar cascades
def detect_objects(image, cascade_path='haarcascade_frontalface_default.xml'):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier(cv2.data.haarcascades + cascade_path)
    objects = cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in objects:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return image

# Load the image
image_path = 'your_image.jpg'  # Replace with your image path
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError(f"Image not found at path: {image_path}")

# Apply object detection
detected_image = detect_objects(image.copy())
detected_image_path = os.path.join(output_dir, 'detected_image.jpg')
cv2.imwrite(detected_image_path, detected_image)

plt.imshow(cv2.cvtColor(detected_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Object Detection')
plt.show()

print(f'Object detected image created and saved as "{detected_image_path}".')
