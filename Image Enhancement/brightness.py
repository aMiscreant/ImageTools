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

# Function to adjust brightness and contrast
def adjust_brightness_contrast(image, brightness=0, contrast=1.0):
    adjusted_image = cv2.convertScaleAbs(image, alpha=contrast, beta=brightness)
    return adjusted_image

# Apply brightness and contrast adjustment
brightness = 50  # Increase brightness
contrast = 1.2   # Increase contrast
adjusted_image = adjust_brightness_contrast(image, brightness, contrast)
adjusted_image_path = 'adjusted_image.jpg'
cv2.imwrite(adjusted_image_path, adjusted_image)

plt.imshow(cv2.cvtColor(adjusted_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Brightness and Contrast Adjusted Image')
plt.show()

print(f'Brightness and contrast adjusted image created and saved as "{adjusted_image_path}".')

