import tkinter as tk
from tkinter import filedialog

def open_file():
    root = tk.Tk()
    root.withdraw()
    
    file_path = filedialog.askopenfilename()

    root.destroy()
    return file_path