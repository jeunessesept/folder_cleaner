# File Organizer for Downloads Folder

This Python script organizes files in your Downloads folder into designated subfolders based on their file extensions. The script automatically categorizes files, creates necessary folders, and handles filename conflicts by incrementing the filenames if a file with the same name already exists in the destination folder.

## Features

- **Automatic Folder Creation:** The script creates folders for different file types if they don't already exist.
- **File Type Categorization:** Files are moved to specific folders based on their extensions.
- **Filename Conflict Handling:** If a file with the same name already exists in the destination folder, the script increments the filename (e.g., `file_1.txt`, `file_2.txt`) to avoid overwriting.

## File Type Mappings

The following table maps file extensions to the corresponding folders:

| Extension | Folder Name        |
|-----------|--------------------|
| `.pdf`    | PDFFolder           |
| `.xlsx`   | ExcelFolder         |
| `.xls`    | ExcelFolder         |
| `.jpg`    | JpgFolder           |
| `.jpeg`   | JpgFolder           |
| `.png`    | PngFolder           |
| `.pptx`   | PowerPointFolder    |
| `.txt`    | TextFolder          |
| `.csv`    | CsvFolder           |
| `.docx`   | TextFolder          |
| `.doc`    | TextFolder          |
| `.wav`    | SoundFolder         |
| `.odt`    | TextFolder          |
| `.mkv`    | MovieFolder         |
| `.heic`   | PhonePhoto          |
| `.ogg`    | SoundFolder         |
| `.zip`    | ZipFolder           |
| `.mjs`    | CodeFolder          |
| `.sql`    | CodeFolder          |
| `.dmg`    | ProgramFolder       |

## How to Use

1. **Ensure Python is Installed:** Make sure you have Python installed on your machine.

2. **Clone or Download the Script:**
   - Clone the repository:
     ```bash
     git clone https://github.com/yourusername/folder_cleaner.git
     ```
   - Or download the `organize_downloads.py` script directly.

3. **Run the Script:**
   - Navigate to the directory where the script is located.
   - Run the script using Python:
     ```bash
     python cleaner.py
     ```

4. **Files are Organized:** After running the script, your files in the Downloads folder will be organized into their respective folders.

## Customization

- **Adding New File Types:** To add support for additional file types, modify the `file_type_folders` dictionary in the script.
- **Changing Folder Names:** You can change the folder names by updating the values in the `file_type_folders` dictionary.

## Example Output

After running the script, your Downloads folder might look something like this:

Downloads/
│
├── PDFFolder/
│ └── document.pdf
├── ExcelFolder/
│ ├── spreadsheet.xlsx
│ └── report.xls
├── JpgFolder/
│ ├── image.jpg
│ └── photo.jpeg
├── PngFolder/
│ └── graphic.png
├── PowerPointFolder/
│ └── presentation.pptx
├── TextFolder/
│ ├── notes.txt
│ ├── essay.docx
│ └── draft.doc
├── CsvFolder/
│ └── data.csv
├── SoundFolder/
│ ├── song.wav
│ └── audio.ogg
├── MovieFolder/
│ └── movie.mkv
└── Other/
├── file.mjs
└── software.dmg