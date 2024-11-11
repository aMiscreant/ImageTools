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

# Function to apply closing (dilation followed by erosion)
def apply_closing(image, kernel_size=(5, 5)):
    kernel = np.ones(kernel_size, np.uint8)
    closed_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    return closed_image

# Apply closing to the image
closed_image = apply_closing(image)
closed_image_path = 'closed_image.jpg'
cv2.imwrite(closed_image_path, closed_image)

plt.imshow(closed_image, cmap='gray')
plt.axis('off')
plt.title('Closed Image')
plt.show()

print(f'Closed image created and saved as "{closed_image_path}".')
