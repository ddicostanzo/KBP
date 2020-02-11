import pydicom
import os
import numpy as np
import tensorflow as tf
from Image import Image
from Study import Study

class Series:
    def __init__(self, study):
        super().__init__()
        
        self._study = study
        self._patient = study._patient
        self.Images = ParseImages(_patient._dcmlist)
        self.NumberOfImages = len(self.Images)
        self.FrameOfReferenceUID = GetFORUID()
        
        self.CTs = []
        self.PETs = []
        self.MRIs = []
        self.RTPlans = []
        self.RTStructs = []
        self.RTDoses = []
        self.RTImages = []
        self.Registrations = []
        
    
    
    def ParseImages(self, imgs):
        for i in imgs:
            img = Image(i)
            
        
    def GetFORUID(self, dcm):
        try:
            print(dcm[0x00200052].value)
        except:
            b_uid = dcm.get_item(0x30060010)[0].get_item(0x00200052).value
            uid = UID(b_uid.decode('ASCII')) 
            print(uid)
     
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
    
    def GetCTScan(self, path):
        
    def GetPETScan(self, path):
        
    def GetMRIScan(self, path):
        
    def GetRTPlan(self, dcm):
    
    def GetRTStruct(self, dcm):
        
    def GetRTDose(self, dcm):
        
    def GetRTImage(self, dcm):
        
    def GetRegistration(self, dcm):
    

        
    def CreateTensorFromPixels(self):
        pixel_tensor = []
        for s in range(len(self.Images)):
            pixel_tensor.append(tf.convert_to_tensor(self.Images[s].PixelData))
        return tf.convert_to_tensor(pixel_tensor)
    
