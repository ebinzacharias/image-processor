# How to Run Tests - Quick Start

## Step 1: Activate Virtual Environment

**First time setup (already done, but here's the command):**
```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
pip install -r requirements.txt
```

**Every time you want to run tests:**
```bash
cd /Users/ebinzacharias/Desktop/Repos/image_Processing
source venv/bin/activate
```

You'll see `(venv)` appear in your terminal prompt when it's activated.

## Step 2: Run Tests

### 🚀 Quick Start - Run Everything

```bash
pytest
```

This runs all 45 tests. You'll see output like:
```
============================= test session starts ==============================
45 passed in 2.18s
============================== ✅ All tests passed! ===============================
```

### 📊 Run with Details

```bash
pytest -v
```

The `-v` (verbose) flag shows each individual test:
```
test_compress_jpeg_image PASSED [  2%]
test_compress_png_image PASSED [  4%]
test_quality_parameter_affects_jpeg PASSED [  6%]
...
```

### 🎯 Run Specific Tests

**Run tests for just one file:**
```bash
pytest tests/test_compress_images.py
```

**Run a specific test:**
```bash
pytest tests/test_compress_images.py::TestCompressImages::test_compress_jpeg_image
```

**Run tests matching a keyword:**
```bash
pytest -k "compress"     # Runs all compression tests
pytest -k "landscape"    # Runs all landscape-related tests
```

### 📈 Run with Coverage Report

See which parts of your code are tested:
```bash
pytest --cov=. --cov-report=term
```

Or generate an HTML report:
```bash
pytest --cov=. --cov-report=html
open htmlcov/index.html  # View in browser
```

## Common Commands

| Command | What It Does |
|---------|-------------|
| `pytest` | Run all tests (quick) |
| `pytest -v` | Run all tests (detailed output) |
| `pytest tests/test_compress_images.py` | Run only compression tests |
| `pytest -k "compress"` | Run tests with "compress" in name |
| `pytest --cov=.` | Run with coverage report |
| `./run_tests.sh` | Use the convenience script |

## Understanding Test Output

### ✅ PASSED
The test worked correctly!

```
test_compress_jpeg_image PASSED
```
Meaning: Your compression function successfully created a compressed JPEG.

### ❌ FAILED
Something didn't work as expected.

```
test_compress_jpeg_image FAILED
AssertionError: Compressed JPEG file should be created
```
Meaning: The test expected a file to exist, but it wasn't created.

### ⚠️ ERROR
The test itself had a problem (not your code).

```
test_compress_jpeg_image ERROR
ImportError: No module named 'compress_images'
```
Meaning: There's a setup issue, not a problem with your code.

## Real Examples

### Example 1: Test One Specific Feature

Let's test just the JPEG compression:
```bash
pytest tests/test_compress_images.py::TestCompressImages::test_compress_jpeg_image -v
```

**What happens:**
1. Creates a temporary folder
2. Creates a test JPEG image (800x600, red color)
3. Runs your compression function
4. Checks that compressed file exists and is valid
5. Cleans up temporary files

**Output:**
```
test_compress_jpeg_image PASSED [100%]
✅ Test passed in 0.03s
```

### Example 2: Test Quality Parameter

```bash
pytest tests/test_compress_images.py::TestCompressImages::test_quality_parameter_affects_jpeg -v
```

**What happens:**
1. Creates test image
2. Compresses with quality=10 (small file)
3. Compresses with quality=90 (large file)
4. Checks that quality=10 file is smaller
5. Verifies your function respects the quality setting

### Example 3: Run All Compression Tests

```bash
pytest tests/test_compress_images.py -v
```

**Output shows:**
- ✅ test_compress_jpeg_image
- ✅ test_compress_png_image
- ✅ test_quality_parameter_affects_jpeg
- ✅ test_optimize_flag_works
- ✅ test_multiple_images_in_directory
- ... and 5 more tests

## Troubleshooting

**Problem: "pytest: command not found"**
```bash
# Solution: Make sure virtual environment is activated
source venv/bin/activate
```

**Problem: "ImportError: No module named 'compress_images'"**
```bash
# Solution: Run from project root directory
cd /Users/ebinzacharias/Desktop/Repos/image_Processing
pytest
```

**Problem: Tests are slow**
```bash
# Run specific tests instead of all
pytest tests/test_compress_images.py  # Only compression tests
```

## Quick Reference Card

```bash
# Setup (one time)
source venv/bin/activate

# Daily use
pytest                    # Run all tests
pytest -v                 # Detailed output
pytest -k "compress"      # Filter by keyword

# Debugging
pytest -v -s              # Show print statements
pytest --pdb              # Drop into debugger on failure
```

## What Gets Tested?

- ✅ Image compression (JPEG & PNG)
- ✅ Quality settings
- ✅ Format preservation
- ✅ Aspect ratio resizing
- ✅ Image organization (landscape/portrait/square)
- ✅ Error handling
- ✅ Edge cases (empty folders, invalid files)

**Total: 45 automated tests covering all functionality!**

