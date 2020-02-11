import pydicom
import os
from Study import Study, Series, Image

class Patient:
    def __init__(self,path):
        super().__init__()
        
        self._dcmlist = self.BuildDICOMList(path)
        self.Studies = self.GetStudiesUIDs()
        
    def BuildDICOMList(self,path):
        _dcmlist = []
        for root, dirs, files in os.walk(path):
            for f in files:
                _root_dcm = os.path.join(root, dcm)
                dcm = pydicom.read_file(_root_dcm)
                _dcmlist.append(dcm)
        return _dcmlist
                
    def GetStudiesUIDs(self):
        studies = []
        for d in self._dcmlist:
            studies.append(d.StudyInstanceUID)
        return set(studies)          
    
    
        
        