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

# Function to swap color channels (e.g., RGB to BGR)
def swap_channels(image, order=(2, 1, 0)):
    swapped_image = image[:, :, order]
    return swapped_image

# Apply channel swapping
swapped_image = swap_channels(image, order=(2, 1, 0))  # Swap RGB to BGR
swapped_image_path = 'swapped_image.jpg'
cv2.imwrite(swapped_image_path, swapped_image)

plt.imshow(cv2.cvtColor(swapped_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Channel Swapped Image')
plt.show()

print(f'Channel swapped image created and saved as "{swapped_image_path}".')
