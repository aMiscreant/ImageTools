import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

# Ensure the output directory exists
output_dir = 'output_3d_transformations'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


# Function to create a basic stereoscopic effect
def create_stereoscopic_effect(image, shift=10):
    height, width, _ = image.shape
    left_image = image[:, :-shift]  # Shift left image to create parallax
    right_image = image[:, shift:]  # Shift right image
    stereoscopic_image = np.zeros((height, width, 3), dtype=np.uint8)
    stereoscopic_image[:, :width//2] = left_image[:, :width//2]  # Left half from left image
    stereoscopic_image[:, width//2:] = right_image[:, width//2-shift:]  # Right half from right image
    return stereoscopic_image

# Load the image
image_path = 'your_image.jpg'  # Replace with your image path
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError(f"Image not found at path: {image_path}")

# Apply stereoscopic effect
stereoscopic_image = create_stereoscopic_effect(image)
stereoscopic_image_path = os.path.join(output_dir, 'stereoscopic_image.jpg')
cv2.imwrite(stereoscopic_image_path, stereoscopic_image)

plt.imshow(cv2.cvtColor(stereoscopic_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Stereoscopic Effect')
plt.show()

print(f'Stereoscopic image created and saved as "{stereoscopic_image_path}".')
