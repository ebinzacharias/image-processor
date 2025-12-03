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
- pytest >= 7.4.0 (for testing)
- pytest-cov >= 4.1.0 (for coverage reports)

## Testing

This project includes comprehensive test suites to ensure reliability and correctness of all image processing functionality.

### Running Tests

**Quick start (using convenience script):**
```bash
./run_tests.sh              # Run all tests
./run_tests.sh --coverage   # Run with coverage report
```

**Run all tests:**
```bash
pytest
```

**Run tests with verbose output:**
```bash
pytest -v
```

**Run a specific test file:**
```bash
pytest tests/test_compress_images.py
```

**Run a specific test class or function:**
```bash
pytest tests/test_compress_images.py::TestCompressImages::test_compress_jpeg_image
```

**Run tests with coverage report:**
```bash
pytest --cov=. --cov-report=html --cov-report=term
```

This generates:
- Terminal output showing coverage percentage
- HTML report in `htmlcov/index.html` (open in browser for detailed view)

**Run tests matching a pattern:**
```bash
pytest -k "compress"  # Runs all tests with "compress" in the name
```

### Test Structure

The test suite is organized in the `tests/` directory:

```
tests/
├── __init__.py
├── conftest.py                    # Shared fixtures and configuration
├── test_compress_images.py        # Tests for image compression
├── test_resize_aspectRatio.py     # Tests for aspect ratio resizing
└── test_organize_datatypes.py     # Tests for media organization
```

### Testing Practices

This project follows modern Python testing best practices:

1. **Fixtures for Test Data**: The `conftest.py` file provides reusable fixtures that create temporary directories and sample images for testing. This ensures:
   - Tests are isolated (each test gets fresh data)
   - No permanent files are created on disk
   - Tests can run in parallel without conflicts

2. **Comprehensive Test Coverage**: Each module has dedicated test files covering:
   - **Happy paths**: Normal operation with valid inputs
   - **Edge cases**: Boundary conditions (empty directories, extreme values)
   - **Error handling**: Invalid inputs, corrupted files
   - **Format preservation**: Ensuring JPEG/PNG formats are maintained
   - **Functionality verification**: Aspect ratios, dimensions, file sizes

3. **Test Organization**: Tests are organized by functionality:
   - Separate test classes for logical groupings
   - Descriptive test names that explain what is being tested
   - Each test is independent and can run in isolation

4. **Automated Fixture Cleanup**: Temporary directories and files are automatically cleaned up after each test using pytest's fixture teardown, preventing disk space issues.

### What is Tested

#### Image Compression (`test_compress_images.py`)
- ✅ JPEG and PNG format preservation
- ✅ Quality parameter effects on file size
- ✅ Optimization flag behavior
- ✅ Multiple images in directory
- ✅ Output directory creation
- ✅ Non-image file filtering
- ✅ Dimension preservation
- ✅ Edge case quality values

#### Aspect Ratio Resizing (`test_resize_aspectRatio.py`)
- ✅ Aspect ratio preservation
- ✅ Bounds checking (images fit within target dimensions)
- ✅ Wide vs tall image handling
- ✅ Square image resizing
- ✅ Format preservation (JPEG/PNG)
- ✅ Quality parameter effects
- ✅ Images smaller than target dimensions

#### Media Organization (`test_organize_datatypes.py`)
- ✅ Landscape/portrait/square detection
- ✅ Aspect ratio calculations
- ✅ File type detection (images vs videos)
- ✅ Directory structure creation
- ✅ File copying (not moving)
- ✅ Nested directory structure preservation
- ✅ Non-image file filtering
- ✅ File counting functionality

### Continuous Integration

To integrate testing into your development workflow:

1. **Pre-commit checks**: Run tests before committing:
   ```bash
   pytest && git commit
   ```

2. **CI/CD Pipeline**: Add to your CI configuration:
   ```yaml
   # Example for GitHub Actions
   - name: Run tests
     run: pytest --cov=. --cov-report=xml
   ```

3. **Coverage goals**: Aim for >80% code coverage. Current coverage can be checked with:
   ```bash
   pytest --cov=. --cov-report=term-missing
   ```

### Writing New Tests

When adding new functionality, follow these guidelines:

1. **Add tests in the appropriate test file** or create a new one if needed
2. **Use existing fixtures** from `conftest.py` when possible
3. **Follow naming convention**: `test_<functionality>` or `test_<condition>`
4. **Test one thing per test**: Keep tests focused and independent
5. **Use descriptive assertions**: Include clear error messages

Example test structure:
```python
def test_new_feature(self, temp_dir, sample_image_jpeg):
    """Test description explaining what is being tested."""
    # Arrange: Set up test data
    output_dir = os.path.join(temp_dir, "output")
    
    # Act: Execute the function being tested
    your_function(sample_image_jpeg, output_dir)
    
    # Assert: Verify the results
    assert os.path.exists(output_file), "Expected file should exist"
```

## Notes

These scripts process images in place and create output directories as needed. Make sure you have write permissions for the output directories.

