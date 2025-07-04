# Insert script for image filters here
# Example: Applying a grayscale.py filter using OpenCV
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

# Function to apply a sepia filter
def apply_sepia(image):
    sepia_filter = np.array([[0.272, 0.534, 0.131],
                             [0.349, 0.686, 0.168],
                             [0.393, 0.769, 0.189]])
    sepia_image = cv2.transform(image, sepia_filter)
    sepia_image = np.clip(sepia_image, 0, 255)  # Ensure pixel values are valid
    return sepia_image

# Function to apply a grayscale filter
def apply_grayscale(image):
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.cvtColor(grayscale_image, cv2.COLOR_GRAY2BGR)  # Convert to 3 channels for consistency

# Apply sepia filter
sepia_image = apply_sepia(image)

# Save and display the sepia image
sepia_image_path = 'sepia_image.jpg'
cv2.imwrite(sepia_image_path, sepia_image)

plt.imshow(cv2.cvtColor(sepia_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Sepia Image')
plt.show()

print(f'Sepia image created and saved as "{sepia_image_path}".')

# Apply grayscale filter
grayscale_image = apply_grayscale(image)

# Save and display the grayscale image
grayscale_image_path = 'grayscale_image.jpg'
cv2.imwrite(grayscale_image_path, grayscale_image)

plt.imshow(cv2.cvtColor(grayscale_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Grayscale Image')
plt.show()

print(f'Grayscale image created and saved as "{grayscale_image_path}".')
