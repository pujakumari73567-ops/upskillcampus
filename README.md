# 📁 Smart File Organizer

> **A modern, GUI-based Python application that automates the tedious task of sorting messy directories into organized folders.**

[![Internship Project](https://img.shields.io/badge/Project-Industrial%20Internship-blue?style=for-the-badge)](https://upskillcampus.com/)
[![Language](https://img.shields.io/badge/Language-Python%203-yellow?style=for-the-badge&logo=python)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey?style=for-the-badge&logo=windows)](https://www.microsoft.com/windows)

---

## 🌟 About the Project

Cluttered "Downloads" or "Desktop" folders are a universal problem. Manual sorting is time-consuming and prone to human error.

The **Smart File Organizer** solves this problem by providing a user-friendly desktop interface. Built using Python and the modern CustomTkinter GUI framework, it scans any user-selected directory, intelligently identifies file types (Images, Documents, Videos, etc.) using their extensions, and seamlessly moves them into organized subfolders.

This project was developed during my Industrial Internship with **upskill Campus** and The IoT Academy, in collaboration with **UniConverge Technologies Pvt Ltd (UCT)**.

---

## ✨ Key Features

* **⚡ Automated Organization:** Instantly detects file types and sorts them without manual intervention.
* **🎨 Modern UI/UX:** A clean, dark-themed interactive Graphical User Interface built with CustomTkinter.
* **💻 Standalone Executable:** Includes a compiled `.exe` version, allowing non-technical users to run the application without installing Python.
* **🛡️ Intelligent Handling:**
    * Gracefully handles files with unknown extensions by placing them in an 'Others' folder.
    * Avoids accidental overwriting by handling duplicate filenames.
    * Skips existing directories to prevent redundant processing.

---

## 🛠️ Technologies Used

| Technology | Purpose |
| :--- | :--- |
| **Python 3** | Core Programming Language |
| **CustomTkinter** | Modern Graphical User Interface Framework |
| **OS Module** | Backend File System Interactions |
| **Shutil Module** | High-level File Move Operations |
| **PyInstaller** | Packaging the script into a standalone `.exe` |

---

## 🚀 How to Run the Application

Since you requested the full code, including dependencies and the `.exe`, to be pushed, you have two ways to run the app:

### Method 1: Running the Pre-compiled Application (Easiest)

1.  Clone this repository to your local machine:
    ```bash
   https://github.com/pujakumari73567-ops/upskillcampus.git
    ```
2.  Navigate into the `dist` directory:
    ```text
    Upskill-Smart-File-Organizer/dist/
    ```
3.  Double-click on **`organizer.exe`** to launch the software instantly.

### Method 2: Running from Source Code (Developer Mode)

1.  Clone the repository and navigate into the folder.
2.  Install the necessary dependencies (ensure Python is installed):
    ```bash
    pip install customtkinter
    ```
3.  Run the script:
    ```bash
    python organizer.py
    ```

---

## 🔧 Project Structure

* `organizer.py`: The main source code (Core Logic + GUI).
* `README.md`: Project documentation (this file).
* `TestFolder/`: A sample directory containing mixed dummy files to test the organizer's functionality.
* `dist/`: Contains the standalone `organizer.exe` application.
* `build/`: Build artifacts from PyInstaller.

---

## 🔮 Future Scope

* 🔄 **Undo Functionality:** Allow users to reverse the organization process.
* 📝 **Custom Categories:** Enable users to define their own sorting rules via the UI.
* 📅 **Scheduling:** Automatic weekly organization of specified folders in the background.

---

## 👩‍💻 Developed By

* **Student Name:** Pooja Kumari
* **Institution:** Amity University, Noida
* **Mentored By:** upskill Campus & UniConverge Technologies Pvt Ltd (UCT).

---
