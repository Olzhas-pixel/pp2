import os
import shutil
import string

def list_items(path):
    """Lists directories, files, and both in a specified path"""
    if not os.path.exists(path):
        print("Path does not exist.")
        return
    
    print("Directories:", [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
    print("Files:", [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
    print("All items:", os.listdir(path))

def check_access(path):
    """Checks for access: existence, readability, writability, executability"""
    print("Exists:", os.path.exists(path))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))

def path_info(path):
    """Tests whether a path exists and gets its directory and filename"""
    if os.path.exists(path):
        print("Path exists.")
        print("Directory:", os.path.dirname(path))
        print("Filename:", os.path.basename(path))
    else:
        print("Path does not exist.")

def count_lines(file_path):
    """Counts the number of lines in a text file"""
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            print("Number of lines:", sum(1 for line in file))
    else:
        print("File does not exist.")

def write_list_to_file(file_path, data_list):
    """Writes a list to a file"""
    with open(file_path, 'w', encoding='utf-8') as file:
        for item in data_list:
            file.write(f"{item}\n")
    print("List written to file.")

def generate_text_files():
    """Generates 26 text files named A.txt to Z.txt"""
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", 'w', encoding='utf-8') as file:
            file.write(f"This is {letter}.txt\n")
    print("26 text files created.")

def copy_file(source, destination):
    """Copies contents of a file to another file"""
    if os.path.exists(source):
        shutil.copy(source, destination)
        print("File copied successfully.")
    else:
        print("Source file does not exist.")

def delete_file(file_path):
    """Deletes a file after checking for existence and access"""
    if os.path.exists(file_path):
        if os.access(file_path, os.W_OK):
            os.remove(file_path)
            print("File deleted successfully.")
        else:
            print("No write permission to delete the file.")
    else:
        print("File does not exist.")

