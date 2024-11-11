import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

# Ensure the output directory exists
output_dir = 'output_composition'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to add a watermark to an image
def add_watermark(image, text='Watermark', position=(30, 30), font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=1, color=(255, 255, 255), thickness=2):
    watermarked_image = image.copy()
    cv2.putText(watermarked_image, text, position, font, font_scale, color, thickness, cv2.LINE_AA)
    return watermarked_image

# Load the image to apply the watermark
image_path = 'your_image.jpg'  # Replace with your image path
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError(f"Image not found at path: {image_path}")

# Apply watermark to the image
watermarked_image = add_watermark(image, text='My Watermark', position=(50, 50))
watermarked_image_path = os.path.join(output_dir, 'watermarked_image.jpg')
cv2.imwrite(watermarked_image_path, watermarked_image)

plt.imshow(cv2.cvtColor(watermarked_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Watermarked Image')
plt.show()

print(f'Watermarked image created and saved as "{watermarked_image_path}".')
