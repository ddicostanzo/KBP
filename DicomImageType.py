from enum import Enum
class DicomImageType(Enum):
    CT = 1
    RTDOSE = 2
    RTIMAGE = 3
    RTPLAN = 4
    RTSTRUCT = 5
    REG = 6
    MR = 7
    PT = 8
    UNKNOWN = 99
  