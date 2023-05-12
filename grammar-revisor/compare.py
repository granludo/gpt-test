import tkinter as tk
from tkinter import filedialog
import difflib

def load_file():
    file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
    return file_path

def compare_files():
    file1_path = load_file()
    file2_path = load_file()

    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        lines1 = file1.readlines()
        lines2 = file2.readlines()

    diff = difflib.ndiff(lines1, lines2)

    diff_window = tk.Toplevel(root)
    diff_text = tk.Text(diff_window)
    diff_text.pack()

    for line in diff:
        diff_text.insert(tk.END, line)

root = tk.Tk()

compare_button = tk.Button(root, text='Compare Files', command=compare_files)
compare_button.pack()

root.mainloop()
