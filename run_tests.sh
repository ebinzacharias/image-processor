#!/bin/bash
# Convenience script to run tests with various options

set -e

echo "Running Image Processing Tests..."
echo ""

# Check if pytest is installed
if ! python3 -m pytest --version &> /dev/null; then
    echo "Error: pytest is not installed. Please run: pip install -r requirements.txt"
    exit 1
fi

# Parse command line arguments
if [ "$1" == "--coverage" ] || [ "$1" == "-c" ]; then
    echo "Running tests with coverage report..."
    python3 -m pytest --cov=. --cov-report=html --cov-report=term-missing -v
    echo ""
    echo "Coverage report generated in htmlcov/index.html"
elif [ "$1" == "--fast" ] || [ "$1" == "-f" ]; then
    echo "Running tests (fast mode)..."
    python3 -m pytest -v
elif [ "$1" == "--help" ] || [ "$1" == "-h" ]; then
    echo "Usage: ./run_tests.sh [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  --coverage, -c    Run tests with coverage report"
    echo "  --fast, -f        Run tests in fast mode (no coverage)"
    echo "  --help, -h        Show this help message"
    echo ""
    echo "Without options, runs all tests with verbose output."
else
    echo "Running all tests..."
    python3 -m pytest -v
fi

