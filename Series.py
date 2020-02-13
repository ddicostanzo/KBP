import pydicom
from pydicom.uid import UID
import os
import numpy as np
import tensorflow as tf
from Image import image
from DicomImageType import DicomImageType
from FileUID import file_uid

class series:
    def __init__(self, _images: list, study):
        super().__init__()
        
        self.__image_methods = self.__create_dict_of_image_methods()
        
        self._study = study
        self._patient = study._patient
        self.series_files = _images
        self.number_of_images = len(self.series_files)
        _dcm = pydicom.read_file(_images[0].file_path)
        self.FrameOfReferenceUID = self.GetFORUID(_dcm)
        self.series_modality = _dcm.Modality
        _dcm = None
        #self.series_images = create_images_for_series()
        self.__image_parsing_method = self.__image_methods[self.series_modality]
        self.__image_parsing_method(self.series_files)
        
        # self.CTs = []
        # self.PETs = []
        # self.MRIs = []
        # self.RTPlans = []
        # self.RTStructs = []
        # self.RTDoses = []
        # self.RTImages = []
        # self.Registrations = []
        
    def __create_dict_of_image_methods(self):
        methods = {}
        methods['CT'] = self.SetCTScan
        methods['REG'] = self.SetRegistration
        methods['RTDOSE'] = self.SetRTDose
        methods['RTIMAGE'] = self.SetRTImage
        methods['RTPLAN'] = self.SetRTPlan
        methods['RTSTRUCT'] = self.SetRTStruct
        methods['MR'] = self.SetMRIScan
        methods['PT'] = self.SetPETScan
        return methods
    
    
        
    def SetDicomImageType(self, dcm):
        _modality = dcm.Modality
        if dcm.Modality == 'RTSTRUCT':
            return DicomImageType.RTSTRUCT
        elif dcm.Modality == 'MR':
            return DicomImageType.MR
        elif dcm.Modality == 'PT':
            return DicomImageType.PT
        elif dcm.Modality == 'RTPLAN':
            return DicomImageType.RTPLAN
        elif dcm.Modality == 'RTIMAGE':
            return DicomImageType.RTIMAGE
        elif dcm.Modality == 'RTDOSE':
            return DicomImageType.RTDOSE
        elif dcm.Modality == 'REG':
            return DicomImageType.REG
        elif dcm.Modality == 'CT':
            return DicomImageType.CT
        else:
            return DicomImageType.Unknown
    
    def create_images_for_series(self):
        pass
        #images = []
        #for i in self.series_files:
            
        
            
        
    def GetFORUID(self, dcm):
        try:
            return dcm[0x00200052].value
        except:
            b_uid = dcm.get_item(0x30060010)[0].get_item(0x00200052).value
            uid = UID(b_uid.decode('ASCII')) 
            return uid
     
    def SetCTScan(self):
        pass
                
    def SetPETScan(self):
        pass
            
    def SetMRIScan(self):
        pass
            
    def SetRTPlan(self):
        pass
            
    def SetRTStruct(self):
        pass
            
    def SetRTDose(self):
        pass
              
    def SetRTImage(self):
        pass  
             
    def SetRegistration(self):
        pass
    
    
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
    
