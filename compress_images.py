from PIL import Image
import os
import argparse

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

def main():
    parser = argparse.ArgumentParser(description='Compress images in a directory')
    parser.add_argument('input_dir', help='Input directory containing images')
    parser.add_argument('output_dir', help='Output directory for compressed images')
    parser.add_argument('--quality', type=int, default=50, help='JPEG quality (1-100, default: 50)')
    parser.add_argument('--optimize', action='store_true', default=True, help='Optimize images (default: True)')
    parser.add_argument('--no-optimize', dest='optimize', action='store_false', help='Disable optimization')
    
    args = parser.parse_args()
    compress_images_in_directory(args.input_dir, args.output_dir, args.quality, args.optimize)

if __name__ == "__main__":
    main()


