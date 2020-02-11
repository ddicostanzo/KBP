import pydicom
from Patient import patient, study, series
from DicomImageType import DicomImageType

class Image:
    def __init__(self, dcm):
        super().__init__()
        
        self.SOPInstanceUID = dcm.SOPInstanceUID
        self.FrameOfReferenceUID = dcm.FrameOfReferenceUID
        self.ImageType = SetDicomImageType(dcm)
        self.Series = Series()
        self.Study = Study()
        self.Patient = Patient()
        
    def SetDicomImageType(self, dcm):
        _modality = dcm.Modality
        if dcm.Modality == 'RTSTRUCT':
            return DicomImageType.RTStruct
        elif dcm.Modality == 'MR':
            return DicomImageType.Image
        elif dcm.Modality == 'PT':
            return DicomImageType.Image
        elif dcm.Modality == 'RTPLAN':
            return DicomImageType.RTPlan
        elif dcm.Modality == 'RTIMAGE':
            return DicomImageType.RTImage
        elif dcm.Modality == 'RTDOSE':
            return DicomImageType.RTDose
        elif dcm.Modality == 'REG':
            return DicomImageType.Registration
        elif dcm.Modality == 'CT':
            return DicomImageType.Image
        else:
            return DicomImageType.Unknown
        
  