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
        self.__image_parsing_method = self.__image_methods[self.series_modality]
        self.__series_images = None
        
    def GetFORUID(self, dcm):
        try:
            return dcm[0x00200052].value
        except:
            b_uid = dcm.get_item(0x30060010)[0].get_item(0x00200052).value
            uid = UID(b_uid.decode('ASCII')) 
            return uid
        
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
    
    def get_series_images(self):
        if self.__series_images == None:
            self.__series_images = self.create_series_images()
        return self.__series_images
        
        
    def create_series_images(self):
        imgs = []
        for i in self.series_files:
            imgs.append(self.__image_parsing_method(i.file_path))
        return imgs
    
    def SetCTScan(self, img: str):
        image = image(img)
        return image 
                            
    def SetPETScan(self, img: str):
        image = image(img)
        return image
            
    def SetMRIScan(self, img: str):
        image = image(img)
        return image
            
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
