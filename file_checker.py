import os
from config import CATEGORIES, SOURCE_DIR

def get_extension(file_name):
    return os.path.splitext(file_name)[1].lower()

def find_unsorted_files():
    unsorted_files = []
    for file in os.listdir(SOURCE_DIR):
        if os.path.isdir(os.path.join(SOURCE_DIR, file)):  
            continue  # Skip directories
        
        ext = get_extension(file)
        is_sorted = any(ext in exts for category in CATEGORIES.values() for exts in category.values())

        if not is_sorted:  # If the file doesn't belong to any category, mark it as unsorted
            unsorted_files.append(file)

    return unsorted_files

