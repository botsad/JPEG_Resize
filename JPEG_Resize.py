from PIL import Image
import os


def compress_image(input_image_path, output_image_path):
    image = Image.open(input_image_path)
    if image.mode != 'RGB':  # If the image is not in RGB mode, then convert it to RGB
        image = image.convert('RGB')
    image.save(output_image_path, quality=85)  # Set the compression quality to 85%


def process_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.lower().endswith(".jpg") or file_path.lower().endswith(".jpeg"):
                if os.path.getsize(file_path) > 1 * 1024 * 1024:  # Checking the file size (more than 1 MB)
                    compress_image(file_path, file_path)  # Save the compressed file instead of the original file


if __name__ == "__main__":
    photos_folder = "С:\\folder"
    process_folder(photos_folder)
