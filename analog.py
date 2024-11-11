import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

# Ensure the output directory exists
output_dir = 'output_analog_effect'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to apply an analog noise effect
def create_analog_effect(image, grain_intensity=0.05, color_shift=15):
    height, width, _ = image.shape

    # Add grain noise
    noise = np.random.normal(0, grain_intensity * 255, image.shape).astype(np.uint8)
    analog_image = cv2.add(image, noise)

    # Add subtle color shift to create an analog look
    b, g, r = cv2.split(analog_image)
    b = cv2.add(b, np.random.randint(-color_shift, color_shift, (height, width), dtype=np.int16).astype(np.uint8))
    g = cv2.add(g, np.random.randint(-color_shift, color_shift, (height, width), dtype=np.int16).astype(np.uint8))
    r = cv2.add(r, np.random.randint(-color_shift, color_shift, (height, width), dtype=np.int16).astype(np.uint8))

    analog_image = cv2.merge((b, g, r))

    # Apply slight blur to soften the grain
    analog_image = cv2.GaussianBlur(analog_image, (3, 3), 0)

    return analog_image

# Load the image
image_path = 'your_image.jpg'  # Replace with your image path
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError(f"Image not found at path: {image_path}")

# Apply the analog effect
analog_image = create_analog_effect(image)
analog_image_path = os.path.join(output_dir, 'analog_effect_image.jpg')
cv2.imwrite(analog_image_path, analog_image)

plt.imshow(cv2.cvtColor(analog_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Analog Effect')
plt.show()

print(f'Analog effect image created and saved as "{analog_image_path}".')
