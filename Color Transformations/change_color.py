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

# Function to change specific color tones
def change_color_tone(image, lower_bound, upper_bound, new_color):
    mask = cv2.inRange(image, lower_bound, upper_bound)
    result = image.copy()
    result[mask > 0] = new_color
    return result

# Apply color tone change
lower_bound = np.array([0, 0, 100])  # Adjust as needed (e.g., a shade of red)
upper_bound = np.array([50, 50, 255])  # Adjust as needed
new_color = [0, 255, 0]  # Change to green
toned_image = change_color_tone(image, lower_bound, upper_bound, new_color)
toned_image_path = 'toned_image.jpg'
cv2.imwrite(toned_image_path, toned_image)

plt.imshow(cv2.cvtColor(toned_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Color Tone Changed Image')
plt.show()

print(f'Color tone changed image created and saved as "{toned_image_path}".')
