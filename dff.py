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

# Example usage:
file_path = "/mnt/e/badanie.vhd"
print(get_file_sha1(file_path))
