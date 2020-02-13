import pydicom
import tensorflow as tf

class image:
    def __init__(self, file: path):
        super().__init__()
        
        slice = pydicom.read_file(file)
        slope = slice.RescaleSlope
        intercept = slice.RescaleIntercept
        pixels = slice.pixel_array
        self.pixel_data = slope * pixels + intercept
        self.rows = slice.Rows
        self.columns = slice.Columns
        self.size_x = slice.PixelSpacing[0]
        self.size_y = slice.PixelSpacing[1]
        self.location = slice.SliceLocation
        self.frame_of_reference_uid = slice.FrameOfReferenceUID
        self.thickness = slice.SliceThickness
        self.image_orientation = slice.ImageOrientation
        self.image_position = slice.ImagePosition
        slice = None
        
    def CreateTensorFromPixels(self):
        pixel_tensor = []
        for s in range(len(self.Slices)):
            pixel_tensor.append(tf.convert_to_tensor(self.Slices[s].PixelData))
        return tf.convert_to_tensor(pixel_tensor)
    

        
    