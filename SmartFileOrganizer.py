import os
import shutil
import customtkinter as ctk
from tkinter import filedialog, messagebox

# --- CORE LOGIC ---
FILE_CATEGORIES = {
    "Images": [".jpeg", ".jpg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mkv", ".avi", ".webm"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar"]
}

def organize_files(target_folder):
    if not target_folder or not os.path.exists(target_folder):
        messagebox.showerror("Error", "Kripya ek sahi folder select karein!")
        return

    moved_count = 0
    for item in os.listdir(target_folder):
        item_path = os.path.join(target_folder, item)

        if os.path.isdir(item_path):
            continue

        file_name, file_extension = os.path.splitext(item)
        file_extension = file_extension.lower() 

        moved = False
        for category, extensions in FILE_CATEGORIES.items():
            if file_extension in extensions:
                category_folder = os.path.join(target_folder, category)
                if not os.path.exists(category_folder):
                    os.makedirs(category_folder)
                shutil.move(item_path, os.path.join(category_folder, item))
                moved = True
                moved_count += 1
                break
        
        if not moved and file_extension != "":
            others_folder = os.path.join(target_folder, "Others")
            if not os.path.exists(others_folder):
                os.makedirs(others_folder)
            shutil.move(item_path, os.path.join(others_folder, item))
            moved_count += 1

    messagebox.showinfo("Success", f"Ho gaya! Total {moved_count} files organize ho gayi hain.")


# --- UI DESIGN ---
def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        path_entry.delete(0, ctk.END)
        path_entry.insert(0, folder)

def start_organizing():
    folder_path = path_entry.get()
    organize_files(folder_path)

# System settings
ctk.set_appearance_mode("Dark")  
ctk.set_default_color_theme("blue") 

# App window setup
app = ctk.CTk()  
app.geometry("500x300")
app.title("Smart File Organizer")

# Title Label
title_label = ctk.CTkLabel(app, text="Smart File Organizer", font=("Arial", 24, "bold"))
title_label.pack(pady=30)

# Path Entry Box
path_entry = ctk.CTkEntry(app, placeholder_text="Folder ka path yahan aayega...", width=350)
path_entry.pack(pady=10)

# Browse Button
browse_btn = ctk.CTkButton(app, text="Browse Folder", command=browse_folder, fg_color="#4CAF50", hover_color="#45a049")
browse_btn.pack(pady=10)

# Organize Button
organize_btn = ctk.CTkButton(app, text="Organize Now!", command=start_organizing, font=("Arial", 16, "bold"), height=40)
organize_btn.pack(pady=20)

# App Run karna
app.mainloop()