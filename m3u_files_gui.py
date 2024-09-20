import os
import re
import tkinter as tk
from tkinter import filedialog, messagebox

# Define the file extensions to search for
FILE_EXTENSIONS = ['.cue', '.chd', '.iso', '.img']

# Pattern to identify files with "disk" or "side" naming conventions
SET_PATTERN = re.compile(r'.*(disk|side).*[1-9A-Z]', re.IGNORECASE)

def create_m3u_file(directory, file_set):
    """Create an .m3u file based on the group of related files."""
    if not file_set:
        return

    # Use the base name of the first file to create the .m3u file
    base_name = os.path.basename(file_set[0])
    # Remove the "(disk 1)", "(side A)", etc. part from the name
    common_name = re.sub(r'(\s*\(.*[1-9A-Z]\))', '', base_name, flags=re.IGNORECASE)
    m3u_filename = os.path.join(directory, f"{common_name}.m3u")

    # Write the related files into the .m3u file
    with open(m3u_filename, 'w') as m3u_file:
        for file in file_set:
            m3u_file.write(f"{os.path.basename(file)}\n")
    print(f"M3U file created: {m3u_filename}")

def process_directory(directory):
    """Search for files in the directory and create .m3u files for related sets."""
    if not os.path.isdir(directory):
        print(f"Invalid directory: {directory}")
        return

    # Store files by base name (without "disk 1" or "side A")
    files_grouped = {}

    # Walk through the directory and all subdirectories
    for root, _, files in os.walk(directory):
        for file in files:
            # Check if the file has one of the desired extensions
            if any(file.lower().endswith(ext) for ext in FILE_EXTENSIONS):
                # Check if the file matches the pattern (disk/side + number)
                if SET_PATTERN.search(file):
                    # Get the common base name
                    base_name = re.sub(r'(\s*\(.*[1-9A-Z]\))', '', file, flags=re.IGNORECASE)
                    base_path = os.path.join(root, base_name)

                    # Group related files
                    if base_path not in files_grouped:
                        files_grouped[base_path] = []
                    files_grouped[base_path].append(os.path.join(root, file))

    # Create an .m3u file for each set of related files
    for base_path, file_set in files_grouped.items():
        create_m3u_file(os.path.dirname(base_path), file_set)

def select_directory():
    """Open a dialog to select a directory and process the files."""
    directory = filedialog.askdirectory()
    if directory:
        process_directory(directory)
        messagebox.showinfo("Success", "M3U files created successfully.")
    else:
        messagebox.showwarning("Warning", "No directory selected.")

# Set up the GUI
def create_gui():
    root = tk.Tk()
    root.title("Group Files into M3U")
    root.geometry("400x200")

    # Label
    label = tk.Label(root, text="Select a directory to search for .cue, .chd, .iso, .img files:")
    label.pack(pady=20)

    # Button to select directory
    select_btn = tk.Button(root, text="Select Directory", command=select_directory)
    select_btn.pack(pady=10)

    # Run the GUI
    root.mainloop()

if __name__ == "__main__":
    create_gui()
