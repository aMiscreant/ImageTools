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

# Alternative function to apply oil painting effect
def apply_oil_painting(image, kernel_size=7):
    blurred = cv2.medianBlur(image, kernel_size)
    return blurred

# Apply oil painting effect
oil_painted_image = apply_oil_painting(image)
oil_painted_image_path = 'oil_painted_image.jpg'
cv2.imwrite(oil_painted_image_path, oil_painted_image)

plt.imshow(cv2.cvtColor(oil_painted_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Oil Painted Image')
plt.show()

print(f'Oil painted image created and saved as "{oil_painted_image_path}".')
