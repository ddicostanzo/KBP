from pydicom.uid import UID


class file_uid:
    def __init__(self, path: str, study: UID, series: UID, image: UID):
        super().__init__()
        self.file_path = path
        self.study_uid = study 
        self.series_uid = series
        self.image_uid = image