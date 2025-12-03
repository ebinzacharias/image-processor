"""
Tests for compress_images.py module.

This test suite covers:
- Image compression functionality
- Quality parameter handling
- Optimization flag behavior
- File format preservation (JPEG vs PNG)
- Error handling
"""
import os
import pytest
from PIL import Image
import sys

# Add parent directory to path to import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from compress_images import compress_images_in_directory


class TestCompressImages:
    """Test suite for image compression functionality."""

    def test_compress_jpeg_image(self, temp_dir, sample_image_jpeg):
        """Test compressing a JPEG image with default settings."""
        output_dir = os.path.join(temp_dir, "output")
        compress_images_in_directory(temp_dir, output_dir, quality=50, optimize=True)
        
        output_file = os.path.join(output_dir, "test_image_compressed.jpg")
        assert os.path.exists(output_file), "Compressed JPEG file should be created"
        
        # Verify the compressed image can be opened
        img = Image.open(output_file)
        assert img.format == 'JPEG', "Output should remain JPEG format"

    def test_compress_png_image(self, temp_dir, sample_image_png):
        """Test compressing a PNG image."""
        output_dir = os.path.join(temp_dir, "output")
        compress_images_in_directory(temp_dir, output_dir, quality=50, optimize=True)
        
        output_file = os.path.join(output_dir, "test_image_compressed.png")
        assert os.path.exists(output_file), "Compressed PNG file should be created"
        
        # Verify the compressed image can be opened
        img = Image.open(output_file)
        assert img.format == 'PNG', "Output should remain PNG format"

    def test_quality_parameter_affects_jpeg(self, temp_dir, sample_image_jpeg):
        """Test that quality parameter affects JPEG file size."""
        output_dir_low = os.path.join(temp_dir, "output_low")
        output_dir_high = os.path.join(temp_dir, "output_high")
        
        compress_images_in_directory(temp_dir, output_dir_low, quality=10, optimize=True)
        compress_images_in_directory(temp_dir, output_dir_high, quality=90, optimize=True)
        
        low_quality_file = os.path.join(output_dir_low, "test_image_compressed.jpg")
        high_quality_file = os.path.join(output_dir_high, "test_image_compressed.jpg")
        
        low_size = os.path.getsize(low_quality_file)
        high_size = os.path.getsize(high_quality_file)
        
        assert low_size < high_size, "Lower quality should result in smaller file size"

    def test_optimize_flag_works(self, temp_dir, sample_image_jpeg):
        """Test that optimization flag works correctly."""
        output_dir_optimized = os.path.join(temp_dir, "output_optimized")
        output_dir_not_optimized = os.path.join(temp_dir, "output_not_optimized")
        
        compress_images_in_directory(temp_dir, output_dir_optimized, quality=50, optimize=True)
        compress_images_in_directory(temp_dir, output_dir_not_optimized, quality=50, optimize=False)
        
        optimized_file = os.path.join(output_dir_optimized, "test_image_compressed.jpg")
        not_optimized_file = os.path.join(output_dir_not_optimized, "test_image_compressed.jpg")
        
        assert os.path.exists(optimized_file), "Optimized file should exist"
        assert os.path.exists(not_optimized_file), "Non-optimized file should exist"

    def test_multiple_images_in_directory(self, temp_dir, sample_image_jpeg, sample_image_png):
        """Test compressing multiple images in a directory."""
        output_dir = os.path.join(temp_dir, "output")
        compress_images_in_directory(temp_dir, output_dir, quality=50, optimize=True)
        
        jpeg_output = os.path.join(output_dir, "test_image_compressed.jpg")
        png_output = os.path.join(output_dir, "test_image_compressed.png")
        
        assert os.path.exists(jpeg_output), "JPEG should be compressed"
        assert os.path.exists(png_output), "PNG should be compressed"

    def test_output_directory_creation(self, temp_dir, sample_image_jpeg):
        """Test that output directory is created if it doesn't exist."""
        output_dir = os.path.join(temp_dir, "new_output", "nested")
        assert not os.path.exists(output_dir), "Output directory should not exist initially"
        
        compress_images_in_directory(temp_dir, output_dir, quality=50, optimize=True)
        
        assert os.path.exists(output_dir), "Output directory should be created"

    def test_non_image_files_ignored(self, temp_dir, sample_image_jpeg):
        """Test that non-image files are ignored."""
        # Create a text file
        text_file = os.path.join(temp_dir, "test.txt")
        with open(text_file, 'w') as f:
            f.write("This is not an image")
        
        output_dir = os.path.join(temp_dir, "output")
        compress_images_in_directory(temp_dir, output_dir, quality=50, optimize=True)
        
        # Only image should be compressed
        output_files = os.listdir(output_dir)
        assert len(output_files) == 1, "Only image files should be processed"
        assert "test_image_compressed.jpg" in output_files

    def test_empty_directory(self, temp_dir, empty_directory):
        """Test handling of empty directory."""
        output_dir = os.path.join(temp_dir, "output")
        # Should not raise an error
        compress_images_in_directory(empty_directory, output_dir, quality=50, optimize=True)
        
        assert os.path.exists(output_dir), "Output directory should still be created"

    def test_preserves_image_dimensions(self, temp_dir, sample_image_jpeg):
        """Test that compression preserves image dimensions."""
        output_dir = os.path.join(temp_dir, "output")
        
        original_img = Image.open(sample_image_jpeg)
        original_size = original_img.size
        
        compress_images_in_directory(temp_dir, output_dir, quality=50, optimize=True)
        
        compressed_file = os.path.join(output_dir, "test_image_compressed.jpg")
        compressed_img = Image.open(compressed_file)
        compressed_size = compressed_img.size
        
        assert compressed_size == original_size, "Dimensions should be preserved"

    def test_handles_invalid_quality_values(self, temp_dir, sample_image_jpeg):
        """Test that function handles edge case quality values."""
        output_dir = os.path.join(temp_dir, "output")
        
        # Should not crash with extreme values
        compress_images_in_directory(temp_dir, output_dir, quality=1, optimize=True)
        compress_images_in_directory(temp_dir, output_dir, quality=100, optimize=True)
        
        output_file = os.path.join(output_dir, "test_image_compressed.jpg")
        assert os.path.exists(output_file), "File should be created even with extreme quality values"

