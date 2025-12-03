# Quick Testing Guide

## Setup (One-time)

1. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # OR
   venv\Scripts\activate     # On Windows
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests

### Basic Commands

**Run all tests:**
```bash
pytest
```

**Run all tests with verbose output:**
```bash
pytest -v
```

**Run all tests with coverage report:**
```bash
pytest --cov=. --cov-report=html --cov-report=term
```

This creates:
- Terminal output showing coverage percentage
- HTML report at `htmlcov/index.html` (open in browser)

### Running Specific Tests

**Run a specific test file:**
```bash
pytest tests/test_compress_images.py
```

**Run a specific test class:**
```bash
pytest tests/test_compress_images.py::TestCompressImages
```

**Run a specific test function:**
```bash
pytest tests/test_compress_images.py::TestCompressImages::test_compress_jpeg_image
```

**Run tests matching a pattern:**
```bash
pytest -k "compress"    # Runs all tests with "compress" in the name
pytest -k "landscape"   # Runs all tests with "landscape" in the name
```

### Using the Convenience Script

**Simple run:**
```bash
./run_tests.sh
```

**With coverage:**
```bash
./run_tests.sh --coverage
```

**Fast mode (no coverage):**
```bash
./run_tests.sh --fast
```

### View Coverage Report

After running with coverage, open the HTML report:
```bash
# macOS
open htmlcov/index.html

# Linux
xdg-open htmlcov/index.html

# Windows
start htmlcov/index.html
```

## Test Results

When you run the tests, you should see:
- ✅ All 45 tests passing
- Test execution time
- Coverage percentages (if using --cov)

## Common Issues

**Issue: "pytest: command not found"**
- Solution: Make sure the virtual environment is activated

**Issue: Import errors**
- Solution: Ensure you're running from the project root directory

**Issue: Permission denied on run_tests.sh**
- Solution: `chmod +x run_tests.sh`

## Next Steps

- Write new tests when adding features
- Aim for >80% code coverage
- Run tests before committing changes

