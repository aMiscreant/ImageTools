import cv2
import numpy as np
import os
import argparse
import imageio
import matplotlib.pyplot as plt


# Function to parse command line arguments
def parse_args():
    parser = argparse.ArgumentParser(description='Animate Any Image to create a GIF.')
    parser.add_argument('image_path', type=str, nargs='?', default=None, help='Path to the image to animate')
    parser.add_argument('--output_dir', type=str, default='output_animation',
                        help='Directory to save output frames and GIF')
    parser.add_argument('--num_frames', type=int, default=30, help='Number of frames for the animation')
    parser.add_argument('--duration', type=float, default=0.1, help='Duration between frames in the GIF')
    parser.add_argument('--loop', action='store_true', help='Set if the GIF should loop indefinitely')
    args = parser.parse_args()

    if not args.image_path:
        parser.print_help()
        exit()

    return args


# Function to animate any image
def animate_image(image, num_frames=30):
    height, width, _ = image.shape
    frames = []

    for i in range(num_frames):
        # Create a slight zoom effect for animation
        scale_factor = 1 + 0.02 * np.sin(2 * np.pi * i / num_frames)  # Creates a looped zoom in and out
        new_size = (int(width * scale_factor), int(height * scale_factor))
        resized_image = cv2.resize(image, new_size)

        # Center the resized image on a black background of the original size
        black_background = np.zeros((height, width, 3), dtype=np.uint8)
        offset_y = (height - new_size[1]) // 2
        offset_x = (width - new_size[0]) // 2
        black_background[offset_y:offset_y + new_size[1], offset_x:offset_x + new_size[0]] = resized_image

        frames.append(black_background)

    return frames


# Main function
def main():
    args = parse_args()

    # Load the image
    image = cv2.imread(args.image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found at path: {args.image_path}")

    # Ensure the output directory exists
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    # Generate animation frames
    frames = animate_image(image, num_frames=args.num_frames)

    # Save each frame
    for i, frame in enumerate(frames):
        frame_path = os.path.join(args.output_dir, f'frame_{i:03d}.png')
        cv2.imwrite(frame_path, frame)

    # Convert frames to RGB format for GIF creation
    frames_rgb = [cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) for frame in frames]

    # Create a GIF
    gif_path = os.path.join(args.output_dir, 'animated_image.gif')
    loop_option = 0 if args.loop else 1  # 0 for loop indefinitely, 1 for no loop
    imageio.mimsave(gif_path, frames_rgb, format='GIF', duration=args.duration, loop=loop_option)

    print(f'Animated GIF created and saved as "{gif_path}".')


if __name__ == '__main__':
    main()
