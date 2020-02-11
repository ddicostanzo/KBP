import
import tkinter as tk
from tkinter import filedialog
from CreateDicomCollections import DICOMCollection

root = tk.Tk()
root.withdraw()

read_directory = filedialog.askdirectory()

collection = DICOMCollection()
collection.CreateDICOMCollections(read_directory)
