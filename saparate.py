import os
import shutil

# Paths (CHANGE THESE)
source_folder = r"C:\Users\Sakib Mahmud\Downloads\gencsv\pdfs"
destination_folder = r"C:\Users\Sakib Mahmud\Downloads\gencsv\pdfs_separated"
list_file = r"C:\Users\Sakib Mahmud\Downloads\gencsv\list.txt"   # File containing PDF numbers

# Create destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Read list of PDF numbers
with open(list_file, "r") as file:
    pdf_numbers = [line.strip() for line in file.readlines() if line.strip()]

# Loop through numbers and copy matching PDFs
for number in pdf_numbers:
    pdf_name = f"{number}.pdf"  # final filename format
    source_path = os.path.join(source_folder, pdf_name)
    destination_path = os.path.join(destination_folder, pdf_name)

    if os.path.exists(source_path):
        shutil.copy2(source_path, destination_path)
        print(f"Copied: {pdf_name}")
    else:
        print(f"NOT FOUND: {pdf_name}")
