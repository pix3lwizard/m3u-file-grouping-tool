# M3U File Grouping Tool

This Python application allows you to group related `.cue`, `.chd`, `.iso`, and `.img` files based on their names (e.g., `disk 1`, `side A`, etc.) into a single `.m3u` playlist file. 

## Features
- Searches for multi-part files like `disk 1`, `disk 2`, `side A`, `side B` and creates `.m3u` files for each set.
- Supports `.cue`, `.chd`, `.iso`, and `.img` file extensions.
- Easy-to-use graphical interface to select directories for processing.

## Setup Instructions

### Prerequisites

You will need Python installed on your system.

- [Python Download](https://www.python.org/downloads/)

Make sure you have Python 3.6 or higher.

### Install Dependencies

There are no additional dependencies beyond standard Python libraries.

To install dependencies:

```bash
pip install -r requirements.txt
```

### How to Run

1. **Clone the repository:**

```bash
git clone https://github.com/pix3lwizard/m3u-file-grouping-tool.git
cd m3u-file-grouping-tool
```

2. **Run the script:**

- **Windows:**

    Double-click `group_files_gui.py` or run the following command from a terminal:

    ```bash
    python group_files_gui.py
    ```

- **macOS and Linux:**

    Run the following command from a terminal:

    ```bash
    python3 group_files_gui.py
    ```

This will launch the GUI where you can select a directory to process.

## Platform-Specific Instructions

### Windows

1. Make sure Python is installed and added to the PATH.
2. Install `tkinter` if it's not included with your Python installation.
3. Open a terminal or use the command prompt and navigate to the folder containing the script.
4. Run the script by double-clicking `group_files_gui.py` or using the command:
   ```bash
   python group_files_gui.py
   ```

### macOS

1. Python 3 usually comes pre-installed, but ensure that the `tkinter` package is included.
2. Open a terminal, navigate to the project folder, and run:
   ```bash
   python3 group_files_gui.py
   ```

### Linux

1. Ensure Python 3 is installed along with the `tkinter` library.
   
   - On **Ubuntu** or **Debian**, you can install `tkinter` with:
     ```bash
     sudo apt-get install python3-tk
     ```

2. Run the script from a terminal:
   ```bash
   python3 group_files_gui.py
   ```

## License

This project is licensed under the MIT License.
