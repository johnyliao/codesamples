import os
#from pypdf import PdfMerger
from pypdf import PdfWriter


def combine_pdfs_from_directory(directory_path, output_filename="combined_output.pdf"):
    merger = PdfWriter()
    
    # Resolve relative paths (like "." or "..") into absolute system paths
    target_dir = os.path.abspath(directory_path)
    
    if not os.path.exists(target_dir):
        print(f"Error: The directory '{target_dir}' does not exist.")
        return

    # 1. Collect and sort all matching PDF files inside the specified folder
    pdf_files = [f for f in os.listdir(target_dir) if f.lower().endswith('.pdf') and f != output_filename]
    pdf_files.sort()  # Ensures sequential order (01, 02, 03...)
    
    if not pdf_files:
        print(f"No PDF files found to merge in: '{target_dir}'")
        return

    print(f"Found {len(pdf_files)} files in '{target_dir}' to combine.")

    # 2. Loop through each file and append it with a bookmark
    for file_name in pdf_files:
        # Construct the full path to locate the file inside its folder
        full_file_path = os.path.join(target_dir, file_name)
        
        # Strip the ".pdf" extension to create the bookmark name (e.g., "01-title1")
        bookmark_name = os.path.splitext(file_name)[0]
        
        print(f"Appending: {file_name} -> Bookmark: {bookmark_name}")
        
        # Open and append the file
        merger.append(full_file_path, outline_item=bookmark_name)
    
    # 3. Write out the final combined file to the target directory
    final_output_path = os.path.join(target_dir, output_filename)
    merger.write(final_output_path)
    merger.close()
    print(f"\nSuccess! Merged file saved at: '{final_output_path}'")

if __name__ == "__main__":
    # --- CHANGE THIS TO YOUR FOLDER PATH ---
    # Examples:
    # Windows: r"C:\Users\YourName\Documents\PDF_Folder"
    # Mac/Linux: "/Users/YourName/Documents/PDF_Folder"
    # Relative path: "./my_pdfs"
    my_folder = ""
    
    combine_pdfs_from_directory(my_folder)
