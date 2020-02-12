import pydicom
import os
from Series import series

class study:
    def __init__(self, study_uid: str, images: dict, patient):
        super().__init__()
        self._patient = patient
        self.__study_uids = patient.study_uids
        self.series_uids = set([v[1] for k,v in images.items()])
        self.image_uids = set([v[2] for k,v in images.items()])
        self.study_images = images
        self.study_uid = study_uid
        self.series = []
        self.create_series_for_study();
    
    def create_series_for_study(self):
        for s in self.series_uids:
            imgs = {k:v for k,v in self.study_images.items() if v[1] == s}
            _series = series(imgs, self)
            self.series.append(_series)
            
        
        
        
        
        
        
                    
    