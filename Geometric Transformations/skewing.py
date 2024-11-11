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

# Function to apply skew/perspective transformation
def skew_image(image):
    (h, w) = image.shape[:2]
    src_points = np.float32([[0, 0], [w - 1, 0], [0, h - 1], [w - 1, h - 1]])
    dst_points = np.float32([[0, 0], [w - 1, 0], [int(0.33 * w), h - 1], [int(0.66 * w), h - 1]])
    perspective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)
    skewed_image = cv2.warpPerspective(image, perspective_matrix, (w, h))
    return skewed_image

# Apply skew/perspective transformation to the image
skewed_image = skew_image(image)
skewed_image_path = 'skewed_image.jpg'
cv2.imwrite(skewed_image_path, skewed_image)

plt.imshow(cv2.cvtColor(skewed_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Skewed Image')
plt.show()

print(f'Skewed image created and saved as "{skewed_image_path}".')
