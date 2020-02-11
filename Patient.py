import pydicom
import os
from Study import Study, Series, Image
from CreateDicomCollections import DICOMCollection

class patient:
    def __init__(self, mrn, collection: DICOMCollection):
        super().__init__()
        
        self.__collection = collection
        self.mrn = mrn
        self.study_uids = collection.study_uid_set
        self.series_uids = collection.series_uid_set
        self.raw_images = collection.raw_image_set
        self.image_uids = collection.image_uid_set
        self.studies = []
        
        
    def create_patient_studies(self):
        for st in self.__collection.study_uid_set:
            
        
        
        