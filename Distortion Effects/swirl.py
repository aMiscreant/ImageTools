from typing import Any

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


# Function to apply swirl distortion
def apply_swirl(image, strength=1, radius=100):
    h, w = image.shape[:2]
    center = (w // 2, h // 2)
    Y, X = np.meshgrid(np.arange(h), np.arange(w), indexing='ij')
    offset_x = X - center[0]
    offset_y = Y - center[1]
    r = np.sqrt(offset_x ** 2 + offset_y ** 2)
    theta = np.arctan2(offset_y, offset_x) + strength * np.exp(-r / radius)
    X_new = center[0] + r * np.cos(theta)
    Y_new = center[1] + r * np.sin(theta)

    # Clip the coordinates to be within image bounds
    X_new = np.clip(X_new, 0, w - 1).astype(np.float32)
    Y_new = np.clip(Y_new, 0, h - 1).astype(np.float32)

    # Map coordinates using correct interpolation method
    warped_image = cv2.remap(image, X_new, Y_new, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    return warped_image


# Apply swirl distortion
swirled_image = apply_swirl(image)
swirled_image_path = 'swirled_image.jpg'
cv2.imwrite(swirled_image_path, swirled_image)

plt.imshow(cv2.cvtColor(swirled_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Swirled Image')
plt.show()

print(f'Swirled image created and saved as "{swirled_image_path}".')
