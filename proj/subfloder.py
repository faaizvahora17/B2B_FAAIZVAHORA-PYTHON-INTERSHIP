import os
import matplotlib.pyplot as plt

def format_size(size_bytes):
    """Convert bytes to a human-readable format."""
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    size = float(size_bytes)

    for unit in units:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

    return f"{size:.2f} PB"


def get_folder_size(folder_path):
    """Recursively calculate folder size."""
    total_size = 0

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)

            try:
                total_size += os.path.getsize(file_path)
            except (PermissionError, FileNotFoundError):
                continue

    return total_size


def analyze_folder(folder_path):
    print(f"\nAnalyzing: {folder_path}\n")

    total_folder_size = get_folder_size(folder_path)

    print("=" * 60)
    print(f"Total Folder Size: {format_size(total_folder_size)}")
    print("=" * 60)

    print("\nSubfolder Sizes:\n")

try:
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            size = get_folder_size(item_path)
            print(f"[DIR ] {item:<40} {format_size(size)}")

        elif os.path.isfile(item_path):
            size = os.path.getsize(item_path)
            print(f"[FILE] {item:<40} {format_size(size)}")

except PermissionError:
        print("Permission denied.")


if __name__ == "__main__":
    folder = input("Enter folder path: ").strip()

    if os.path.exists(folder):
        analyze_folder(folder)
    else:
        print("Folder does not exist.")