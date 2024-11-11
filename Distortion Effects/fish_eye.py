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

# Function to apply fish-eye lens effect
def apply_fisheye(image):
    h, w = image.shape[:2]
    K = np.array([[w, 0, w//2], [0, h, h//2], [0, 0, 1]])
    D = np.array([0.2, 0.2, 0, 0])
    map1, map2 = cv2.initUndistortRectifyMap(K, D, None, K, (w, h), 5)
    fisheye_image = cv2.remap(image, map1, map2, interpolation=cv2.INTER_LINEAR)
    return fisheye_image

# Apply fish-eye lens effect
fisheye_image = apply_fisheye(image)
fisheye_image_path = 'fisheye_image.jpg'
cv2.imwrite(fisheye_image_path, fisheye_image)

plt.imshow(cv2.cvtColor(fisheye_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Fish-eye Image')
plt.show()

print(f'Fish-eye image created and saved as "{fisheye_image_path}".')

