import pydicom
import os
from Series import series
from FileUID import file_uid

class study:
    def __init__(self, study_uid: str, images: list, patient):
        super().__init__()
        
        self._patient = patient
        self.__study_uids = patient.study_uids
        self.series_uids = set([i.series_uid for i in images])
        self.image_uids = set([i.image_uid for i in images])
        self.study_images = images
        self.study_uid = study_uid
        self.series = []
        self.create_series_for_study();
    
    def create_series_for_study(self):
        for s in self.series_uids:
            imgs = [i for i in self.study_images if i.series_uid == s]
            _series = series(imgs, self)
            self.series.append(_series)
            
        
        
        
        
        
        
                    
    