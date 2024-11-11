import cv2
import numpy as np
import os
import shutil
import imageio
import matplotlib.pyplot as plt
import threading

# Load the image
image_path = 'your_image.jpg'  # Replace with your image path
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError(f"Image not found at path: {image_path}")

# Ensure the output directory exists and delete it if it does
output_dir = 'output_frames'
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir, exist_ok=True)

# Function to apply a Gaussian effect
def apply_gaussian_effect(image, kernel_size=(25, 25)):
    gaussian_image = cv2.GaussianBlur(image, kernel_size, 0)
    return gaussian_image

# Apply Gaussian effect
gaussian_image = apply_gaussian_effect(image)

# Save and display the Gaussian image
gaussian_image_path = 'gaussian_image.jpg'
cv2.imwrite(gaussian_image_path, gaussian_image)

plt.imshow(cv2.cvtColor(gaussian_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Gaussian Image')
plt.show()

print(f'Gaussian image created and saved as "{gaussian_image_path}".')
