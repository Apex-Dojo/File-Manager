import os

def list_files(directory):
    """List all files in the specified directory."""
    try:
        files = os.listdir(directory)
        print(f"Files in {directory}:")
        for file in files:
            print(file)
    except FileNotFoundError:
        print(f"Directory {directory} not found.")
    except PermissionError:
        print(f"Permission denied to access {directory}.")

def create_file(file_path):
    """Create a new file at the specified path."""
    try:
        with open(file_path, 'w') as file:
            file.write("This is a simple file created by the Python script.")
        print(f"File {file_path} created successfully.")
    except PermissionError:
        print(f"Permission denied to create file at {file_path}.")

def delete_file(file_path):
    """Delete the specified file."""
    try:
        os.remove(file_path)
        print(f"File {file_path} deleted successfully.")
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except PermissionError:
        print(f"Permission denied to delete {file_path}.")

def main():
    directory = input("Enter the directory path: ")
    
    print("\nOptions:")
    print("1. List files")
    print("2. Create file")
    print("3. Delete file")
    choice = input("Choose an option (1/2/3): ")

    if choice == '1':
        list_files(directory)
    elif choice == '2':
        file_name = input("Enter the file name to create: ")
        create_file(os.path.join(directory, file_name))
    elif choice == '3':
        file_name = input("Enter the file name to delete: ")
        delete_file(os.path.join(directory, file_name))
    else:
        print("Invalid choice, please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
