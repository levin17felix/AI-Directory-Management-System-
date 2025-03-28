import os
import shutil
import time
from config import CATEGORIES, SOURCE_DIR 
from file_checker import find_unsorted_files



def get_extension(filename):
    return os.path.splitext(filename)[1].lower()

def move_file(filename):
    """Move file to the correct category and subcategory based on its extension."""
    ext = get_extension(filename)
    for category, subcategories in CATEGORIES.items():
        for subcategory, extensions in subcategories.items():
            if ext in extensions:
                dest_folder = os.path.join(SOURCE_DIR, category, subcategory)
                os.makedirs(dest_folder, exist_ok=True)  # Ensure folder exists
                src_path = os.path.join(SOURCE_DIR, filename)
                dest_path = os.path.join(dest_folder, filename)

                if os.path.exists(src_path):  # Ensure file still exists
                    shutil.move(src_path, dest_path)
                    print(f"Moved {filename} to {dest_folder}/")
                    return True
    return False

def monitor_directory():
    """Monitor directory and sort new files."""
    print(f"Monitoring {SOURCE_DIR} for changes...")
    while True:
        files = [f for f in os.listdir(SOURCE_DIR) if os.path.isfile(os.path.join(SOURCE_DIR, f))]
        for file in files:
            move_file(file)
        time.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
    # Initial sorting
    print("🔄 Sorting existing files...")
    files = [f for f in os.listdir(SOURCE_DIR) if os.path.isfile(os.path.join(SOURCE_DIR, f))]
    for file in files:
        move_file(file)

    # Check for unsorted files
    unsorted_files = find_unsorted_files()
    if unsorted_files:
        print("\n⚠️ The following files were NOT sorted:")
        for file in unsorted_files:
            print(f"❌ {file}")
    else:
        print("\n✅ All files were successfully sorted.")

    # Start monitoring directory for new files
    monitor_directory()
