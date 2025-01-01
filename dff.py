import os
import hashlib
from collections import defaultdict

def get_file_sha1(file_path):
    sha1 = hashlib.sha1()
    try:
        with open(file_path, 'rb') as file:
            while chunk := file.read(8192):
                sha1.update(chunk)
        return sha1.hexdigest()
    except FileNotFoundError:
        return None

def traverse_and_store(root_dir):
    file_info = defaultdict(list)
    for root, _, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_size = os.path.getsize(file_path)
                file_sha1 = get_file_sha1(file_path)
                if file_sha1:
                    file_info[(file_size, file_sha1)].append(file_path)
            except (FileNotFoundError, PermissionError):
                continue
    return file_info

def find_and_display_duplicates(file_info):
    duplicates = {key: paths for key, paths in file_info.items() if len(paths) > 1}
    for key, paths in duplicates.items():
        print(f"Duplicate files (Size: {key[0]} bytes, SHA-1: {key[1]}):")
        for path in paths:
            print(f" - {path}")

def main(root_dir):
    file_info = traverse_and_store(root_dir)
    find_and_display_duplicates(file_info)

# Example usage:
root_directory = "/mnt/e/backup/"
main(root_directory)