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

# Function to apply glitch effect by manipulating pixel data
def apply_glitch_effect(image, severity=5):
    glitch_image = image.copy()
    rows, cols, _ = glitch_image.shape
    for i in range(0, rows, severity):
        shift = np.random.randint(-severity, severity)
        glitch_image[i] = np.roll(glitch_image[i], shift, axis=0)
    return glitch_image

# Apply glitch effect
glitch_image = apply_glitch_effect(image)
glitch_image_path = 'glitch_image.jpg'
cv2.imwrite(glitch_image_path, glitch_image)

plt.imshow(cv2.cvtColor(glitch_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Glitch Image')
plt.show()

print(f'Glitch image created and saved as "{glitch_image_path}".')
