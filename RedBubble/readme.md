# Image Resizer Script for RedBubble Product Sizes

This script resizes images to match specific size requirements for various Redbubble products. It supports different categories and subcategories, ensuring images are appropriately resized for each product type.

## Features
- **Supports multiple categories and subcategories** (e.g., Apparel, Wall Art, Stationery).
- **Batch processing** for resizing all images in a folder.
- **Customizable image quality and format**.
- **Logs** errors and successful operations for tracking.
- **Progress reporting** during batch processing.

## Prerequisites
- Python 3.x
- `Pillow` library for image processing

Install `Pillow` using pip if you haven't already:
```bash
pip install Pillow
```

## Usage
### Command-Line Arguments
```bash
python redbubble.py <category> <input_path> <output_path> [--subcategory <subcategory>] [--quality <quality>] [--format <format>]
```

### Arguments
- **`<category>`**: The product category (e.g., `Stationery`, `Wall Art`).
- **`<input_path>`**: Path to the input image or folder of images.
- **`<output_path>`**: Path to save the resized images.
- **`--subcategory <subcategory>`**: (Optional) Subcategory for specific sizing options (e.g., `Greeting Cards`).
- **`--quality <quality>`**: (Optional) Quality of the output image (1-100). Default is 95.
- **`--format <format>`**: (Optional) Format of the output image (`JPEG`, `PNG`, `WEBP`). Default is `JPEG`.

### Example Usage
Resize a single image for `Stationery` under the subcategory `Greeting Cards`:
```bash
python redbubble.py "Stationery" "your_image.jpg" "output/" --subcategory "Greeting Cards"
```

Batch process all images in a folder for `Wall Art`:
```bash
python redbubble.py "Wall Art" "input_folder/" "output/"
```

## Directory Structure
The resized images are saved in subdirectories named after their sizes (e.g., `1300x900`), organized within the specified output folder.

## Logging
A log file named `resize_log.txt` is created in the current working directory, recording:
- Successful image processing
- Errors encountered during processing

## Additional Notes
Ensure the `input_path` only contains images or specify the path to an image file. Non-image files will be ignored.

## License
This project is provided under the MIT License.

