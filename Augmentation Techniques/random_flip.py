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

# Function for random flip
def random_flip(image):
    flip_code = random.choice([-1, 0, 1])  # -1: both axes, 0: vertical, 1: horizontal
    flipped_image = cv2.flip(image, flip_code)
    return flipped_image

# Apply random flip
flipped_image = random_flip(image)
flipped_image_path = 'flipped_image_aug.jpg'
cv2.imwrite(flipped_image_path, flipped_image)

plt.imshow(cv2.cvtColor(flipped_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Randomly Flipped Image')
plt.show()

print(f'Randomly flipped image created and saved as "{flipped_image_path}".')
