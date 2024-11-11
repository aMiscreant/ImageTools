import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

# Ensure the output directory exists
output_dir = 'output_advanced_cv'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function for image segmentation (simple background subtraction)
def segment_image(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)
    segmented_image = cv2.bitwise_and(image, image, mask=thresh)
    return segmented_image

# Load the image
image_path = 'your_image.jpg'  # Replace with your image path
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError(f"Image not found at path: {image_path}")

# Apply image segmentation
segmented_image = segment_image(image.copy())
segmented_image_path = os.path.join(output_dir, 'segmented_image.jpg')
cv2.imwrite(segmented_image_path, segmented_image)

plt.imshow(cv2.cvtColor(segmented_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Segmented Image')
plt.show()

print(f'Segmented image created and saved as "{segmented_image_path}".')
