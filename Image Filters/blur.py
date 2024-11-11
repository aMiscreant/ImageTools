import cv2
import numpy as np
import os
import shutil
import imageio
import matplotlib.pyplot as plt
import threading

# Load the image
image_path = 'your_image.jpg'  # Replace with your image path
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError(f"Image not found at path: {image_path}")

# Ensure the output directory exists and delete it if it does
output_dir = 'output_frames'
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir, exist_ok=True)

# Function to apply a blur effect
def apply_blur(image, kernel_size=(15, 15)):
    blurred_image = cv2.GaussianBlur(image, kernel_size, 0)
    return blurred_image

# Apply blur filter
blurred_image = apply_blur(image)

# Save and display the blurred image
blurred_image_path = 'blurred_image.jpg'
cv2.imwrite(blurred_image_path, blurred_image)

plt.imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Blurred Image')
plt.show()

print(f'Blurred image created and saved as "{blurred_image_path}".')

# Function to apply a custom blur effect
def apply_custom_blur(image, kernel_size=(25, 25)):
    custom_blurred_image = cv2.blur(image, kernel_size)
    return custom_blurred_image

# Apply custom blur filter
custom_blurred_image = apply_custom_blur(image)

# Save and display the custom blurred image
custom_blurred_image_path = 'custom_blurred_image.jpg'
cv2.imwrite(custom_blurred_image_path, custom_blurred_image)

plt.imshow(cv2.cvtColor(custom_blurred_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Custom Blurred Image')
plt.show()

print(f'Custom blurred image created and saved as \"{custom_blurred_image_path}\".')
