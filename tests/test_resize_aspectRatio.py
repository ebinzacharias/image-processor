"""
Tests for resize_aspectRatio.py module.

This test suite covers:
- Aspect ratio preservation during resizing
- Dimension calculations
- Quality and optimization parameters
- Different image formats
- Edge cases (already smaller, square images)
"""
import os
import pytest
from PIL import Image
import sys

# Add parent directory to path to import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from resize_aspectRatio import resize_images_fixed_resolution


class TestResizeAspectRatio:
    """Test suite for aspect ratio preserving resizing."""

    def test_resize_landscape_image(self, temp_dir, landscape_image):
        """Test resizing a landscape image while maintaining aspect ratio."""
        output_dir = os.path.join(temp_dir, "output")
        resize_images_fixed_resolution(
            temp_dir, output_dir, width=800, height=600, quality=85, optimize=True
        )
        
        output_file = os.path.join(output_dir, "landscape_resized.jpg")
        assert os.path.exists(output_file), "Resized file should be created"
        
        resized_img = Image.open(output_file)
        assert resized_img.width <= 800, "Width should not exceed target"
        assert resized_img.height <= 600, "Height should not exceed target"

    def test_resize_portrait_image(self, temp_dir, portrait_image):
        """Test resizing a portrait image while maintaining aspect ratio."""
        output_dir = os.path.join(temp_dir, "output")
        resize_images_fixed_resolution(
            temp_dir, output_dir, width=800, height=1200, quality=85, optimize=True
        )
        
        output_file = os.path.join(output_dir, "portrait_resized.jpg")
        assert os.path.exists(output_file), "Resized file should be created"
        
        resized_img = Image.open(output_file)
        assert resized_img.width <= 800, "Width should not exceed target"
        assert resized_img.height <= 1200, "Height should not exceed target"

    def test_aspect_ratio_preserved(self, temp_dir, sample_image_jpeg):
        """Test that aspect ratio is preserved after resizing."""
        output_dir = os.path.join(temp_dir, "output")
        
        original_img = Image.open(sample_image_jpeg)
        original_ratio = original_img.width / original_img.height
        
        resize_images_fixed_resolution(
            temp_dir, output_dir, width=1518, height=628, quality=85, optimize=True
        )
        
        output_file = os.path.join(output_dir, "test_image_resized.jpg")
        resized_img = Image.open(output_file)
        resized_ratio = resized_img.width / resized_img.height
        
        # Allow small floating point differences
        assert abs(original_ratio - resized_ratio) < 0.01, "Aspect ratio should be preserved"

    def test_fits_within_bounds(self, temp_dir, sample_image_jpeg):
        """Test that resized image fits within specified bounds."""
        output_dir = os.path.join(temp_dir, "output")
        target_width, target_height = 1518, 628
        
        resize_images_fixed_resolution(
            temp_dir, output_dir, width=target_width, height=target_height, quality=85, optimize=True
        )
        
        output_file = os.path.join(output_dir, "test_image_resized.jpg")
        resized_img = Image.open(output_file)
        
        assert resized_img.width <= target_width, "Width should fit within bounds"
        assert resized_img.height <= target_height, "Height should fit within bounds"

    def test_wider_image_resizes_correctly(self, temp_dir):
        """Test resizing an image that is wider than target ratio."""
        # Create a very wide image (e.g., 2000x500, ratio = 4.0)
        wide_img_path = os.path.join(temp_dir, "wide.jpg")
        img = Image.new('RGB', (2000, 500), color='red')
        img.save(wide_img_path, format='JPEG')
        
        output_dir = os.path.join(temp_dir, "output")
        resize_images_fixed_resolution(
            temp_dir, output_dir, width=800, height=600, quality=85, optimize=True
        )
        
        output_file = os.path.join(output_dir, "wide_resized.jpg")
        resized_img = Image.open(output_file)
        
        # Should fit width constraint (800) and calculate height accordingly
        assert resized_img.width == 800, "Width should match target for wide images"
        assert resized_img.height == 200, "Height should be calculated to maintain ratio"

    def test_taller_image_resizes_correctly(self, temp_dir):
        """Test resizing an image that is taller than target ratio."""
        # Create a very tall image (e.g., 500x2000, ratio = 0.25)
        tall_img_path = os.path.join(temp_dir, "tall.jpg")
        img = Image.new('RGB', (500, 2000), color='blue')
        img.save(tall_img_path, format='JPEG')
        
        output_dir = os.path.join(temp_dir, "output")
        resize_images_fixed_resolution(
            temp_dir, output_dir, width=800, height=600, quality=85, optimize=True
        )
        
        output_file = os.path.join(output_dir, "tall_resized.jpg")
        resized_img = Image.open(output_file)
        
        # Should fit height constraint (600) and calculate width accordingly
        assert resized_img.height == 600, "Height should match target for tall images"
        assert resized_img.width == 150, "Width should be calculated to maintain ratio"

    def test_square_image_resizing(self, temp_dir, square_image):
        """Test resizing a square image."""
        output_dir = os.path.join(temp_dir, "output")
        resize_images_fixed_resolution(
            temp_dir, output_dir, width=500, height=500, quality=85, optimize=True
        )
        
        output_file = os.path.join(output_dir, "square_resized.jpg")
        resized_img = Image.open(output_file)
        
        # Square image should remain square
        assert resized_img.width == resized_img.height, "Square image should remain square"

    def test_png_format_preserved(self, temp_dir, sample_image_png):
        """Test that PNG format is preserved during resizing."""
        output_dir = os.path.join(temp_dir, "output")
        resize_images_fixed_resolution(
            temp_dir, output_dir, width=400, height=400, quality=85, optimize=True
        )
        
        output_file = os.path.join(output_dir, "test_image_resized.png")
        assert os.path.exists(output_file), "PNG file should be created"
        
        resized_img = Image.open(output_file)
        assert resized_img.format == 'PNG', "Format should remain PNG"

    def test_quality_parameter_affects_jpeg(self, temp_dir, sample_image_jpeg):
        """Test that quality parameter affects resized JPEG file size."""
        output_dir_low = os.path.join(temp_dir, "output_low")
        output_dir_high = os.path.join(temp_dir, "output_high")
        
        resize_images_fixed_resolution(
            temp_dir, output_dir_low, width=400, height=300, quality=10, optimize=True
        )
        resize_images_fixed_resolution(
            temp_dir, output_dir_high, width=400, height=300, quality=90, optimize=True
        )
        
        low_quality_file = os.path.join(output_dir_low, "test_image_resized.jpg")
        high_quality_file = os.path.join(output_dir_high, "test_image_resized.jpg")
        
        low_size = os.path.getsize(low_quality_file)
        high_size = os.path.getsize(high_quality_file)
        
        assert low_size < high_size, "Lower quality should result in smaller file size"

    def test_already_smaller_image(self, temp_dir):
        """Test resizing an image that's already smaller than target."""
        small_img_path = os.path.join(temp_dir, "small.jpg")
        img = Image.new('RGB', (100, 100), color='green')
        img.save(small_img_path, format='JPEG')
        
        output_dir = os.path.join(temp_dir, "output")
        resize_images_fixed_resolution(
            temp_dir, output_dir, width=800, height=600, quality=85, optimize=True
        )
        
        output_file = os.path.join(output_dir, "small_resized.jpg")
        resized_img = Image.open(output_file)
        
        # Image should be scaled up to fit within bounds
        assert resized_img.width <= 800, "Should fit within bounds"
        assert resized_img.height <= 600, "Should fit within bounds"

    def test_output_directory_creation(self, temp_dir, sample_image_jpeg):
        """Test that output directory is created if it doesn't exist."""
        output_dir = os.path.join(temp_dir, "new_output", "nested")
        assert not os.path.exists(output_dir), "Output directory should not exist initially"
        
        resize_images_fixed_resolution(
            temp_dir, output_dir, width=400, height=300, quality=85, optimize=True
        )
        
        assert os.path.exists(output_dir), "Output directory should be created"

