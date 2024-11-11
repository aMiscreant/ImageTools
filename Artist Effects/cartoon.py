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

# Function to apply cartoon effect
def apply_cartoon_effect(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.medianBlur(gray, 7)
    edges = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 10)
    color = cv2.bilateralFilter(image, 9, 300, 300)
    cartoon_image = cv2.bitwise_and(color, color, mask=edges)
    return cartoon_image

# Apply cartoon effect
cartoon_image = apply_cartoon_effect(image)
cartoon_image_path = 'cartoon_image.jpg'
cv2.imwrite(cartoon_image_path, cartoon_image)

plt.imshow(cv2.cvtColor(cartoon_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Cartoon Image')
plt.show()

print(f'Cartoon image created and saved as "{cartoon_image_path}".')
