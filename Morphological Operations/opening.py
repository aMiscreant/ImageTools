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

# Function to apply opening (erosion followed by dilation)
def apply_opening(image, kernel_size=(5, 5)):
    kernel = np.ones(kernel_size, np.uint8)
    opened_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    return opened_image

# Apply opening to the image
opened_image = apply_opening(image)
opened_image_path = 'opened_image.jpg'
cv2.imwrite(opened_image_path, opened_image)

plt.imshow(opened_image, cmap='gray')
plt.axis('off')
plt.title('Opened Image')
plt.show()

print(f'Opened image created and saved as "{opened_image_path}".')
