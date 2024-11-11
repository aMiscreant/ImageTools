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

# Function to scale the image
def scale_image(image, scale_factor):
    (h, w) = image.shape[:2]
    scaled_image = cv2.resize(image, (int(w * scale_factor), int(h * scale_factor)))
    return scaled_image

# Apply scaling to the image
scale_factor = 1.5  # You can change this value for different scaling effects
scaled_image = scale_image(image, scale_factor)
scaled_image_path = 'scaled_image.jpg'
cv2.imwrite(scaled_image_path, scaled_image)

plt.imshow(cv2.cvtColor(scaled_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Scaled Image (1.5x)')
plt.show()

print(f'Scaled image created and saved as "{scaled_image_path}".')
