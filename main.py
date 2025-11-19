# Import necessary modules
import os # Provides functions for interacting with the operating system, like file paths and directory listing
import shutil # Provides high-level file operations, like moving files
import argparse # Provides utilities for parsing command-line arguments

# Massive extension database
# Dictionary mapping file categories (keys) to lists of corresponding file extensions (values)
FILE_TYPES = {
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif", ".svg", ".webp",
        ".psd", ".raw", ".ico", ".heif", ".heic"
    ],
    "Videos": [
        ".mp4", ".mkv", ".mov", ".avi", ".wmv", ".flv", ".webm", ".mpeg",
        ".mpg", ".m4v", ".3gp", ".ts"
    ],
    "Audio": [
        ".mp3", ".wav", ".aac", ".m4a", ".flac", ".ogg", ".oga", ".aiff",
        ".alac", ".wma", ".mid", ".midi"
    ],
    "Documents": [
        ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt",
        ".rtf", ".odt", ".ods", ".odp", ".md", ".csv", ".epub"
    ],
    "Archives": [
        ".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".iso"
    ],
    "Code": [
        ".py", ".java", ".js", ".jsx", ".ts", ".tsx", ".c", ".cpp", ".h",
        ".hpp", ".cs", ".php", ".rb", ".go", ".rs", ".swift", ".kt",
        ".sh", ".bat", ".ps1", ".sql", ".html", ".css", ".xml", ".json",
        ".yaml", ".yml", ".ini", ".toml"
    ],
    "Executables": [
        ".exe", ".msi", ".apk", ".app", ".deb", ".rpm", ".bin", ".run"
    ],
    "Fonts": [
        ".ttf", ".otf", ".woff", ".woff2", ".fon"
    ],
    "3D_Models": [
        ".obj", ".fbx", ".blend", ".stl", ".dae", ".gltf", ".glb"
    ],
    # Note: ".xls", ".xlsx", ".ods", ".csv" are also in Documents, which is fine
    "Spreadsheets": [
        ".xls", ".xlsx", ".ods", ".csv"
    ],
    "Databases": [
        ".db", ".sqlite", ".sqlite3", ".mdb", ".accdb"
    ],
    "Design": [
        ".ai", ".eps", ".indd", ".xd", ".sketch"
    ],
    "Torrents": [
        ".torrent"
    ]
}

# --- Helper Function ---

def ensure_folder(path):
    # Check if the directory path exists
    if not os.path.exists(path):
        # If it doesn't exist, create it (including any necessary parent directories)
        os.makedirs(path)

# --- Core Logic ---

def sort_files(source, destination):
    # Iterate through every file and directory in the source folder
    for item in os.listdir(source):
        # Create the full path to the current item
        src_path = os.path.join(source, item)

        # Skip if the item is a directory (we only want to sort files)
        if os.path.isdir(src_path):
            continue

        # Get the file extension (e.g., '.jpg') and the base name (e.g., 'photo')
        _, ext = os.path.splitext(item)
        # Convert the extension to lowercase for case-insensitive matching
        ext = ext.lower()

        # Flag to track if the file was moved to a category folder
        moved = False
        # Loop through each category and its list of extensions
        for category, ext_list in FILE_TYPES.items():
            # Check if the file's extension is in the current category's list
            if ext in ext_list:
                # Construct the full path for the target category folder
                target_folder = os.path.join(destination, category)
                
                # Ensure the category folder exists
                ensure_folder(target_folder)
                
                # Move the file from the source to the target category folder
                shutil.move(src_path, os.path.join(target_folder, item))
                
                # Print confirmation of the move
                print(f"[Moved] {item} → {category}")
                
                # Set the flag and break out of the category loop, as the file has been sorted
                moved = True
                break

        # If the file wasn't moved (i.e., its extension wasn't found in FILE_TYPES)
        if not moved:
            # Define the 'Misc' folder path
            misc_folder = os.path.join(destination, "Misc")
            
            # Ensure the 'Misc' folder exists
            ensure_folder(misc_folder)
            
            # Move the file to the 'Misc' folder
            shutil.move(src_path, os.path.join(misc_folder, item))
            
            # Print confirmation of the misc move
            print(f"[Misc] {item}")

# --- Main Execution Block ---

def main():
    # Initialize the argument parser with a description
    parser = argparse.ArgumentParser(description="Sort files into category folders.")
    
    # Add 'source' argument: required, positionally first, provides the folder to sort
    parser.add_argument("source", help="Folder to sort")
    
    # Add 'destination' argument: optional, positionally second, defaults to source if not provided
    parser.add_argument(
        "destination",
        nargs="?", # '?' means 0 or 1 argument is expected
        help="Optional destination root (defaults to source)",
        default=None
    )

    # Parse the arguments provided by the user
    args = parser.parse_args()

    # Get the absolute path for the source folder
    source = os.path.abspath(args.source)
    
    # Determine the destination: use the provided destination or the source if none was given
    destination = os.path.abspath(args.destination or source)

    # Check if the source folder actually exists
    if not os.path.isdir(source):
        print("Error: Source folder does not exist.")
        return # Exit if the source is invalid

    # Call the core sorting function
    sort_files(source, destination)
    
    # Print final status
    print("\nSorting complete!")

# Standard Python entry point: run main() when the script is executed directly
if __name__ == "__main__":
    main()
