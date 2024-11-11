import cv2
import numpy as np
import os
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

# Function to flip the image
def flip_image(image, flip_code):
    flipped_image = cv2.flip(image, flip_code)
    return flipped_image

# Apply flipping to the image
flipped_image = flip_image(image, 1)  # 1 for horizontal, 0 for vertical, -1 for both
flipped_image_path = 'flipped_image.jpg'
cv2.imwrite(flipped_image_path, flipped_image)

plt.imshow(cv2.cvtColor(flipped_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Flipped Image (Horizontal)')
plt.show()

print(f'Flipped image created and saved as "{flipped_image_path}".')
