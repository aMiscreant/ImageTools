import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

# Ensure the output directory exists
output_dir = 'output_3d_transformations'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to create a simple depth mapping effect with parallax
def create_depth_map(image, depth_shift=20):
    h, w, _ = image.shape
    depth_map = np.zeros_like(image)
    for i in range(1, depth_shift):
        shifted_image = np.roll(image, shift=i, axis=1)  # Create parallax effect by shifting
        alpha = 1.0 - (i / depth_shift)
        depth_map = cv2.addWeighted(depth_map, 1.0, shifted_image, alpha, 0)
    return depth_map

# Load the image
image_path = 'your_image.jpg'  # Replace with your image path
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError(f"Image not found at path: {image_path}")

# Apply depth mapping effect
depth_map_image = create_depth_map(image)
depth_map_image_path = os.path.join(output_dir, 'depth_map_image.jpg')
cv2.imwrite(depth_map_image_path, depth_map_image)

plt.imshow(cv2.cvtColor(depth_map_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Depth Mapping Effect')
plt.show()

print(f'Depth map image created and saved as "{depth_map_image_path}".')
