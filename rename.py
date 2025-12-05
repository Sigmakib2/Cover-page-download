import os

folder_path = r"C:\Users\Sakib Mahmud\Downloads\gencsv\pdfs"   # <-- change this

for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):
        # Split at the first underscore
        parts = filename.split("_", 1)

        # Ensure the pattern exists
        if len(parts) == 2:
            new_name = parts[1]  # This is the part after the underscore

            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_name)

            os.rename(old_path, new_path)
            print(f"Renamed: {filename} → {new_name}")
