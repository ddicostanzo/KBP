#from CTDataClass import CTData
#from CTScanClass import CTScan
import os
import pydicom
from pydicom.uid import UID
           
path = r'C:/Users/dico01/Desktop/HN-CHUM-001/'

#CT = CTScan(path)

print(path)

fors = []

for root, dirs, files in os.walk(path):
    for f in files:
        dcm = pydicom.read_file(os.path.join(root,f))
        if dcm.Modality == 'RTSTRUCT':
            print('RT Struct FOR')
            try:
                print(dcm[0x00200052].value)
            except:
                b_uid = dcm.get_item(0x30060010)[0].get_item(0x00200052).value
                uid = UID(b_uid.decode('ASCII')) 
                print(uid)
                
        if dcm.Modality == 'CT':
            try:
                fors.append(dcm.FrameOfReferenceUID)
            except:
                print(f)
            
ct_fors = set(fors)
print(ct_fors)