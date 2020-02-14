import tkinter as tk
from tkinter import filedialog
from CreateDicomCollections import DICOMCollection

root = tk.Tk()
root.withdraw()

read_directory = filedialog.askdirectory()

collection = DICOMCollection(read_directory)
collection.GenerateFullCollection()
print(collection.patients)




# How to get data
for st in collection.patients[0].studies:
    for se in st.series_list:
        if se.series_modality == 'RTDOSE':
            se.get_series_images()