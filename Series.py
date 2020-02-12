import pydicom
from pydicom.uid import UID
import os
import numpy as np
import tensorflow as tf
from Image import image
from DicomImageType import DicomImageType

class series:
    def __init__(self, _images: dict, study):
        super().__init__()
        
        self._study = study
        self._patient = study._patient
        self.series_images = _images
        self.number_of_images = len(self.series_images)
        _dcm = pydicom.read_file(list(_images.keys())[0])
        self.FrameOfReferenceUID = self.GetFORUID(_dcm)
        self.series_type = self.SetDicomImageType(_dcm)
        
        # self.CTs = []
        # self.PETs = []
        # self.MRIs = []
        # self.RTPlans = []
        # self.RTStructs = []
        # self.RTDoses = []
        # self.RTImages = []
        # self.Registrations = []
        
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
    
    def ParseImages(self, imgs):
        for i in imgs:
            img = Image(i)
            
        
    def GetFORUID(self, dcm):
        try:
            return dcm[0x00200052].value
        except:
            b_uid = dcm.get_item(0x30060010)[0].get_item(0x00200052).value
            uid = UID(b_uid.decode('ASCII')) 
            return uid
     
    def SetCTScan(self, path):
        CT = CTScan(path)
        if not(CT in self.CTs):
            self.CTs.append(CT)
            
    def SetPETScan(self, path):
        PT = PTScan(path)
        if not(PT in self.PETs):
            self.PETs.append(PT)
            
    def SetMRIScan(self, path):
        MRI = MRIScan(path)
        if not(MRI in self.MRIs):
            self.MRIs.append(MRI)
            
    def SetRTPlan(self, dcm):
        plan = RTPlan(dcm)
        if not(plan in self.RTPlans):
            self.RTPlans.append(plan)
            
    def SetRTStruct(self, dcm):
        rtstruct = RTStruct(dcm)
        if not(rtstruct in self.RTStructs):
            self.RTStructs.append(rtstruct)
            
    def SetRTDose(self, dcm):
        dose = RTDose(dcm)
        if not(dose in self.RTDoses):
            self.RTDoses.append(dose)  
              
    def SetRTImage(self, dcm):
        img = RTImage(dcm)
        if not(img in self.RTImages):
            self.RTImages.append(img)   
             
    def SetRegistration(self, dcm):
        reg = Registration(dcm)
        if not(dcm in self.Registrations):
            self.Registrations.append(reg)
    
    
    def GetRTStruct(self, dcm):
        pass
    def GetCTScan(self, path):
        pass
    def GetPETScan(self, path):
        pass
    def GetMRIScan(self, path):
        pass
    def GetRTPlan(self, dcm):
        pass
    def GetRTStruct(self, dcm):
        pass
    def GetRTDose(self, dcm):
        pass
    def GetRTImage(self, dcm):
        pass
    def GetRegistration(self, dcm):
        pass

        
    def CreateTensorFromPixels(self):
        pixel_tensor = []
        for s in range(len(self.Images)):
            pixel_tensor.append(tf.convert_to_tensor(self.Images[s].PixelData))
        return tf.convert_to_tensor(pixel_tensor)
    
