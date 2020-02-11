import pydicom
import os
from Study import study
from CreateDicomCollections import DICOMCollection

class patient:
    def __init__(self, mrn: str, collection: DICOMCollection):
        super().__init__()
        
        self.__collection = collection
        self.mrn = mrn
        self.study_uids = collection.study_uid_set
        self.series_uids = collection.series_uid_set
        self.raw_images = collection.raw_image_set
        self.image_uids = collection.image_uid_set
        self.studies = []
        self.create_patient_studies()
        
    def create_patient_studies(self):
        for st in self.__collection.study_uid_set:
            images_from_study = [i for i in self.raw_images if i.StudyInstanceUID = st]
            _study = study(self, uid, images_from_study)
            self.studies.append(_study)
            
        
    
        