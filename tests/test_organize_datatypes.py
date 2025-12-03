"""
Tests for organize_datatypes.py module.

This test suite covers:
- Image orientation detection (landscape, portrait, square)
- File type detection (images vs videos)
- File copying and organization
- Directory structure creation
- Error handling
"""
import os
import pytest
from PIL import Image
import sys

# Add parent directory to path to import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from organize_datatypes import (
    get_aspect_ratio,
    is_landscape_image,
    is_portrait_image,
    is_square_image,
    is_video_file,
    is_image_file,
    count_files,
    detect_and_copy_images
)


class TestAspectRatioFunctions:
    """Test suite for aspect ratio calculation functions."""

    def test_get_aspect_ratio_landscape(self, landscape_image):
        """Test getting aspect ratio for landscape image."""
        ratio = get_aspect_ratio(landscape_image)
        assert ratio > 1.5, "Landscape image should have ratio > 1.5"
        assert ratio == 2.0, "1600x800 should have ratio of 2.0"

    def test_get_aspect_ratio_portrait(self, portrait_image):
        """Test getting aspect ratio for portrait image."""
        ratio = get_aspect_ratio(portrait_image)
        assert ratio < 1.0, "Portrait image should have ratio < 1.0"
        assert ratio == 0.5, "600x1200 should have ratio of 0.5"

    def test_get_aspect_ratio_square(self, square_image):
        """Test getting aspect ratio for square image."""
        ratio = get_aspect_ratio(square_image)
        assert 1.0 <= ratio <= 1.5, "Square image should have ratio between 1.0 and 1.5"
        assert ratio == 1.0, "1000x1000 should have ratio of 1.0"

    def test_is_landscape_image(self, landscape_image, portrait_image, square_image):
        """Test landscape image detection."""
        assert is_landscape_image(landscape_image) == True, "Wide image should be detected as landscape"
        assert is_landscape_image(portrait_image) == False, "Tall image should not be landscape"
        assert is_landscape_image(square_image) == False, "Square image should not be landscape"

    def test_is_portrait_image(self, landscape_image, portrait_image, square_image):
        """Test portrait image detection."""
        assert is_portrait_image(landscape_image) == False, "Wide image should not be portrait"
        assert is_portrait_image(portrait_image) == True, "Tall image should be detected as portrait"
        assert is_portrait_image(square_image) == False, "Square image should not be portrait"

    def test_is_square_image(self, landscape_image, portrait_image, square_image):
        """Test square image detection."""
        assert is_square_image(landscape_image) == False, "Wide image should not be square"
        assert is_square_image(portrait_image) == False, "Tall image should not be square"
        assert is_square_image(square_image) == True, "Square image should be detected as square"


class TestFileTypeDetection:
    """Test suite for file type detection functions."""

    def test_is_image_file_jpeg(self, sample_image_jpeg):
        """Test JPEG image file detection."""
        assert is_image_file(sample_image_jpeg) == True, "JPEG file should be detected as image"
        assert is_image_file(sample_image_jpeg.upper()) == True, "Should be case insensitive"

    def test_is_image_file_png(self, sample_image_png):
        """Test PNG image file detection."""
        assert is_image_file(sample_image_png) == True, "PNG file should be detected as image"

    def test_is_image_file_negative(self, temp_dir):
        """Test that non-image files are not detected as images."""
        text_file = os.path.join(temp_dir, "test.txt")
        with open(text_file, 'w') as f:
            f.write("Not an image")
        assert is_image_file(text_file) == False, "Text file should not be detected as image"

    def test_is_video_file(self, temp_dir):
        """Test video file detection."""
        video_extensions = ['.mov', '.mp4', '.MOV', '.MP4']
        for ext in video_extensions:
            video_file = os.path.join(temp_dir, f"test{ext}")
            # Create empty file
            with open(video_file, 'w') as f:
                f.write("")
            assert is_video_file(video_file) == True, f"{ext} file should be detected as video"

    def test_is_video_file_negative(self, sample_image_jpeg):
        """Test that non-video files are not detected as videos."""
        assert is_video_file(sample_image_jpeg) == False, "Image file should not be detected as video"


class TestCountFiles:
    """Test suite for file counting function."""

    def test_count_files_empty_directory(self, empty_directory):
        """Test counting files in empty directory."""
        count = count_files(empty_directory)
        assert count == 0, "Empty directory should have 0 files"

    def test_count_files_with_images(self, temp_dir, sample_image_jpeg, sample_image_png):
        """Test counting files in directory with images."""
        count = count_files(temp_dir)
        assert count >= 2, "Should count at least 2 image files"

    def test_count_files_nested_structure(self, temp_dir):
        """Test counting files in nested directory structure."""
        subdir = os.path.join(temp_dir, "subdir")
        os.makedirs(subdir)
        
        file1 = os.path.join(temp_dir, "file1.jpg")
        file2 = os.path.join(subdir, "file2.jpg")
        
        img = Image.new('RGB', (100, 100), color='red')
        img.save(file1, format='JPEG')
        img.save(file2, format='JPEG')
        
        count = count_files(temp_dir)
        assert count == 2, "Should count files in nested directories"


class TestOrganizeImages:
    """Test suite for image organization functionality."""

    def test_organize_landscape_image(self, temp_dir, landscape_image):
        """Test organizing a landscape image."""
        dest_dir = os.path.join(temp_dir, "destination")
        detect_and_copy_images(temp_dir, dest_dir)
        
        landscape_dir = os.path.join(dest_dir, "landscape_images")
        assert os.path.exists(landscape_dir), "Landscape images directory should be created"
        
        # Check if file was copied
        files = os.listdir(landscape_dir)
        assert len(files) > 0, "Landscape image should be copied"

    def test_organize_portrait_image(self, temp_dir, portrait_image):
        """Test organizing a portrait image."""
        dest_dir = os.path.join(temp_dir, "destination")
        detect_and_copy_images(temp_dir, dest_dir)
        
        portrait_dir = os.path.join(dest_dir, "portrait_images")
        assert os.path.exists(portrait_dir), "Portrait images directory should be created"
        
        # Check if file was copied
        files = os.listdir(portrait_dir)
        assert len(files) > 0, "Portrait image should be copied"

    def test_organize_square_image(self, temp_dir, square_image):
        """Test organizing a square image."""
        dest_dir = os.path.join(temp_dir, "destination")
        detect_and_copy_images(temp_dir, dest_dir)
        
        square_dir = os.path.join(dest_dir, "square_images")
        assert os.path.exists(square_dir), "Square images directory should be created"
        
        # Check if file was copied
        files = os.listdir(square_dir)
        assert len(files) > 0, "Square image should be copied"

    def test_organize_multiple_image_types(self, temp_dir, landscape_image, portrait_image, square_image):
        """Test organizing multiple types of images."""
        dest_dir = os.path.join(temp_dir, "destination")
        detect_and_copy_images(temp_dir, dest_dir)
        
        landscape_dir = os.path.join(dest_dir, "landscape_images")
        portrait_dir = os.path.join(dest_dir, "portrait_images")
        square_dir = os.path.join(dest_dir, "square_images")
        
        assert os.path.exists(landscape_dir), "Landscape directory should exist"
        assert os.path.exists(portrait_dir), "Portrait directory should exist"
        assert os.path.exists(square_dir), "Square directory should exist"

    def test_destination_directories_created(self, temp_dir, sample_image_jpeg):
        """Test that all destination directories are created."""
        dest_dir = os.path.join(temp_dir, "destination")
        detect_and_copy_images(temp_dir, dest_dir)
        
        assert os.path.exists(os.path.join(dest_dir, "landscape_images"))
        assert os.path.exists(os.path.join(dest_dir, "portrait_images"))
        assert os.path.exists(os.path.join(dest_dir, "square_images"))
        assert os.path.exists(os.path.join(dest_dir, "videos"))

    def test_preserves_relative_path_structure(self, temp_dir, landscape_image):
        """Test that relative path structure is preserved."""
        # Create nested structure
        subdir = os.path.join(temp_dir, "subdir", "nested")
        os.makedirs(subdir)
        
        nested_image = os.path.join(subdir, "landscape.jpg")
        img = Image.new('RGB', (1600, 800), color='red')
        img.save(nested_image, format='JPEG')
        
        dest_dir = os.path.join(temp_dir, "destination")
        detect_and_copy_images(temp_dir, dest_dir)
        
        # Check if nested structure is preserved
        expected_path = os.path.join(dest_dir, "landscape_images", "subdir", "nested", "landscape.jpg")
        assert os.path.exists(expected_path), "Nested structure should be preserved"

    def test_copies_images_not_moves(self, temp_dir, landscape_image):
        """Test that images are copied, not moved (original should still exist)."""
        dest_dir = os.path.join(temp_dir, "destination")
        detect_and_copy_images(temp_dir, dest_dir)
        
        assert os.path.exists(landscape_image), "Original image should still exist after copying"

    def test_non_image_files_ignored(self, temp_dir, sample_image_jpeg):
        """Test that non-image files are ignored."""
        # Create a text file
        text_file = os.path.join(temp_dir, "test.txt")
        with open(text_file, 'w') as f:
            f.write("Not an image")
        
        dest_dir = os.path.join(temp_dir, "destination")
        detect_and_copy_images(temp_dir, dest_dir)
        
        # Text file should not appear in any organized folder
        for folder_name in ["landscape_images", "portrait_images", "square_images", "videos"]:
            folder_path = os.path.join(dest_dir, folder_name)
            if os.path.exists(folder_path):
                files = os.listdir(folder_path)
                assert "test.txt" not in str(files), "Text file should not be copied"

    def test_empty_source_directory(self, temp_dir, empty_directory):
        """Test organizing an empty directory."""
        dest_dir = os.path.join(temp_dir, "destination")
        # Should not raise an error
        detect_and_copy_images(empty_directory, dest_dir)
        
        # Directories should still be created
        assert os.path.exists(os.path.join(dest_dir, "landscape_images"))

    def test_handles_invalid_image_file(self, temp_dir):
        """Test handling of invalid/corrupted image files."""
        # Create a fake image file
        fake_image = os.path.join(temp_dir, "fake.jpg")
        with open(fake_image, 'w') as f:
            f.write("This is not a real image")
        
        dest_dir = os.path.join(temp_dir, "destination")
        # Should not crash, but may skip invalid files
        detect_and_copy_images(temp_dir, dest_dir)
        
        # Function should complete without error

