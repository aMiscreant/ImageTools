import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

# Load the images
image_path1 = 'your_image1.jpg'  # Replace with your first image path
image_path2 = 'your_image2.jpg'  # Replace with your second image path
image1 = cv2.imread(image_path1)
image2 = cv2.imread(image_path2)

if image1 is None or image2 is None:
    raise FileNotFoundError(f"One or both images not found at paths: {image_path1}, {image_path2}")

# Resize images to the same dimensions for blending
h, w = image1.shape[:2]
image2 = cv2.resize(image2, (w, h))

# Ensure the output directory exists and delete it if it does
output_dir = 'output_frames'
if os.path.exists(output_dir):
    os.makedirs(output_dir, exist_ok=True)

# Function to apply alpha blending of two images
def alpha_blend(image1, image2, alpha=0.5):
    blended_image = cv2.addWeighted(image1, alpha, image2, 1 - alpha, 0)
    return blended_image

# Function to overlay an image with transparency
def overlay_image(background, overlay, x=0, y=0, alpha=0.5):
    # Check if the overlay image has an alpha channel
    if overlay.shape[2] == 4:
        h, w = overlay.shape[:2]
        overlay_resized = overlay.copy()

        # Create a mask and inverse mask
        overlay_mask = overlay_resized[:, :, 3] / 255.0
        inverse_mask = 1.0 - overlay_mask

        # Iterate through each color channel
        for c in range(0, 3):
            background[y:y+h, x:x+w, c] = (overlay_mask * overlay_resized[:, :, c] +
                                           inverse_mask * background[y:y+h, x:x+w, c])
    else:
        print("Overlay image does not have an alpha channel. Ensure the image is RGBA format.")
        return background

    return background

# Apply alpha blending
alpha = 0.7  # Change this value to modify the blending ratio
blended_image = alpha_blend(image1, image2, alpha)
blended_image_path = 'blended_image.jpg'
cv2.imwrite(blended_image_path, blended_image)

plt.imshow(cv2.cvtColor(blended_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Blended Image')
plt.show()

print(f'Blended image created and saved as "{blended_image_path}".')

# Overlay effect with transparency (requires images with alpha channel)
overlay_image_path = 'overlay_image.jpg'  # Replace with an image that has an alpha channel
overlay = cv2.imread(overlay_image_path, cv2.IMREAD_UNCHANGED)
if overlay is not None:
    overlay_resized = cv2.resize(overlay, (w, h))
    overlaid_image = overlay_image(image1.copy(), overlay_resized)
    overlaid_image_path = 'overlaid_image.jpg'
    cv2.imwrite(overlaid_image_path, overlaid_image)

    plt.imshow(cv2.cvtColor(overlaid_image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title('Overlaid Image')
    plt.show()

    print(f'Overlaid image created and saved as "{overlaid_image_path}".')
else:
    print(f'Overlay image not found or does not have an alpha channel at path: {overlay_image_path}')
