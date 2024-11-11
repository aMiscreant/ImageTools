import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.ndimage import map_coordinates, gaussian_filter

# Load the image
image_path = 'your_image.jpg'  # Replace with your image path
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError(f"Image not found at path: {image_path}")

# Ensure the output directory exists and delete it if it does
output_dir = 'output_frames'
if os.path.exists(output_dir):
    os.makedirs(output_dir, exist_ok=True)

# Function to apply pixelation effect
def apply_pixelation(image, pixel_size=10):
    h, w = image.shape[:2]
    small_image = cv2.resize(image, (w // pixel_size, h // pixel_size), interpolation=cv2.INTER_LINEAR)
    pixelated_image = cv2.resize(small_image, (w, h), interpolation=cv2.INTER_NEAREST)
    return pixelated_image

# Apply pixelation effect
pixelated_image = apply_pixelation(image)
pixelated_image_path = 'pixelated_image.jpg'
cv2.imwrite(pixelated_image_path, pixelated_image)

plt.imshow(cv2.cvtColor(pixelated_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Pixelated Image')
plt.show()

print(f'Pixelated image created and saved as "{pixelated_image_path}".')
