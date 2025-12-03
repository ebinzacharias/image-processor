"""
Pytest configuration and shared fixtures for image processing tests.
"""
import pytest
import os
import tempfile
import shutil
from PIL import Image


@pytest.fixture
def temp_dir():
    """Create a temporary directory for testing."""
    temp_path = tempfile.mkdtemp()
    yield temp_path
    shutil.rmtree(temp_path)


@pytest.fixture
def sample_image_jpeg(temp_dir):
    """Create a sample JPEG image for testing."""
    img_path = os.path.join(temp_dir, "test_image.jpg")
    img = Image.new('RGB', (800, 600), color='red')
    img.save(img_path, format='JPEG', quality=95)
    return img_path


@pytest.fixture
def sample_image_png(temp_dir):
    """Create a sample PNG image for testing."""
    img_path = os.path.join(temp_dir, "test_image.png")
    img = Image.new('RGB', (600, 800), color='blue')
    img.save(img_path, format='PNG')
    return img_path


@pytest.fixture
def landscape_image(temp_dir):
    """Create a landscape-oriented image (width > height * 1.5)."""
    img_path = os.path.join(temp_dir, "landscape.jpg")
    img = Image.new('RGB', (1600, 800), color='green')
    img.save(img_path, format='JPEG')
    return img_path


@pytest.fixture
def portrait_image(temp_dir):
    """Create a portrait-oriented image (width < height)."""
    img_path = os.path.join(temp_dir, "portrait.jpg")
    img = Image.new('RGB', (600, 1200), color='yellow')
    img.save(img_path, format='JPEG')
    return img_path


@pytest.fixture
def square_image(temp_dir):
    """Create a square image (aspect ratio between 1.0 and 1.5)."""
    img_path = os.path.join(temp_dir, "square.jpg")
    img = Image.new('RGB', (1000, 1000), color='purple')
    img.save(img_path, format='JPEG')
    return img_path


@pytest.fixture
def image_directory(temp_dir, sample_image_jpeg, sample_image_png):
    """Create a directory with multiple test images."""
    # Images are already in temp_dir
    return temp_dir


@pytest.fixture
def empty_directory(temp_dir):
    """Create an empty temporary directory."""
    return temp_dir

