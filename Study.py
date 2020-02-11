import pydicom
import os
from Series import Series, Image

class Study:
    def __init__(self, patient):
        super().__init__()
        self._patient = patient
        self.StudyUID = 
        self.SeriesUIDs = self.GetSeriesUIDs()
        self.Series = []
        
    def GetSeriesUIDs(self):
        series = []
        for d in self._patient._dcmlist:
            series.append(d.SeriesInstanceUID)
        return set(series)  
        
     def GetSeries(self, uids):
        series = []
        for s in uids:
            for i in self._patient._dcmlist:
                if i.SeriesInstanceUID == s:
                    series.append(i)
        
        
        
        
        
                    
    