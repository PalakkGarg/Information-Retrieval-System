import os
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# List of files and their respective paths
list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "app.py",
    "research/trials.ipynb",
]

# Iterate through each file
for filepath in list_of_files:
    filepath = Path(filepath)  # Use Path to handle cross-platform paths
    filedir = filepath.parent  # Get the directory
    filename = filepath.name   # Get the filename

    # Create directory if it doesn't exist
    if not filedir.exists() and filedir != Path():
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Create file if it doesn't exist or is empty
    if not filepath.exists() or filepath.stat().st_size == 0:
        filepath.touch()  # Create an empty file
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
