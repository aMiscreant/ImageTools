import cv2
import numpy as np
import os
import random
import matplotlib.pyplot as plt

# Load the image
image_path = 'your_image.jpg'  # Replace with your image path
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError(f"Image not found at path: {image_path}")

# Ensure the output directory exists and delete it if it does
output_dir = 'output_frames'
if os.path.exists(output_dir):
    os.makedirs(output_dir, exist_ok=True)

# Function for random rotation
def random_rotation(image, angle_range=(-30, 30)):
    angle = random.uniform(*angle_range)
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h), borderMode=cv2.BORDER_REFLECT)
    return rotated_image

# Apply random rotation
rotated_image = random_rotation(image)
rotated_image_path = 'rotated_image_aug.jpg'
cv2.imwrite(rotated_image_path, rotated_image)

plt.imshow(cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Randomly Rotated Image')
plt.show()

print(f'Randomly rotated image created and saved as "{rotated_image_path}".')
