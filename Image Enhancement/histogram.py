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

# Function to apply histogram equalization
def apply_histogram_equalization(image):
    img_yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])
    equalized_image = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
    return equalized_image


# Apply histogram equalization
equalized_image = apply_histogram_equalization(image)
equalized_image_path = 'equalized_image.jpg'
cv2.imwrite(equalized_image_path, equalized_image)

plt.imshow(cv2.cvtColor(equalized_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Histogram Equalized Image')
plt.show()

print(f'Histogram equalized image created and saved as "{equalized_image_path}".')

