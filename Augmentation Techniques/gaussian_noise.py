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

# Function for adding Gaussian noise
def add_gaussian_noise(image, mean=0, stddev=25):
    gaussian_noise = np.random.normal(mean, stddev, image.shape).astype(np.uint8)
    noisy_image = cv2.add(image, gaussian_noise)
    return noisy_image

# Apply Gaussian noise
gaussian_noise_image = add_gaussian_noise(image)
gaussian_noise_image_path = 'gaussian_noise_image_aug.jpg'
cv2.imwrite(gaussian_noise_image_path, gaussian_noise_image)

plt.imshow(cv2.cvtColor(gaussian_noise_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Gaussian Noisy Image')
plt.show()

print(f'Gaussian noisy image created and saved as "{gaussian_noise_image_path}".')
