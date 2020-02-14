import pydicom
import tensorflow as tf
from pydicom.uid import UID
class dose:
    def __init__(self, file: str):
        super().__init__()
        
        slice = pydicom.read_file(file)
        pixels = slice.pixel_array
        self.samples_per_pixel = slice.SamplesPerPixel
        self.number_of_frames = slice.NumberOfFrames
        self.frame_increment_pointer = slice.FrameIncrementPointer
        self.dose_units = slice.DoseUnits
        self.grid_frame_offset_vector = slice.GridFrameOffsetVector
        self.dose_grid_scaling = slice.DoseGridScaling
        self.pixel_data = self.dose_grid_scaling * pixels 
        self.rows = slice.Rows
        self.columns = slice.Columns
        self.size_x = slice.PixelSpacing[0]
        self.size_y = slice.PixelSpacing[1]
        self.location = None
        try:
           self.location = slice.SliceLocation 
        except:
            pass
        self.frame_of_reference_uid = slice.FrameOfReferenceUID
        self.thickness = slice.SliceThickness
        self.image_orientation = slice.ImageOrientationPatient
        self.image_position = slice.ImagePositionPatient
        self.referenced_rt_plan = self.__get_sequence_data(slice)
        self.referenced_rt_struct = self.__get_sequence_data(slice)
        slice = None
        
        
    def create_tensor_from_pixels(self):
        pixel_tensor = []
        for s in range(len(self.Slices)):
            pixel_tensor.append(tf.convert_to_tensor(self.Slices[s].PixelData))
        return tf.convert_to_tensor(pixel_tensor)
    
    
    def __get_sequence_data(self, dcm):
        b_uid = dcm.get_item(0x300c0002)[0].get_item(0x00081155).value
        uid = UID(b_uid.decode('ASCII')) 
        return uid