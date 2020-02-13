import os
import pydicom
from pydicom.uid import UID
from Patient import patient
from FileUID import file_uid


class DICOMCollection:
    def __init__(self, path: str):
        super().__init__()
        
        self.__read_dir = path
        self.patient_id_set = set()
        self.study_uid_set = set()
        self.series_uid_set = set()
        self.image_uid_set = set()
        self.raw_image_list = []
        self.patients = []
        
    def GenerateFullCollection(self):
        self.__CreateDICOMCollections(self.__read_dir)
        self.__CreatePatients()
    
    def __CreateDICOMCollections(self,path):
        for root, dirs, files in os.walk(path):
            for f in files:
                dcm = pydicom.read_file(os.path.join(root,f))
                self.patient_id_set.add(dcm.PatientID)
                self.study_uid_set.add(dcm.StudyInstanceUID)
                self.series_uid_set.add(dcm.SeriesInstanceUID)
                self.image_uid_set.add(dcm.SOPInstanceUID)
                self.raw_image_list.append(file_uid(os.path.join(root,f), dcm.StudyInstanceUID, dcm.SeriesInstanceUID, dcm.SOPInstanceUID))

    
    def __CreatePatients(self):
        for p in self.patient_id_set:
            pat = patient(p, self)
            self.patients.append(pat)
            
            

# if dcm.Modality == 'RTSTRUCT':
#                 print('RT Struct FOR')
#                 try:
#                     print(dcm[0x00200052].value)
#                 except:
#                     b_uid = dcm.get_item(0x30060010)[0].get_item(0x00200052).value
#                     uid = UID(b_uid.decode('ASCII')) 
#                     print(uid)
                    
#             if dcm.Modality == 'CT':
#                 try:
#                     fors.append(dcm.FrameOfReferenceUID)
#                 except:
#                     print(f)