from enum import Enum

class Result(Enum):
    RESULT = 0,
    OK = 1,
    NG = 2,
    ERROR = 3

class CameraSetting(Enum):
    camera_number = 1,
    camera_width = 2,
    camera_height = 3

class ClientSocketSetting(Enum):
    ip = 1,
    port = 2

class RobotCameraCoordinateSetting(Enum):
    offset_x = 1,
    offset_y = 2,
    mm_per_pixel_x = 3,
    mm_per_pixel_y = 4

class FindCentroidSetting(Enum):
    threshold = 1