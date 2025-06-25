import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

# file types
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Videos': ['.mp4', '.mkv', '.avi'],
    'Music': ['.mp3', '.wav', '.aac', '.flac'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Others': []
}

# organize files
def organize_folder(path):
    if not os.path.isdir(path):
        messagebox.showerror("Error", "Invalid folder path")
        return

    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        if os.path.isfile(full_path):
            ext = os.path.splitext(file)[1].lower()
            moved = False
            for category, extensions in file_types.items():
                if ext in extensions:
                    category_path = os.path.join(path, category)
                    os.makedirs(category_path, exist_ok=True)
                    shutil.move(full_path, os.path.join(category_path, file))
                    moved = True
                    break
            if not moved:
                other_path = os.path.join(path, "Others")
                os.makedirs(other_path, exist_ok=True)
                shutil.move(full_path, os.path.join(other_path, file))

# GUI
def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        organize_folder(folder_selected)

root = tk.Tk()
root.title("Auto File Organizer")

label = ttk.Label(root, text="Click the button below to select a folder:")
label.pack(padx=10, pady=10)

button = ttk.Button(root, text="Browse Folder", command=browse_folder)
button.pack(padx=10, pady=10)

root.mainloop()
