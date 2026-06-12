import os

inputs = print(input("Path:"))

def format_size(size_bytes):
    """Converts bytes to a human-readable string format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} PB"

def get_directory_sizes(inputs):
    """
    Recursively maps directory and subdirectory sizes.
    Returns a dictionary of {path: total_size_in_bytes}
    """
    dir_sizes = {}
    
    # Bottom-up processing allows subfolder sizes to bubble up correctly
    for inputs, dirs, files in os.walk(inputs, topdown=False):
        current_dir_size = 0
        
        # Add sizes of immediate files in the current folder
        for file in files:
            file_path = os.path.join(inputs, file)
            try:
                # Use st_size to read file metadata directly
                current_dir_size += os.path.getsize(file_path)
            except (OSError, PermissionError):
                # Ignore system files or protected items lacking read permission
                continue
                
        # Add sizes of immediate subdirectories
        for sub_dir in dirs:
            sub_dir_path = os.path.join(inputs, sub_dir)
            current_dir_size += dir_sizes.get(sub_dir_path, 0)
            
        dir_sizes[inputs] = current_dir_size
        
    return dir_sizes

def print_analyzer_tree(inputs):
    """Generates and displays the size analysis report."""
    if not os.path.exists(inputs):
        print("Error: The specified target path does not exist.")
        return

    print(f"Analyzing: {os.path.abspath(inputs)}\n" + "="*50)
    all_sizes = get_directory_sizes(inputs)
    
    # Sort top-down to display structural output accurately
    for path in sorted(all_sizes.keys()):
        # Calculate indentation levels based on folder depth
        depth = path.replace(inputs, "").count(os.sep)
        indent = "  " * depth
        folder_name = os.path.basename(path) or path
        
        readable_size = format_size(all_sizes[path])
        print(f"{indent}📁 {folder_name} ({readable_size})")
        
        # Optional: Print files residing directly inside this folder
        try:
            with os.scandir(path) as entries:
                for entry in entries:
                    if entry.is_file(follow_symlinks=False):
                        file_size = format_size(entry.stat().st_size)
                        print(f"{indent}  📄 {entry.name} ({file_size})")
        except PermissionError:
            continue

# Example Execution
if __name__ == "__main__":
    # Replace with your target directory path
 target_folder = "." 
print_analyzer_tree(target_folder)