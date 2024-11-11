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

# List to store frames for GIF creation
gif_frames = []
frame_count = 0
height, width = image.shape[:2]  # Original dimensions

# Function to create fade transitions between images
def create_fade_transition(image1, image2, steps=15):
    frames = []
    for alpha in np.linspace(0, 1, steps):
        blended_image = cv2.addWeighted(image1, 1 - alpha, image2, alpha, 0)
        frames.append(blended_image)
    return frames

# Function to create slide transitions between images
def create_slide_transition(image1, image2, steps=15):
    frames = []
    h, w, _ = image1.shape
    for step in range(steps):
        dx = int(w * (step / steps))
        transition_image = np.zeros_like(image1)
        transition_image[:, :w-dx] = image1[:, dx:]
        transition_image[:, w-dx:] = image2[:, :dx]
        frames.append(transition_image)
    return frames

# Function to create and save animation frames
def create_frame(_frame, _frame_count):
    global gif_frames
    gif_frames.append(_frame)
    output_path = os.path.join(output_dir, f'frame_{_frame_count:03d}.png')
    cv2.imwrite(output_path, _frame)

threads = []

for i in range(5):  # Number of cycles (adjust as needed)
    # Example using the same image flipped horizontally as a transition pair
    img1 = image
    img2 = cv2.flip(image, 1)

    if img1.shape != img2.shape:
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    # Generate and save fade transition frames
    transition_frames = create_fade_transition(img1, img2)
    for frame in transition_frames:
        t = threading.Thread(target=create_frame, args=(frame, frame_count))
        threads.append(t)
        t.start()
        frame_count += 1

    # Generate and save slide transition frames
    slide_transition_frames = create_slide_transition(img1, img2)
    for frame in slide_transition_frames:
        t = threading.Thread(target=create_frame, args=(frame, frame_count))
        threads.append(t)
        t.start()
        frame_count += 1

# Wait for all threads to complete
for t in threads:
    t.join()

# Convert frames to RGB format for GIF creation
gif_frames_rgb = [cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) for frame in gif_frames]

# Save as GIF
gif_path = 'animated_image.gif'
imageio.mimsave(gif_path, gif_frames_rgb, format='GIF', duration=0.1)

print(f'Saved {frame_count} frames to the "{output_dir}" directory.')
print(f'GIF created and saved as "{gif_path}".')

# Display the GIF using matplotlib
plt.ion()  # Enable interactive mode
for frame in gif_frames_rgb:
    plt.imshow(frame)
    plt.axis('off')
    plt.pause(0.03)  # Adjust to control the animation speed
plt.ioff()
plt.show()
