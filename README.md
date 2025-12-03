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

All scripts can be run from the command line with configurable paths and options.

### Compress Images

Compresses images in a directory, preserving the original format (JPEG stays JPEG, PNG stays PNG).

```bash
python compress_images.py <input_dir> <output_dir> [--quality QUALITY] [--optimize|--no-optimize]
```

**Examples:**
```bash
# Basic usage with default quality (50)
python compress_images.py images/ images/compressed/

# Custom quality setting
python compress_images.py images/ images/compressed/ --quality 75

# Disable optimization
python compress_images.py images/ images/compressed/ --quality 50 --no-optimize
```

The `quality` parameter (1-100) only applies to JPEG files. PNG files are optimized without quality loss.

**As a Python module:**
```python
from compress_images import compress_images_in_directory

compress_images_in_directory(
    input_dir="images/",
    output_dir="images/compressed/",
    quality=50,
    optimize=True
)
```

### Resize Images with Aspect Ratio

Resizes images to fit within target dimensions while maintaining the original aspect ratio.

```bash
python resize_aspectRatio.py <input_dir> <output_dir> --width WIDTH --height HEIGHT [--quality QUALITY] [--optimize|--no-optimize]
```

**Examples:**
```bash
# Resize to 1518x628
python resize_aspectRatio.py images/ images/resized/ --width 1518 --height 628

# Custom quality
python resize_aspectRatio.py images/ images/resized/ --width 1920 --height 1080 --quality 90
```

Images are resized to fit within the specified width and height bounds without distortion.

**As a Python module:**
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

### Organize Media Files

Sorts images and videos into folders based on their orientation and type.

```bash
python organize_datatypes.py <source_folder> <destination_folder>
```

**Example:**
```bash
python organize_datatypes.py ssd/ ssd/_sorted/
```

**As a Python module:**
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

