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

# Function to apply a median effect
def apply_median_effect(image, kernel_size=15):
    median_image = cv2.medianBlur(image, kernel_size)
    return median_image

# Apply Median effect
median_image = apply_median_effect(image)

# Save and display the Median image
median_image_path = 'median_image.jpg'
cv2.imwrite(median_image_path, median_image)

plt.imshow(cv2.cvtColor(median_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Median Image')
plt.show()

print(f'Median image created and saved as "{median_image_path}".')
