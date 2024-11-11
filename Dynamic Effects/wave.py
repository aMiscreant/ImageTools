import cv2
import imageio
import numpy as np
import os
import matplotlib.pyplot as plt

# Ensure the output directory exists
output_dir = 'output_dynamic_effects'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to create wave distortion effect
def create_wave_effect(image, amplitude=5, frequency=20):
    h, w = image.shape[:2]
    wave_image = np.zeros_like(image)
    for y in range(h):
        offset_x = int(amplitude * np.sin(2 * np.pi * y / frequency))
        wave_image[y] = np.roll(image[y], offset_x)
    return wave_image

# Load the image
image_path = 'your_image.jpg'  # Replace with your image path
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError(f"Image not found at path: {image_path}")

# Apply wave effect
wave_image = create_wave_effect(image)
wave_image_path = os.path.join(output_dir, 'wave_effect_image.jpg')
cv2.imwrite(wave_image_path, wave_image)

plt.imshow(cv2.cvtColor(wave_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Wave Effect')
plt.show()

print(f'Wave effect image created and saved as "{wave_image_path}".')
