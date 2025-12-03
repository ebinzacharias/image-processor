# Image Processing Utilities

A collection of Python scripts for common image processing tasks. These utilities help with compressing images, resizing while maintaining aspect ratios, and organizing media files by their dimensions.

## Overview

I created these scripts to handle repetitive image processing tasks. Each script focuses on a specific use case and can be easily modified or integrated into larger projects.

## Features

- **Image Compression**: Reduce file sizes while maintaining visual quality
- **Aspect Ratio Resizing**: Resize images to target dimensions while preserving aspect ratios
- **Media Organization**: Automatically sort images and videos by orientation (landscape, portrait, square)

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Compress Images

Compresses images in a directory, preserving the original format (JPEG stays JPEG, PNG stays PNG).

```python
from compress_images import compress_images_in_directory

compress_images_in_directory(
    input_dir="images/",
    output_dir="images/compressed/",
    quality=50,
    optimize=True
)
```

The `quality` parameter (1-100) only applies to JPEG files. PNG files are optimized without quality loss.

### Resize Images with Aspect Ratio

Resizes images to fit within target dimensions while maintaining the original aspect ratio.

```python
from resize_aspectRatio import resize_images_fixed_resolution

resize_images_fixed_resolution(
    input_dir="images/",
    output_dir="images/resized/",
    width=1518,
    height=628,
    quality=85,
    optimize=True
)
```

Images are resized to fit within the specified width and height bounds without distortion.

### Organize Media Files

Sorts images and videos into folders based on their orientation and type.

```python
from organize_datatypes import detect_and_copy_images

detect_and_copy_images(
    source_folder="ssd/",
    destination_folder="ssd/_sorted/"
)
```

Images are categorized as:
- **Landscape**: Aspect ratio > 1.5
- **Portrait**: Aspect ratio < 1.0
- **Square**: Aspect ratio between 1.0 and 1.5

Videos are copied to a separate `videos` folder.

## Requirements

- Python 3.7+
- Pillow >= 10.0.0

## Notes

These scripts process images in place and create output directories as needed. Make sure you have write permissions for the output directories.

