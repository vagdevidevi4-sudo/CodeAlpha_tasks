import os
import shutil

def move_jpg_files(source_folder, destination_folder):
    # Create destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"Created folder: {destination_folder}")

    # Counter to track moved files
    moved_count = 0

    # Loop through all files in the source folder
    for file_name in os.listdir(source_folder):
        # Check if the file has a .jpg extension (case-insensitive)
        if file_name.lower().endswith(".jpg"):
            source_path = os.path.join(source_folder, file_name)
            destination_path = os.path.join(destination_folder, file_name)

            # Move the file
            shutil.move(source_path, destination_path)
            print(f"Moved: {file_name}")
            moved_count += 1

    if moved_count == 0:
        print("No .jpg files found in the source folder.")
    else:
        print(f"\nTotal .jpg files moved: {moved_count}")


# ------------------- Main Program -------------------
if __name__ == "__main__":
    source = input("Enter the source folder path: ")
    destination = input("Enter the destination folder path: ")

    move_jpg_files(source, destination)