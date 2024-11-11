import argparse
from PIL import Image
import os
import logging

# Configure logging
logging.basicConfig(filename='resize_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the output directory path
output_dir = os.path.join(os.getcwd(), 'output')

# Check if the directory exists and handle cases accordingly
if os.path.exists(output_dir):
    if os.path.isdir(output_dir):
        print(f"Directory '{output_dir}' already exists.")
    else:
        print(f"'{output_dir}' exists but is not a directory. Please remove or rename the existing file.")
else:
    os.makedirs(output_dir)
    print(f"Directory '{output_dir}' created successfully.")

def is_image_file(file_path):
    """Check if the file is an image"""
    try:
        with Image.open(file_path) as img:
            return True
    except IOError:
        return False

def resize_image(input_path, output_path, sizes, quality=95, image_format="JPEG"):
    try:
        with Image.open(input_path) as img:
            for size in sizes:
                img_resized = img.resize(size, Image.LANCZOS)
                size_name = f"{size[0]}x{size[1]}"
                output_dir = os.path.join(output_path, size_name)
                os.makedirs(output_dir, exist_ok=True)
                output_file = os.path.join(output_dir, os.path.basename(input_path))
                img_resized.save(output_file, format=image_format, quality=quality)
                logging.info(f"Saved resized image to: {output_file}")
                print(f"Saved resized image to: {output_file}")
    except Exception as e:
        logging.error(f"Error resizing image {input_path}: {e}")
        print(f"Error resizing image {input_path}: {e}")

def get_sizes(category, subcategory=None):
    sizes_dict = {
        "Apparel": {
            "Baseball Caps & Dad Hats": [(2400, 1140)],
            "Bucket Hats": [(2040, 1140)],
            "Chiffon Tops": [(3711, 3814)],
            "Leggings": [(4350, 4032)],
            "Long & Premium T-Shirts": [(2875, 3900)],
            "Masks": [(2380, 1630)],
            "Men's Graphic T-Shirts": [(3873, 4814)],
            "Mini Skirts": [(2152, 2502)],
            "Pins": [(1000, 1000)],
            "Scarves": [(5748, 5748)],
            "Socks": [(5848, 6300)],
            "Women's A-Line Dress": [(6310, 6230)],
            "Women's Graphic Dress": [(4020, 6090)],
            "Women's Sleeveless Tops": [(3870, 4280)],
            "Other Apparel": [(2400, 3200)]
        },
        "Bags": {
            "All Over Print Tote Bags": [(2175, 2175), (2625, 2625), (2950, 2950)],
            "Backpacks": [(4575, 3900)],
            "Cotton Tote Bags": [(2400, 3200)],
            "Drawstring Bags": [(2475, 2775)],
            "Laptop Sleeves": [(4125, 2956)],
            "Zipper Pouches": [(4600, 3000)]
        },
        "Device Cases": {
            "iPad Cases & Skins": [(2696, 3305)],
            "iPhone Wallets": [(2087, 1956)],
            "Laptop Skins": [(4600, 3000)],
            "Phone Cases & Skins": [(1187, 1852)]
        },
        "Home Decor": {
            "Acrylic Blocks": [(1860, 1860)],
            "Aprons": [(4065, 4950)],
            "Art Board Prints": [(3060, 3060), (1560, 2160), (1260, 1860), (3360, 4260)],
            "Bath Mats": [(6480, 4320)],
            "Clocks": [(2940, 2940)],
            "Coasters": [(1860, 1860)],
            "Duvet Covers & Comforters": [(7632, 6480)],
            "Jigsaw puzzles": [(9075, 6201)],
            "Magnets": [(2800, 2800)],
            "MugsTravel Mug": [(2376, 2024)],
            "Standard Mug": [(2700, 1120)],
            "Tall Mug": [(2700, 1624)],
            "Shower Curtains": [(7632, 6480)],
            "Tapestries": [(7632, 6480)],
            "Throw Blankets": [(7632, 6480)],
            "Throw Pillows": [(3225, 3225)],
            "Water Bottles": [(3160, 2180)],
        },
        "Pet Supplies": {
            "Cat Mats": [(3150, 2400)],
            "Dog Mats": [(4800, 3657)],
            "Pet Bandanas": [(4500, 2700)],
            "Pet Blankets": [(7632, 6480)],
        },
        "Stationery": {
            "Greeting Cards": [(1300, 900)],
            "Desk Mats": [(8268, 4331)],
            "Hardcover Journals": [(3502, 2385)],
            "Mouse Pads": [(2559, 2165)],
            "Postcards": [(1300, 900)],
            "Spiral Notebooks": [(1756, 2481)],
            "Stickers": [(600, 800), (1100, 1100), (1700, 1700), (2800, 2800)]
        },
        "Wall Art": {
            "Art Prints": [(3840, 3840)],
            "Framed Art Prints & Stretched Canvas": [(2400, 1600), (3240, 2160), (3840, 2560), (4800, 4800)],
            "Metal Prints": [(2400, 2400), (3200, 3200), (3600, 3600), (3840, 3840), (4800, 4800)],
            "Photographic Prints": [(2500, 3500), (3500, 5000), (5000, 7100), (9144, 6096)],
            "Posters": [(2870, 4100), (4100, 5840), (5840, 8310), (8310, 11790)],
            "Canvas & Wood Mounted Prints": [(2646, 3236), (3945, 4890), (4535, 5480)]
        }
    }
    if subcategory and category in sizes_dict and isinstance(sizes_dict[category], dict):
        return sizes_dict[category].get(subcategory, [])
    return sizes_dict.get(category, [])

def main():
    parser = argparse.ArgumentParser(description="Resize images into various sizes for different categories.\n\nExample usage:\npython redbubble.py \"Stationery\" \"your_image.jpg\" \"output/\" --subcategory \"Greeting Cards\"")
    parser.add_argument("category", choices=["Apparel", "Bags", "Device Cases", "Home Decor", "Pet Supplies", "Stationery", "Wall Art"], help="Category to resize images for")
    parser.add_argument("input_path", help="Path to the input image or folder of images")
    parser.add_argument("output_path", help="Path to save the resized images")
    parser.add_argument("--subcategory", help="Subcategory for more specific sizing options (only applicable for certain categories)")
    parser.add_argument("--quality", type=int, default=95, help="Quality of the output image (1-100)")
    parser.add_argument("--format", choices=["JPEG", "PNG", "WEBP"], default="JPEG", help="Format of the output image")

    args = parser.parse_args()

    sizes = get_sizes(args.category, args.subcategory)
    if not sizes:
        print(f"No sizes found for category {args.category} with subcategory {args.subcategory}. Exiting.")
        return

    if os.path.isdir(args.input_path):
        image_files = [f for f in os.listdir(args.input_path) if os.path.isfile(os.path.join(args.input_path, f)) and is_image_file(os.path.join(args.input_path, f))]
        total_files = len(image_files)
        processed_files = 0

        for filename in image_files:
            file_path = os.path.join(args.input_path, filename)
            resize_image(file_path, args.output_path, sizes, args.quality, args.format)
            processed_files += 1
            print(f"Processed {processed_files}/{total_files} files")
    elif os.path.isfile(args.input_path) and is_image_file(args.input_path):
        resize_image(args.input_path, args.output_path, sizes, args.quality, args.format)
    else:
        print(f"Invalid input path: {args.input_path}")

if __name__ == "__main__":
    main()
