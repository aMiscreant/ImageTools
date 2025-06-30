# ========================================== #
#    Made by aMiscreant for Miscreants       #
# ========================================== #
# sepia.py
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

# Apply sepia filter
sepia_image = apply_sepia(image)

# Save and display the sepia image
sepia_image_path = 'sepia_image.jpg'
cv2.imwrite(sepia_image_path, sepia_image)

plt.imshow(cv2.cvtColor(sepia_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Sepia Image')
# plt.title('') # Blank title
plt.show()

print(f'Sepia image created and saved as "{sepia_image_path}".')
