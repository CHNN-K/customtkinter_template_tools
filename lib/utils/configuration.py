import os
from lib.utils import Path, CameraSetting, RobotCameraCoordinateSetting, FindCentroidSetting
import json

class ApplicationConfiguration:
    def checkDirectoryExist(self):
        if os.path.isdir(Path().dir_config):
            pass
        else:
            os.mkdir(Path().dir_bin)
            os.mkdir(Path().dir_config)
    
    def createCameraSetting(self):
        self.checkDirectoryExist()
        if os.path.isfile(Path().json_setting_camera):
            return
        
        with open(Path().json_setting_camera, 'w') as file:
            default_setting = {
                CameraSetting.camera_number.name : 0,
                CameraSetting.camera_width.name : 2592,
                CameraSetting.camera_height.name : 1944,
            }
            json.dump(default_setting, file, indent = 4)
    
    def createClientSocketSetting(self):
        self.checkDirectoryExist()
        if os.path.isfile(Path().json_setting_client_socket):
            return
        
        with open(Path().json_setting_client_socket, 'w') as file:
            default_setting = {
                "ip" : "127.0.0.1",
                "port" : 2001
            }
            json.dump(default_setting, file, indent = 4)
    
    def createRobotCameraCoordinateSetting(self):
        self.checkDirectoryExist()
        if os.path.isfile(Path().json_setting_robot_camera_coordinate):
            return
        
        with open(Path().json_setting_robot_camera_coordinate, 'w') as file:
            default_setting = {
                RobotCameraCoordinateSetting.offset_x.name : 0,
                RobotCameraCoordinateSetting.offset_y.name : 0,
                RobotCameraCoordinateSetting.mm_per_pixel_x.name : 0.1,
                RobotCameraCoordinateSetting.mm_per_pixel_y.name : 0.1
            }
            json.dump(default_setting, file, indent = 4)
    
    def createFindCentroidSetting(self):
        self.checkDirectoryExist()
        if os.path.isfile(Path().json_setting_find_centriod):
            return
        
        with open(Path().json_setting_find_centriod, 'w') as file:
            default_setting = {
                FindCentroidSetting.threshold.name : 100
            }
            json.dump(default_setting, file, indent = 4)