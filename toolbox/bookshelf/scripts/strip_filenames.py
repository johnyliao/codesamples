import os
import re

def strip_pdf_suffix(directory_path, suffix_to_remove="-constant-label"):
    """
    Renames PDF files in a directory by removing a specific suffix from their names.
    Example: '01-title1-constant-label.pdf' -> '01-title1.pdf'
    """
    # Ensure the directory path exists
    if not os.path.exists(directory_path):
        print(f"Error: The directory '{directory_path}' does not exist.")
        return

    # Counter for renamed files
    renamed_count = 0

    # List all files in the directory
    for filename in os.listdir(directory_path):
        # Target only .pdf files that contain the suffix before the extension
        if filename.endswith(".pdf") and suffix_to_remove in filename:
            # Construct the new filename by replacing the suffix with an empty string
            new_filename = filename.replace(f"{suffix_to_remove}.pdf", ".pdf")
            
            # Full paths for renaming
            old_file_path = os.path.join(directory_path, filename)
            new_file_path = os.path.join(directory_path, new_filename)
            
            try:
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: '{filename}' -> '{new_filename}'")
                renamed_count += 1
            except Exception as e:
                print(f"Error renaming '{filename}': {e}")

    print(f"\nTask completed. Total files renamed: {renamed_count}")

# --- Example Usage ---
# Replace 'your_directory_here' with the actual path to your folder
# Example: r"C:\Users\Name\Documents\PDFs" or "/Users/Name/Documents/PDFs"
replaceable_label=""
target_directory = ""

strip_pdf_suffix(target_directory, replaceable_label)
