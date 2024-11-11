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

# Function to apply Sobel edge detection
def apply_sobel_edge_detection(image, ksize=3):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=ksize)
    sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=ksize)
    sobel_combined = cv2.magnitude(sobelx, sobely)
    sobel_combined = np.uint8(np.clip(sobel_combined, 0, 255))  # Ensure pixel values are valid
    sobel_colored = cv2.cvtColor(sobel_combined, cv2.COLOR_GRAY2BGR)  # Convert to 3 channels for consistency
    return sobel_colored

# Apply Sobel edge detection
sobel_image = apply_sobel_edge_detection(image)

# Save and display the Sobel edge detection image
sobel_image_path = 'sobel_image.jpg'
cv2.imwrite(sobel_image_path, sobel_image)

plt.imshow(cv2.cvtColor(sobel_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Sobel Edge Detection')
plt.show()

print(f'Sobel edge detection image created and saved as "{sobel_image_path}".')
