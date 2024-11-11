import cv2
import imageio
import numpy as np
import os
import matplotlib.pyplot as plt

# Ensure the output directory exists
output_dir = 'output_dynamic_effects'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to create animated noise effect
def create_animated_noise(image, noise_frames=30):
    height, width, _ = image.shape
    frames = []
    for i in range(noise_frames):
        noise = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
        noisy_frame = cv2.addWeighted(image, 0.5, noise, 0.5, 0)
        frames.append(noisy_frame)
    return frames

# Load the image
image_path = 'your_image.jpg'  # Replace with your image path
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError(f"Image not found at path: {image_path}")

# Apply animated noise effect
noise_frames = create_animated_noise(image)
noise_gif_path = os.path.join(output_dir, 'animated_noise.gif')
imageio.mimsave(noise_gif_path, [cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) for frame in noise_frames], duration=0.1)

print(f'Animated noise GIF created and saved as "{noise_gif_path}".')
