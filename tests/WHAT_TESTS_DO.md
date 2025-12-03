# What Do the Tests Do?

## Overview

The tests automatically verify that your image processing scripts work correctly. Instead of manually testing each feature, the tests do it automatically and check that everything behaves as expected.

## What Each Test Does

### 1. Image Compression Tests (`test_compress_images.py`)

These tests verify that the `compress_images.py` script works correctly:

**Example: `test_compress_jpeg_image`**
- Creates a test JPEG image (800x600 red image)
- Runs your compression function on it
- Checks that:
  - ✅ A compressed file was created
  - ✅ The file can be opened
  - ✅ It's still a JPEG (not corrupted)
  - ✅ The format is preserved

**Example: `test_quality_parameter_affects_jpeg`**
- Compresses the same image with quality=10 (low)
- Compresses the same image with quality=90 (high)
- Checks that:
  - ✅ Low quality produces a smaller file
  - ✅ High quality produces a larger file

**Other tests check:**
- PNG compression works
- Multiple images in a folder
- Empty folders don't crash
- Non-image files are ignored

### 2. Resize Tests (`test_resize_aspectRatio.py`)

These verify that images resize correctly while keeping proportions:

**Example: `test_aspect_ratio_preserved`**
- Takes an 800x600 image (ratio = 1.33)
- Resizes it to fit within 1518x628
- Checks that:
  - ✅ The new dimensions still have ratio = 1.33
  - ✅ The image fits within the target bounds
  - ✅ No distortion occurred

**Example: `test_wider_image_resizes_correctly`**
- Creates a very wide image (2000x500)
- Resizes to fit 800x600
- Checks that:
  - ✅ Width becomes 800 (fits constraint)
  - ✅ Height is calculated correctly (200 to maintain ratio)

### 3. Organization Tests (`test_organize_datatypes.py`)

These verify that images are sorted into correct folders:

**Example: `test_is_landscape_image`**
- Creates a wide image (1600x800 = ratio 2.0)
- Creates a tall image (600x1200 = ratio 0.5)
- Creates a square image (1000x1000 = ratio 1.0)
- Checks that:
  - ✅ Wide image is detected as landscape
  - ✅ Tall image is NOT detected as landscape
  - ✅ Square image is NOT detected as landscape

**Example: `test_organize_landscape_image`**
- Creates a landscape image
- Runs the organization function
- Checks that:
  - ✅ It's copied to `landscape_images/` folder
  - ✅ Original file still exists (copied, not moved)
  - ✅ Directory structure is created

## How Tests Work Behind the Scenes

1. **Fixtures** (in `conftest.py`) create test data:
   - Temporary folders (automatically cleaned up)
   - Sample images (JPEG, PNG, landscape, portrait, square)

2. **Each test**:
   - Gets a fresh temporary folder
   - Creates test images in it
   - Runs your function
   - Checks the results with `assert` statements
   - Cleans up automatically

3. **Assertions** check that:
   - Files exist where expected
   - Dimensions are correct
   - Formats are preserved
   - File sizes make sense

## Test Results Explained

When you run tests, you'll see:

```
PASSED ✅ - Test worked correctly
FAILED ❌ - Something didn't work as expected (shows what went wrong)
ERROR ⚠️  - Test itself had a problem (not your code)

```

**Example output:**
```
test_compress_jpeg_image PASSED     ✅ Compression works!
test_compress_png_image PASSED      ✅ PNG compression works!
test_quality_parameter FAILED       ❌ Quality didn't affect file size (bug!)
```

## Why Tests Are Useful

1. **Automatic Verification**: Run all tests to check everything works
2. **Catch Bugs Early**: Find problems before they affect real images
3. **Safe Refactoring**: Change code confidently, tests verify it still works
4. **Documentation**: Tests show how functions should be used
5. **Prevent Regressions**: New changes don't break old functionality

## Real-World Example

**Without tests:**
- Manually compress 10 images
- Check each one opened correctly
- Compare file sizes
- Takes 10 minutes, easy to miss problems

**With tests:**
- Run `pytest` (2 seconds)
- Automatically tests 45 scenarios
- Shows exactly what passed/failed
- Catches edge cases you might miss

