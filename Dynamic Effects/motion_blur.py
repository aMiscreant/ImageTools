import cv2
import imageio
import numpy as np
import os
import matplotlib.pyplot as plt

# Ensure the output directory exists
output_dir = 'output_dynamic_effects'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


# Function to create motion blur effect
def create_motion_blur(image, kernel_size=15):
    kernel = np.zeros((kernel_size, kernel_size))
    kernel[int((kernel_size - 1) / 2), :] = np.ones(kernel_size)
    kernel /= kernel_size
    motion_blur_image = cv2.filter2D(image, -1, kernel)
    return motion_blur_image

# Load the image
image_path = 'your_image.jpg'  # Replace with your image path
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError(f"Image not found at path: {image_path}")

# Apply motion blur effect
motion_blur_image = create_motion_blur(image)
motion_blur_image_path = os.path.join(output_dir, 'motion_blur_image.jpg')
cv2.imwrite(motion_blur_image_path, motion_blur_image)

plt.imshow(cv2.cvtColor(motion_blur_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Motion Blur Effect')
plt.show()

print(f'Motion blur image created and saved as "{motion_blur_image_path}".')
