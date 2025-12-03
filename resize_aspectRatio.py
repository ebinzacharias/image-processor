from PIL import Image
import os

def resize_images_fixed_resolution(input_dir, output_dir, width, height, quality=85, optimize=True):
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        file_list = os.listdir(input_dir)

        for filename in file_list:
            input_path = os.path.join(input_dir, filename)

            if os.path.isfile(input_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                img = Image.open(input_path)
                
                original_width, original_height = img.size
                aspect_ratio = original_width / original_height
                
                if aspect_ratio > (width / height):
                    new_width = width
                    new_height = int(width / aspect_ratio)
                else:
                    new_height = height
                    new_width = int(height * aspect_ratio)
                
                img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                
                file_ext = filename.lower().split('.')[-1]
                base_name = filename.rsplit('.', 1)[0]
                
                if file_ext in ['jpg', 'jpeg']:
                    output_path = os.path.join(output_dir, f"{base_name}_resized.jpg")
                    img.save(output_path, format='JPEG', optimize=optimize, quality=quality)
                else:
                    output_path = os.path.join(output_dir, f"{base_name}_resized.png")
                    img.save(output_path, format='PNG', optimize=optimize)

        print("Image resizing with fixed resolution successful!")
    except Exception as e:
        print(f"Error during image resizing with fixed resolution: {e}")

input_image_directory = "images/"
output_directory = "images/resized/"
resize_images_fixed_resolution(input_image_directory, output_directory, width=1518, height=628, quality=85, optimize=True)




