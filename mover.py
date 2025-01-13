import os
import shutil
from tqdm import tqdm


def copy_images_to_folder(source_folder, destination_folder):
    """
    Copies all image files from the specified folder and its subfolders to the given destination folder.

    :param source_folder: Path to the folder containing the images.
    :param destination_folder: Path to the destination folder where images will be copied.
    """
    if not os.path.exists(source_folder):
        raise FileNotFoundError(f"The folder {source_folder} does not exist.")

    if not os.path.exists(destination_folder):
        os.makedirs(
            destination_folder
        )  # Create the destination folder if it does not exist

    # Supported image formats
    supported_formats = (".png", ".jpg", ".jpeg", ".bmp", ".gif", ".tiff")

    # Collect all image files
    image_files = []
    for root, _, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith(supported_formats):
                image_files.append((root, file))

    # Iterate over image files with progress bar
    for root, file in tqdm(image_files, desc="Copying images", unit="file"):
        source_path = os.path.join(root, file)
        destination_path = os.path.join(destination_folder, file)

        try:
            # Skip if file already exists in the destination folder
            if os.path.exists(destination_path):
                print(f"Skipped (duplicate): {source_path}")
                continue

            shutil.copy(source_path, destination_path)
            print(f"Copied: {source_path} -> {destination_path}")
        except Exception as e:
            print(f"Failed to copy {source_path}: {e}")


if __name__ == "__main__":
    # Input folder containing images and subfolders
    source_folder = input(
        "Enter the path to the folder containing images and subfolders: "
    )

    # Input folder to copy images to
    destination_folder = input("Enter the path to the destination folder: ")

    try:
        copy_images_to_folder(source_folder, destination_folder)
        print("All images have been copied to the destination folder.")
    except Exception as e:
        print(f"An error occurred: {e}")
