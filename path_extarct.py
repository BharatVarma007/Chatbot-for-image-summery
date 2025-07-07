import os

def append_file_paths_to_list(folder_path):
    # Initialize an empty list to store file paths
    file_paths = []

    # Ensure the folder path is valid
    if not os.path.isdir(folder_path):
        print(f"The folder path {folder_path} does not exist or is not a directory.")
        return file_paths

    # Walk through the folder and its subfolders
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_paths.append(file_path)
            print(f"Appended: {file_path}")

    return file_paths

if __name__ == "__main__":
    folder_path = input("Enter the path to the folder: ")

    file_paths_list = append_file_paths_to_list(folder_path)

    print("\nAll file paths:")
    for path in file_paths_list:
        print(path)