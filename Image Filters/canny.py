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

# Function to apply Canny edge detection
def apply_canny_edge_detection(image, threshold1=100, threshold2=200):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray_image, threshold1, threshold2)
    edges_colored = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)  # Convert to 3 channels for consistency
    return edges_colored

# Apply Canny edge detection
canny_image = apply_canny_edge_detection(image)

# Save and display the Canny edge detection image
canny_image_path = 'canny_image.jpg'
cv2.imwrite(canny_image_path, canny_image)

plt.imshow(cv2.cvtColor(canny_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Canny Edge Detection')
plt.show()

print(f'Canny edge detection image created and saved as "{canny_image_path}".')
