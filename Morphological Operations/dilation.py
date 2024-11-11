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

# Function to apply dilation
def apply_dilation(image, kernel_size=(5, 5), iterations=1):
    kernel = np.ones(kernel_size, np.uint8)
    dilated_image = cv2.dilate(image, kernel, iterations=iterations)
    return dilated_image

# Apply dilation to the image
dilated_image = apply_dilation(image)
dilated_image_path = 'dilated_image.jpg'
cv2.imwrite(dilated_image_path, dilated_image)

plt.imshow(dilated_image, cmap='gray')
plt.axis('off')
plt.title('Dilated Image')
plt.show()

print(f'Dilated image created and saved as "{dilated_image_path}".')

