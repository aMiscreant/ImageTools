import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

# Ensure the output directory exists
output_dir = 'output_composition'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to create a collage from multiple images
def create_collage(image_paths, collage_size=(800, 600), grid_size=(2, 2)):
    collage = np.zeros((collage_size[1], collage_size[0], 3), dtype=np.uint8)
    img_h, img_w = collage_size[1] // grid_size[1], collage_size[0] // grid_size[0]

    for idx, image_path in enumerate(image_paths):
        if idx >= grid_size[0] * grid_size[1]:
            break
        img = cv2.imread(image_path)
        if img is not None:
            resized_img = cv2.resize(img, (img_w, img_h))
            row = idx // grid_size[0]
            col = idx % grid_size[0]
            collage[row * img_h:(row + 1) * img_h, col * img_w:(col + 1) * img_w] = resized_img

    return collage

# Example paths for collage
image_paths = ['image1.jpg', 'image2.jpg', 'image3.jpg', 'image4.jpg']  # Replace with your image paths
collage = create_collage(image_paths)
collage_path = os.path.join(output_dir, 'collage.jpg')
cv2.imwrite(collage_path, collage)

plt.imshow(cv2.cvtColor(collage, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Collage')
plt.show()

print(f'Collage created and saved as "{collage_path}".')
