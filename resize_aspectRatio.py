from PIL import Image
import os
import argparse

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

def main():
    parser = argparse.ArgumentParser(description='Resize images while maintaining aspect ratio')
    parser.add_argument('input_dir', help='Input directory containing images')
    parser.add_argument('output_dir', help='Output directory for resized images')
    parser.add_argument('--width', type=int, required=True, help='Target width in pixels')
    parser.add_argument('--height', type=int, required=True, help='Target height in pixels')
    parser.add_argument('--quality', type=int, default=85, help='JPEG quality (1-100, default: 85)')
    parser.add_argument('--optimize', action='store_true', default=True, help='Optimize images (default: True)')
    parser.add_argument('--no-optimize', dest='optimize', action='store_false', help='Disable optimization')
    
    args = parser.parse_args()
    resize_images_fixed_resolution(args.input_dir, args.output_dir, args.width, args.height, args.quality, args.optimize)

if __name__ == "__main__":
    main()




