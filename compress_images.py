from PIL import Image
import os

def compress_images_in_directory(input_dir, output_dir, quality, optimize):
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        file_list = os.listdir(input_dir)

        for filename in file_list:
            input_path = os.path.join(input_dir, filename)

            if os.path.isfile(input_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                img = Image.open(input_path)
                
                file_ext = filename.lower().split('.')[-1]
                base_name = filename.rsplit('.', 1)[0]
                
                if file_ext in ['jpg', 'jpeg']:
                    output_path = os.path.join(output_dir, f"{base_name}_compressed.jpg")
                    img.save(output_path, format='JPEG', optimize=optimize, quality=quality)
                else:
                    output_path = os.path.join(output_dir, f"{base_name}_compressed.png")
                    img.save(output_path, format='PNG', optimize=optimize)

        print("Image compression successful!")
    except Exception as e:
        print(f"Error during image compression: {e}")

input_image_directory = "images/"
output_directory = "images/compressed/"
compress_images_in_directory(input_image_directory, output_directory, quality=50, optimize=True)


