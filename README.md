# FileSorterX

**FileSorterX** is a powerful and flexible file organization utility written in Python. It automatically sorts files from a source directory into categorized folders (like Images, Videos, Documents, Archives, and many more) based on their extension. 

> **Key Features:**
> - **Massive Extension Database**: Handles a wide variety of file types out-of-the-box.
> - **Configurable Destination**: Specify a root output directory, or sort files in-place.
> - **Miscellaneous Catch-All**: Unsupported or unknown extensions are placed into a `Misc` folder.
> - **Cross-Platform**: Works on any system with Python 3.x.

---

## Table of Contents

- [Features](#features)
- [How it Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [File Categories](#file-categories)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Automatic Folder Creation**
- **Case-Insensitive Extension Matching**
- **No Third-Party Dependencies (Uses Only the Python Standard Library)**
- **CLI with Intuitive Arguments**

---

## How it Works

FileSorterX leverages a built-in mapping between file categories and extensions. When run, it examines each file in the source directory:

1. If a file matches a known extension, it's moved into a corresponding category folder (e.g., `Images`, `Videos`, `Documents`).
2. Unrecognized file types are placed in a `Misc` folder.
3. Destination directories are created on-the-fly if they don't exist.

---

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/LunexCorp/FileSorterX.git
   cd FileSorterX
   ```

2. **(Optional) Create a Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **No additional installation is required!**

---

## Usage

Run the script from the command line:

```bash
python3 filesorterx.py <source> [destination]
```

- `<source>`: **(Required)** Path to the folder containing files to sort.
- `[destination]`: *(Optional)* Root output folder for sorted files. If omitted, files are sorted inside the `<source>` folder.

**Examples:**

Sort files in the "Downloads" folder and organize them in-place:

```bash
python3 filesorterx.py ~/Downloads
```

Sort files from "Incoming" into "SortedFiles":

```bash
python3 filesorterx.py ~/Incoming ~/SortedFiles
```

---

## File Categories

FileSorterX recognizes the following categories (with example extensions):

| Category      | Example Extensions                               |
|---------------|--------------------------------------------------|
| Images        | `.jpg`, `.png`, `.tiff`, `.svg`                  |
| Videos        | `.mp4`, `.mkv`, `.mov`, `.webm`                  |
| Audio         | `.mp3`, `.wav`, `.flac`, `.aac`                  |
| Documents     | `.pdf`, `.docx`, `.pptx`, `.txt`, `.epub`        |
| Archives      | `.zip`, `.rar`, `.7z`, `.tar.gz`, `.iso`         |
| Code          | `.py`, `.js`, `.ts`, `.cpp`, `.rb`, `.php`       |
| Executables   | `.exe`, `.msi`, `.apk`, `.deb`                   |
| Fonts         | `.ttf`, `.otf`, `.woff`, `.woff2`                |
| 3D_Models     | `.obj`, `.fbx`, `.stl`, `.gltf`                  |
| Spreadsheets  | `.xls`, `.csv`, `.ods`, `.xlsx`                  |
| Databases     | `.db`, `.sqlite`, `.accdb`                       |
| Design        | `.ai`, `.eps`, `.xd`, `.sketch`                  |
| Torrents      | `.torrent`                                       |
| Misc          | _(All other/unknown extensions)_                  |

*See the source code (`filesorterx.py`) for a full list of supported extensions.*

---

## Example

Suppose your directory contains:

```
flower.jpg
presentation.pptx
video.mp4
archive.zip
notes.txt
script.py
song.flac
unknownfile.xyz
```

Running:

```bash
python3 filesorterx.py .
```

Will create folders such as `Images`, `Documents`, `Videos`, `Archives`, `Audio`, `Code`, `Misc`, etc., and move each file accordingly.

---

## Contributing

Contributions to FileSorterX are welcome! Suggestions, improvements, and bug reports are encouraged. Please open an issue or submit a pull request.

---
