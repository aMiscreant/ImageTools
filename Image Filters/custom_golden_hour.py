import cv2
import numpy as np
import os
import shutil
import imageio
import matplotlib.pyplot as plt
import threading

# Load the image
image_path = 'your_image.jpg'  # Replace with your image path
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError(f"Image not found at path: {image_path}")

# Ensure the output directory exists and delete it if it does
output_dir = 'output_frames'
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir, exist_ok=True)

# Function to apply a sepia filter
def apply_sepia(image):
    sepia_filter = np.array([[0.272, 0.534, 0.131],
                             [0.349, 0.686, 0.168],
                             [0.393, 0.769, 0.189]])
    sepia_image = cv2.transform(image, sepia_filter)
    sepia_image = np.clip(sepia_image, 0, 255)  # Ensure pixel values are valid
    return sepia_image

# Function to apply a grayscale filter
def apply_grayscale(image):
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.cvtColor(grayscale_image, cv2.COLOR_GRAY2BGR)  # Convert to 3 channels for consistency

# Function to apply a pink-tinted filter to a grayscale image
def apply_pink_tint(grayscale_image):
    # Create a pink tint by adding a pinkish hue to the grayscale image
    pink_tinted_image = grayscale_image.copy()
    pink_tinted_image[:, :, 0] = pink_tinted_image[:, :, 0] * 0.8  # Reduce blue channel
    pink_tinted_image[:, :, 1] = pink_tinted_image[:, :, 1] * 0.6  # Reduce green channel
    pink_tinted_image[:, :, 2] = pink_tinted_image[:, :, 2] * 1.5  # Enhance red channel
    pink_tinted_image = np.clip(pink_tinted_image, 0, 255)  # Ensure pixel values are valid
    return pink_tinted_image

# Function to apply a custom color filter
def apply_custom_color_filter(image, color_filter):
    custom_image = cv2.transform(image, color_filter)
    custom_image = np.clip(custom_image, 0, 255)  # Ensure pixel values are valid
    return custom_image

# Function to apply a teal-orange filter
def apply_teal_orange_tint(image):
    teal_orange_filter = np.array([[0.6, 0.2, 0.2],
                                   [0.2, 0.7, 0.1],
                                   [0.2, 0.1, 0.7]])
    teal_orange_image = cv2.transform(image, teal_orange_filter)
    teal_orange_image = np.clip(teal_orange_image, 0, 255)  # Ensure pixel values are valid
    return teal_orange_image

# Function to apply a golden-hour filter
def apply_golden_hour_tint(image):
    golden_hour_filter = np.array([[1.0, 0.5, 0.1],
                                   [0.1, 0.8, 0.2],
                                   [0.05, 0.1, 0.9]])
    golden_hour_image = cv2.transform(image, golden_hour_filter)
    golden_hour_image = np.clip(golden_hour_image, 0, 255)  # Ensure pixel values are valid
    return golden_hour_image

# Define a custom color filter (example: blue-green tint)
custom_filter = np.array([[0.1, 0.3, 0.6],
                          [0.1, 0.7, 0.2],
                          [0.1, 0.2, 0.7]])

# Apply sepia filter
sepia_image = apply_sepia(image)

# Save and display the sepia image
sepia_image_path = 'sepia_image.jpg'
cv2.imwrite(sepia_image_path, sepia_image)

plt.imshow(cv2.cvtColor(sepia_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Sepia Image')
plt.show()

print(f'Sepia image created and saved as "{sepia_image_path}".')

# Apply grayscale filter
grayscale_image = apply_grayscale(image)

# Save and display the grayscale image
grayscale_image_path = 'grayscale_image.jpg'
cv2.imwrite(grayscale_image_path, grayscale_image)

plt.imshow(cv2.cvtColor(grayscale_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Grayscale Image')
plt.show()

print(f'Grayscale image created and saved as "{grayscale_image_path}".')

# Apply pink-tinted filter to the grayscale image
pink_tinted_image = apply_pink_tint(grayscale_image)

# Save and display the pink-tinted image
pink_tinted_image_path = 'pink_tinted_image.jpg'
cv2.imwrite(pink_tinted_image_path, pink_tinted_image)

plt.imshow(cv2.cvtColor(pink_tinted_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Pink-Tinted Image')
plt.show()

print(f'Pink-tinted image created and saved as "{pink_tinted_image_path}".')

# Apply custom color filter
custom_image = apply_custom_color_filter(image, custom_filter)

# Save and display the custom color image
custom_image_path = 'custom_color_image.jpg'
cv2.imwrite(custom_image_path, custom_image)

plt.imshow(cv2.cvtColor(custom_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Custom Color Image')
plt.show()

print(f'Custom color image created and saved as "{custom_image_path}".')

# Apply teal-orange filter
teal_orange_image = apply_teal_orange_tint(image)

# Save and display the teal-orange image
teal_orange_image_path = 'teal_orange_image.jpg'
cv2.imwrite(teal_orange_image_path, teal_orange_image)

plt.imshow(cv2.cvtColor(teal_orange_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Teal-Orange Image')
plt.show()

print(f'Teal-orange image created and saved as "{teal_orange_image_path}".')

# Apply golden-hour filter
golden_hour_image = apply_golden_hour_tint(image)

# Save and display the golden-hour image
golden_hour_image_path = 'golden_hour_image.jpg'
cv2.imwrite(golden_hour_image_path, golden_hour_image)

plt.imshow(cv2.cvtColor(golden_hour_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Golden-Hour Image')
plt.show()

print(f'Golden-hour image created and saved as "{golden_hour_image_path}".')
