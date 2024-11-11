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

# Function for adding salt-and-pepper noise
def add_salt_and_pepper_noise(image, salt_prob=0.01, pepper_prob=0.01):
    noisy_image = image.copy()
    num_salt = int(salt_prob * image.size)
    num_pepper = int(pepper_prob * image.size)

    # Add salt
    coords = [np.random.randint(0, i - 1, num_salt) for i in image.shape]
    noisy_image[coords[0], coords[1], :] = 255

    # Add pepper
    coords = [np.random.randint(0, i - 1, num_pepper) for i in image.shape]
    noisy_image[coords[0], coords[1], :] = 0

    return noisy_image

# Apply salt-and-pepper noise
salt_pepper_image = add_salt_and_pepper_noise(image)
salt_pepper_image_path = 'salt_pepper_image_aug.jpg'
cv2.imwrite(salt_pepper_image_path, salt_pepper_image)

plt.imshow(cv2.cvtColor(salt_pepper_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Salt-and-Pepper Noisy Image')
plt.show()

print(f'Salt-and-pepper noisy image created and saved as "{salt_pepper_image_path}".')
