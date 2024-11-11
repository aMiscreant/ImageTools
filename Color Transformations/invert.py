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

# Function to invert colors
def invert_colors(image):
    inverted_image = cv2.bitwise_not(image)
    return inverted_image

# Apply color inversion
inverted_image = invert_colors(image)
inverted_image_path = 'inverted_image.jpg'
cv2.imwrite(inverted_image_path, inverted_image)

plt.imshow(cv2.cvtColor(inverted_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Inverted Image')
plt.show()

print(f'Inverted image created and saved as "{inverted_image_path}".')

