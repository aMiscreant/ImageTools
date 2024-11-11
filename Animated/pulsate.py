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

# Define parameters for the pulsating effect
scale_range = (0.9, 1.1)  # The min and max scale factors
num_frames = 30  # Total number of frames for one cycle

# List to store frames for GIF creation
gif_frames = []

# Apply the pulsating effect
frame_count = 0
height, width = image.shape[:2]  # Original dimensions

def create_frame(_scale_factor, _frame_count):
    global gif_frames
    # Calculate new size
    new_size = (int(width * _scale_factor), int(height * _scale_factor))

    # Resize the image
    resized_image = cv2.resize(image, new_size)

    # Create a black background of the original size
    black_background = np.zeros((height, width, 3), dtype=np.uint8)
    offset_y = (height - new_size[1]) // 2
    offset_x = (width - new_size[0]) // 2

    # Ensure the resized image fits within the black background
    if offset_y >= 0 and offset_x >= 0:
        black_background[offset_y:offset_y + new_size[1], offset_x:offset_x + new_size[0]] = resized_image
    else:
        return  # Skip if resizing goes out of bounds

    # Convert BGR to RGB for GIF compatibility
    black_background_rgb = cv2.cvtColor(black_background, cv2.COLOR_BGR2RGB)
    gif_frames.append(black_background_rgb)

    # Save the altered image to the output directory
    output_path = os.path.join(output_dir, f'frame_{_frame_count:03d}.png')
    cv2.imwrite(output_path, black_background)

threads = []

for i in range(5):  # Number of cycles (adjust as needed)
    for frame_count, scale_factor in enumerate(np.linspace(scale_range[0], scale_range[1], num_frames), start=frame_count):
        t = threading.Thread(target=create_frame, args=(scale_factor, frame_count))
        threads.append(t)
        t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

# Display the frames with matplotlib
plt.ion()  # Enable interactive mode
for frame in gif_frames:
    plt.imshow(frame)
    plt.axis('off')
    plt.pause(0.03)  # Adjust to control the animation speed
plt.ioff()
plt.show()

# Create a GIF from the frames
gif_path = 'pulsating_image.gif'
imageio.mimsave(gif_path, gif_frames, duration=0.03, loop=0)  # Adjust `duration` for speed of GIF

print(f'Saved {frame_count} frames to the \"{output_dir}\" directory.')
print(f'GIF created and saved as \"{gif_path}\".')
