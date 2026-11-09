import os

def replace_pdf_suffix(directory_path, old_suffix="-constant-label", new_suffix="-newlabel"):
    """
    Renames PDF files in a directory by replacing an old suffix with a new label.
    Example: '01-title1-constant-label.pdf' -> '01-title1-newlabel.pdf'
    """
    if not os.path.exists(directory_path):
        print(f"Error: The directory '{directory_path}' does not exist.")
        return

    renamed_count = 0

    for filename in os.listdir(directory_path):
        # Target only .pdf files containing the old suffix
        if filename.endswith(".pdf") and old_suffix in filename:
            # Replace the old suffix + extension with the new suffix + extension
            new_filename = filename.replace(f"{old_suffix}.pdf", f"{new_suffix}.pdf")
            
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
target_directory = "your_directory_here"
replace_pdf_suffix(target_directory, old_suffix="-constant-label", new_suffix="-newlabel")
