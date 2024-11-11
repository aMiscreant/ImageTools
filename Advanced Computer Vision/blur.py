import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

# Ensure the output directory exists
output_dir = 'output_advanced_cv'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to apply face blurring
def blur_faces(image, cascade_path='haarcascade_frontalface_default.xml'):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier(cv2.data.haarcascades + cascade_path)
    faces = cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in faces:
        face_region = image[y:y + h, x:x + w]
        blurred_face = cv2.GaussianBlur(face_region, (99, 99), 30)
        image[y:y + h, x:x + w] = blurred_face
    return image

# Load the image
image_path = 'your_image.jpg'  # Replace with your image path
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError(f"Image not found at path: {image_path}")

# Apply face blurring
blurred_image = blur_faces(image.copy())
blurred_image_path = os.path.join(output_dir, 'blurred_image.jpg')
cv2.imwrite(blurred_image_path, blurred_image)

plt.imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Face Blurred Image')
plt.show()

print(f'Face blurred image created and saved as "{blurred_image_path}".')
