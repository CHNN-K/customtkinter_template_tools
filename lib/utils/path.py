import os
import sys

def resource_path(path):
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, path)

class Path:
    def __init__(self):
        self.dir_bin = "bin"
        self.dir_config = "bin/config"
        self.json_setting_camera = "bin/config/setting_camera.json"
        self.json_setting_client_socket = "bin/config/setting_client_socket.json"
        self.json_setting_robot_camera_coordinate = "bin/config/setting_robot_camera_coordinate.json"
        self.json_setting_find_centriod = "bin/config/setting_find_centroid.json"
        
        self.image_exit = "bin/images/exit.png"
        self.image_history = "bin/images/history.png"
        
        self.image_history = resource_path("bin/images/history.png")