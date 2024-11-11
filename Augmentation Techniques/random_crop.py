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

# Function for random crop
def random_crop(image, crop_size=(200, 200)):
    h, w = image.shape[:2]
    crop_h, crop_w = crop_size
    if h < crop_h or w < crop_w:
        raise ValueError("Crop size should be smaller than the image dimensions")
    x = random.randint(0, w - crop_w)
    y = random.randint(0, h - crop_h)
    cropped_image = image[y:y+crop_h, x:x+crop_w]
    return cropped_image

# Apply random crop
cropped_image = random_crop(image)
cropped_image_path = 'cropped_image_aug.jpg'
cv2.imwrite(cropped_image_path, cropped_image)

plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Randomly Cropped Image')
plt.show()

print(f'Randomly cropped image created and saved as "{cropped_image_path}".')
