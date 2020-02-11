import pydicom
import os
from Patient import patient
from Series import series, image

class study:
    def __init__(self, patient: patient, study_uid: str, images: set):
        super().__init__()
        self._patient = patient
        self.__study_uids = patient.study_uids
        self.series_uids = [uid.SeriesInstanceUID for uid in images if uid.StudyInstanceUID == study_uid]
        self.image_uids = [i.SOPInstanceUID for i in images]
        self.study_images = images
        self.study_uid = study_uid
        self.series = []
        self.create_series_for_study();
        
    def create_series_for_study(self):
        for s in self.series_uids:
            img = [i for i in self.study_images if i.SeriesInstanceUID == s]
            _series = series(self, img)
            self.series.append(_series)
            
        
        
        
        
        
        
                    
    