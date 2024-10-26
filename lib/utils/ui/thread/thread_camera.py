import threading
import cv2
import numpy as np
import time
import os
from PIL import Image
from datetime import datetime
import json

from lib.utils import Path, CameraSetting

class Thread_Camera(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._stop_event = threading.Event()
        self.daemon = True
        self.debug = False
        
        self.cameraNumber = 0
        self.width = 2592
        self.height = 1944
        self.videoCapture = None
        
        self.fps = 0
        self.start_time = time.time()
        self.frameCount = 0
        
        self.image = None
        self.processImage = None
        self.showImage = None
        
        self.buffer_snapImage = None
        self.buffer_showSnapImage = None
        
        self.cameraSetup()
    
    def run(self):
        while not self._stop_event.is_set():
            self.calculateFPS()
            try:
                self.ret, self.frame = self.videoCapture.read()
                # self.frame = cv2.imread("detection_test.png")
                self.processImage = self.frame.copy()
                image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                
                self.add_cursor(image)
                
                self.image = image
                self.showImage = cv2.resize(image,(0,0),fx = 0.4, fy = 0.4)
            except:
                pass
        print("Camera thread stop")
    
    def stop(self):
        self._stop_event.set()

    def cameraSetup(self):
        self.json_read_setting()
        
        self.videoCapture = cv2.VideoCapture(self.cameraNumber)
        self.videoCapture.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.videoCapture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
    
    def add_cursor(self, image):
        h, w = image.shape[0], image.shape[1]
        lenght = 30
        cv2.line(image, (w//2 - lenght, h//2), (w//2 + lenght, h//2), (255,0,0), 3)
        cv2.line(image, (w//2, h//2 - lenght), (w//2, h//2 + lenght), (255,0,0), 3)
        return image
    
    def calculateFPS(self):
        current_time = time.time()
        self.frameCount += 1
        
        elapsed_time = current_time - self.start_time
        if elapsed_time > 1:
            fps = self.frameCount / elapsed_time
            self.fps = f"{fps:.2f}"
            self.frameCount = 0
            self.start_time = current_time
    
    def snapshotImage(self):
        snapshot = Image.fromarray(np.array(self.frame))
        try:
            snapshot = Image.fromarray(np.array(self.frame))
            now = datetime.now()
            time = now.strftime("%H%M%S")
            date = now.strftime("%d%m%Y")
            file = f"Snapshot_{date}_{time}"
            imageType = ".bmp"
            
            if not os.path.isdir("Snapshot"):
                os.mkdir("Snapshot")
                
            snapshot.save(f"Snapshot/{file}{imageType}")
            
            print(f"Snapshot : {file}{imageType}")
        except:
            pass
    
    def snapshotImage_trigger(self):
        self.buffer_snapImage = self.image
        self.buffer_showSnapImage = cv2.resize(self.buffer_snapImage, (0,0), fx = 0.2, fy = 0.2)
    
    def json_read_setting(self):
        try:
            with open(Path().json_setting_camera, 'r') as file:
                json_data = json.load(file)
            
            self.cameraNumber = json_data[CameraSetting.camera_number.name]
            self.width = json_data[CameraSetting.camera_width.name]
            self.height = json_data[CameraSetting.camera_height.name]
        except:
            print ("Can't find json camera setting")