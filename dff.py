import os
import hashlib

def get_file_sha1(file_path):
    sha1 = hashlib.sha1()
    try:
        with open(file_path, 'rb') as file:
            while chunk := file.read(8192):
                sha1.update(chunk)
        return sha1.hexdigest()
    except FileNotFoundError:
        return f"File {file_path} not found."

def traverse_directory(root_dir):
    for root, _, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(root, file)
            file_sha1 = get_file_sha1(file_path)
            print(f"{file_path} -> {file_sha1}")

# Example usage:
root_directory = "/mnt/e/Brabork"
traverse_directory(root_directory)