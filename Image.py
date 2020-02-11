import pydicom
from Patient import patient, study, series

class smage:
    def __init__(self, dcm):
        super().__init__()
        
        if dcm.Modality == 'RTSTRUCT':
            self.SetRTStruct(dcm)
        elif dcm.Modality == 'MR':
            self.SetMRIScan(root)
        elif dcm.Modality == 'PT':
            self.SetPETScan(root)
        elif dcm.Modality == 'RTPLAN':
            self.SetRTPlan(dcm)
        elif dcm.Modality == 'RTIMAGE':
            self.SetRTImage(dcm)
        elif dcm.Modality == 'RTDOSE':
            self.SetRTDose(dcm)
        elif dcm.Modality == 'RTSTRUCT':
            self.SetRTStruct(dcm)
        elif dcm.Modality == 'CT':
            self.SetCTScan(root)
        
        
        slope = slice.RescaleSlope
        intercept = slice.RescaleIntercept
        pixels = slice.pixel_array
        self.PixelData = slope * pixels + intercept
        self.Rows = slice.Rows
        self.Columns = slice.Columns
        self.SizeX = slice.PixelSpacing[0]
        self.SizeY = slice.PixelSpacing[1]
        self.Location = slice.SliceLocation
        self.FrameOfReferenceUID = slice.FrameOfReferenceUID
        self.Thickness = slice.SliceThickness
        
        
        def SetRTStruct(self, dcm):
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
        for s in range(len(self.Slices)):
            pixel_tensor.append(tf.convert_to_tensor(self.Slices[s].PixelData))
        return tf.convert_to_tensor(pixel_tensor)
    
    def ParseSlices(self, _dir):
        _slices = []
        files = os.listdir(_dir)
        for s in files:
            slice = CTData(os.path.join(_dir,s))
            _slices.append(slice)
        return _slices

    def GetFrameOfReferenceUID(self):
        if len(self.Slices) > 0:
            return self.Slices[0].FrameOfReferenceUID
        else:
            return null
        
    