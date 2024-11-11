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

# Function to apply image rotation
def rotate_image(image, angle, scale=1.0):
    (h, w) = image.shape[:2]  # Get the image dimensions
    center = (w // 2, h // 2)  # Determine the center of the image

    # Compute the rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)

    # Perform the rotation
    rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))
    return rotated_image

# Apply rotation to the image
rotation_angle = 45  # You can change this value to rotate the image at different angles
rotated_image = rotate_image(image, rotation_angle)

# Save and display the rotated image
rotated_image_path = 'rotated_image.jpg'
cv2.imwrite(rotated_image_path, rotated_image)

plt.imshow(cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title(f'Rotated Image ({rotation_angle} degrees)')
plt.show()

print(f'Rotated image created and saved as "{rotated_image_path}".')
