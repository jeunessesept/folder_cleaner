import shutil
import os

# Define the path to the Downloads directory

downloads_directory = os.path.join(os.path.expanduser('~'), 'Downloads')

# Define a dictionary to map file extensions to folder names

file_type_folders = {
    '.pdf': 'PDFFolder',
    '.xlsx': 'ExcelFolder',
    '.xls': 'ExcelFolder',
    '.jpg': 'JpgFolder',
    '.jpeg': 'JpgFolder',
    '.png': 'PngFolder',
    '.pptx': 'PowerPointFolder',
    '.txt': 'TextFolder',
    '.csv': 'CsvFolder',
    '.docx': 'TextFolder',
    '.doc': 'TextFolder',
    '.wav': "SoundFolder",
    '.odt': 'TextFolder',
    '.mkv': 'MovieFolder',
    '.heic': 'PhonePhoto',
    '.ogg': 'SoundFolder',
    '.zip': 'ZipFolder',
    '.mjs': 'CodeFolder',
    '.sql': 'CodeFolder',
    '.dmg': 'ProgramFolder'
 
}

# Create the folders if they do not exist
for folder in file_type_folders.values():
    folder_path = os.path.join(downloads_directory, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


# Function to increment file name if it already exists

def increment_filename(filename, destination_folder):
    base_name, extension = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(os.path.join(destination_folder, new_filename)):
        new_filename = f'{base_name}_{counter}{extension}'
        counter +=1
    return new_filename

    
# Move files to their corresponding folders

for filename in os.listdir(downloads_directory):
    file_path = os.path.join(downloads_directory, filename)
    if os.path.isfile(file_path):
        file_extension = os.path.splitext(filename)[1].lower()
        if file_extension in file_type_folders:
            destination_folder = os.path.join(downloads_directory, file_type_folders[file_extension])
            # Check if file exists and increment name if necessary
            new_filename = increment_filename(filename, destination_folder)
            new_file_path = os.path.join(destination_folder, new_filename)

            shutil.move(file_path, new_file_path)

print("Files have been organized in the Downloads folder.")