# MTG Card Processing Scripts

This repository contains a collection of Python scripts designed to help process Magic: The Gathering custom card images for printing and organization.

## Scripts Overview

1. `resize_images_in_folder.py` - Resizes card images to the standard MTG card size (750×1050 px at 300 DPI)
2. `copy_images_to_folder.py` - Consolidates card images from multiple folders into a single destination folder
3. `images_to_pdf.py` - Creates a print-ready PDF with cards arranged in a 3×3 grid
4. `delete_duplicates.py` - (Optional) Removes duplicate card images
5. `main.py` - A wrapper script that runs all the above scripts in sequence

## Recommended Workflow

For the best results, either use the `main.py` script or follow this sequence:

1. **Organize Your Images** (`copy_images_to_folder.py`)
   - Use this script first to gather all your card images into a single folder
   - Input: Source folder containing scattered card images
   - Output: A single folder with all cards consolidated

2. **Resize Images** (`resize_images_in_folder.py`)
   - Ensures all cards are the correct size for printing
   - Input: Folder with consolidated images
   - Output: Same or new folder with properly sized images (750×1050 px)

3. **Create Print-Ready PDF** (`images_to_pdf.py`)
   - Arranges cards in a 3×3 grid format for printing
   - Each card is sized to 63mm × 88mm on the PDF
   - Input: Folder with resized images
   - Output: Print-ready PDF file

4. **Remove Duplicates** (Optional - `delete_duplicates.py`)
   - Can be run at any point to remove duplicate card images
   - Recommended to run before creating the PDF if needed

## Dependencies

- PIL (Python Imaging Library)
- fpdf
- tqdm
- os (standard library)
- shutil (standard library)

## Usage Notes

- Ensure all images are named uniquely, and backup your original images to avoid overwriting during processing
- Each script will prompt for the required input/output paths when run
- Scripts can handle common image formats (PNG, JPG, JPEG, BMP, GIF, TIFF)
- The PDF creation script automatically arranges cards in a 3×3 grid with proper card dimensions
- All scripts include progress bars to track processing status

## Error Handling

- All scripts include basic error handling for common issues
- Failed operations are reported but won't stop the entire process
- Invalid paths or unsupported file types are handled gracefully
