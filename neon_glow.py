import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

# Ensure the output directory exists
output_dir = 'output_neon_glow_effects'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to create neon glow effect
def create_neon_glow_effect(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    edges_colored = cv2.applyColorMap(edges, cv2.COLORMAP_JET)
    glow_image = cv2.addWeighted(image, 0.6, edges_colored, 0.4, 0)
    return glow_image

# Load the image
image_path = 'your_image.jpg'  # Replace with your image path
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError(f"Image not found at path: {image_path}")

# Apply neon glow effect
neon_glow_image = create_neon_glow_effect(image)
neon_glow_image_path = os.path.join(output_dir, 'neon_glow_image.jpg')
cv2.imwrite(neon_glow_image_path, neon_glow_image)

plt.imshow(cv2.cvtColor(neon_glow_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Neon Glow Effect')
plt.show()

print(f'Neon glow effect image created and saved as "{neon_glow_image_path}".')
