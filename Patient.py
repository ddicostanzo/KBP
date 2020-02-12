import pydicom
import os
from Study import study


class patient:
    def __init__(self, mrn: str, collection):
        super().__init__()
        
        self.__collection = collection
        self.mrn = mrn
        self.study_uids = collection.study_uid_set
        self.series_uids = collection.series_uid_set
        self.raw_image_dict = collection.raw_image_dict
        self.image_uids = collection.image_uid_set
        self.studies = []
        self.create_patient_studies()
        
    def create_patient_studies(self):
        for st in self.__collection.study_uid_set:
            images_from_study = {k:v for k,v in self.raw_image_dict.items() if v[0] == st}
            _study = study(st, images_from_study, self)
            self.studies.append(_study)
            
        
    
        