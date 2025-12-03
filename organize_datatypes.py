import os
import shutil
from PIL import Image

def get_aspect_ratio(image_path):
    try:
        img = Image.open(image_path)
        width, height = img.size
        return width / height
    except Exception as e:
        print(f"Error while calculating aspect ratio: {e}")
        return 0

def is_landscape_image(image_path):
    try:
        aspect_ratio = get_aspect_ratio(image_path)
        return aspect_ratio > 1.5
    except Exception as e:
        print(f"Error while checking landscape image: {e}")
        return False

def is_portrait_image(image_path):
    try:
        aspect_ratio = get_aspect_ratio(image_path)
        return aspect_ratio < 1.0
    except Exception as e:
        print(f"Error while checking portrait image: {e}")
        return False

def is_square_image(image_path):
    try:
        aspect_ratio = get_aspect_ratio(image_path)
        return 1.0 <= aspect_ratio <= 1.5
    except Exception as e:
        print(f"Error while checking square image: {e}")
        return False

def is_video_file(file_path):
    video_extensions = ('.mov', '.mp4')
    return file_path.lower().endswith(video_extensions)

def is_image_file(file_path):
    image_extensions = ('.jpeg', '.jpg', '.png')
    return file_path.lower().endswith(image_extensions)

def count_files(folder):
    count = 0
    for root, _, files in os.walk(folder):
        count += len(files)
    return count

def detect_and_copy_images(source_folder, destination_folder):
    try:
        total_files_before = count_files(source_folder)

        os.makedirs(os.path.join(destination_folder, 'landscape_images'), exist_ok=True)
        os.makedirs(os.path.join(destination_folder, 'portrait_images'), exist_ok=True)
        os.makedirs(os.path.join(destination_folder, 'square_images'), exist_ok=True)
        os.makedirs(os.path.join(destination_folder, 'videos'), exist_ok=True)

        total_copied = 0

        for root, _, files in os.walk(source_folder):
            for filename in files:
                file_path = os.path.join(root, filename)

                if is_image_file(file_path):
                    if is_landscape_image(file_path):
                        destination_subfolder = os.path.join(destination_folder, 'landscape_images')
                    elif is_portrait_image(file_path):
                        destination_subfolder = os.path.join(destination_folder, 'portrait_images')
                    elif is_square_image(file_path):
                        destination_subfolder = os.path.join(destination_folder, 'square_images')
                    else:
                        continue

                    relative_path = os.path.relpath(file_path, source_folder)
                    destination_path = os.path.join(destination_subfolder, relative_path)
                    os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                    shutil.copy(file_path, destination_path)
                    total_copied += 1

                elif is_video_file(file_path):
                    relative_path = os.path.relpath(file_path, source_folder)
                    destination_path = os.path.join(destination_folder, 'videos', relative_path)
                    os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                    shutil.copy(file_path, destination_path)
                    total_copied += 1

        total_files_after = count_files(destination_folder)

        print(f"Total files before organizing: {total_files_before}")
        print(f"Total files copied to new folders: {total_copied}")
        print(f"Total files after organizing: {total_files_after}")

        print("Images and videos organized successfully!")
    except Exception as e:
        print(f"Error while organizing images and videos: {e}")

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Organize images and videos by orientation and type')
    parser.add_argument('source_folder', help='Source folder containing images and videos')
    parser.add_argument('destination_folder', help='Destination folder for organized files')
    
    args = parser.parse_args()
    detect_and_copy_images(args.source_folder, args.destination_folder)

if __name__ == "__main__":
    main()

