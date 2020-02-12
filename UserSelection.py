import tkinter as tk
from tkinter import filedialog
from CreateDicomCollections import DICOMCollection

root = tk.Tk()
root.withdraw()

read_directory = filedialog.askdirectory()

collection = DICOMCollection(read_directory)
collection.GenerateFullCollection()
print(collection.patients)