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


# Function to apply sharpening using kernels
def apply_sharpening(image):
    kernel = np.array([[-1, -1, -1],
                       [-1,  9, -1],
                       [-1, -1, -1]])
    sharpened_image = cv2.filter2D(image, -1, kernel)
    return sharpened_image

# Apply sharpening
sharpened_image = apply_sharpening(image)
sharpened_image_path = 'sharpened_image.jpg'
cv2.imwrite(sharpened_image_path, sharpened_image)

plt.imshow(cv2.cvtColor(sharpened_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Sharpened Image')
plt.show()

print(f'Sharpened image created and saved as "{sharpened_image_path}".')
