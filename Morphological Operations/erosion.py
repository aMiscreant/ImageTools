import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

# Load the image
image_path = 'your_image.jpg'  # Replace with your image path
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Use grayscale for morphological operations

if image is None:
    raise FileNotFoundError(f"Image not found at path: {image_path}")

# Ensure the output directory exists and delete it if it does
output_dir = 'output_frames'
if os.path.exists(output_dir):
    os.makedirs(output_dir, exist_ok=True)

# Function to apply erosion
def apply_erosion(image, kernel_size=(5, 5), iterations=1):
    kernel = np.ones(kernel_size, np.uint8)
    eroded_image = cv2.erode(image, kernel, iterations=iterations)
    return eroded_image

# Apply erosion to the image
eroded_image = apply_erosion(image)
eroded_image_path = 'eroded_image.jpg'
cv2.imwrite(eroded_image_path, eroded_image)

plt.imshow(eroded_image, cmap='gray')
plt.axis('off')
plt.title('Eroded Image')
plt.show()

print(f'Eroded image created and saved as "{eroded_image_path}".')

