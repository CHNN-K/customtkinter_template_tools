from customtkinter import *
import threading
import socket
import requests
import time
from datetime import datetime
import cv2
from PIL import Image
import numpy as np

class Color:
    def __init__(self):
        self.main = "#1F6AA5"
        self.background = "#3A3A3A"
        self.background_frame = "#181717"
        self.white = "#F2F2F2"
        self.red = "#C00000"
        self.green = "#00B050"
        self.blue = "#0078D4"
        self.black = "#0D0D0D"
        self.pink = "#F24171"
        self.gray = "#424242"
        
        self.transparent = "transparent"
        self.disable = "#626262"

class ServerModule(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.host_ip = "127.0.0.1"
        self.port = 2001
        self.daemon = True
        self._is_stop = threading.Event()
        self.data = ""
        self.isConnect = False
        
        self.snap_callback = None

    def run(self):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.settimeout(0.2)
        host_ip = self.host_ip
        sock.bind((host_ip, self.port))
        sock.listen(1)
        while not self._is_stop.is_set():
            try:
                client, addr = sock.accept()
                print(f"Connected : {addr}")
                self.isConnect = True
                while True:
                    try:
                        data = client.recv(1024).decode()
                        if data != "":
                            print(f"server recieve : {data}")
                            
                            if data == "SNAP":
                                self.snap_function_callback()
                                
                            time.sleep(0.1)
                        
                        if not data:
                            client.close()
                            self.isConnect = False
                            print("Client disconnect")
                            self.log = "Robot disconnected"
                            time.sleep(1)
                            print("Waiting for connecting.")
                            break
                        data = ""

                    except socket.error as se:
                        client.close()
                        self.isConnect = False
                        print("Critical Client disconnect")
                        time.sleep(1)
                        print("Waiting for connecting.")
                        break

            except socket.timeout:
                pass
        print("Close server")
    
    def snap_function_callback(self):
        if self.snap_callback:
            self.snap_callback()
    
    def set_snap_callback(self, callback):
        self.snap_callback = callback
    
    def stop(self):
        self._is_stop.set()

    def status(self):
        return not self._is_stop.is_set()

class ThreadCamera(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._stop_event = threading.Event()
                
        self.cameraList = []
        self.cameraNumber = 0
        self.width = 2592
        self.height = 1944
        self.videoCapture = None
        
        self.fps = 0
        self.start_time = time.time()
        self.frameCount = 0
        
        self.image = None
        self.showImage = None
        
        self.buffer_snapImage = None
        self.buffer_showSnapImage = None
        
        self.cameraSetup()
    
    def run(self):
        while not self._stop_event.is_set():
            self.calculateFPS()
            try:
                self.ret, self.frame = self.videoCapture.read()
                self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                image = self.frame
                
                self.showImage = cv2.resize(image,(0,0),fx = 0.4, fy = 0.4)
                self.image = image
            except:
                pass
        print("Camera thread stop")
    
    def stop(self):
        self._stop_event.set()

    def cameraSetup(self):
        self.videoCapture = cv2.VideoCapture(self.cameraNumber)
        self.videoCapture.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.videoCapture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
    
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


class MainApp(CTk):
    def __init__(self):
        super().__init__()

        # Variable
        self.image_width = 2592
        self.image_height = 1944
        self.camera_display_width = int(self.image_width/2.5)
        self.camera_display_height = int(self.image_height/2.5)
        self.snapshot_display_width = int(self.image_width/5)
        self.snapshot_display_height = int(self.image_height/5)
        
        # Screen Setting
        screen_width = 1600
        screen_height = 900
        self.geometry(f"{screen_width}x{screen_height}+0+0")
        self.resizable(False, False)
        set_appearance_mode("Dark")
        self.title("Camera Test")
        
        self.protocol("WM_DELETE_WINDOW", self.exitApplication)
        self.bind("<Escape>", lambda event : self.exitApplication())
        
        self.camera = ThreadCamera()
        self.camera.start()
        
        self.serverModule = ServerModule()
        self.serverModule.start()
        self.serverModule.set_snap_callback(self.btn_snapshot_callback)
        
        self.build_ui()
        self.FixedUpdate()

    def build_ui(self):
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)
        
        self.frame_main = CTkFrame(self)
        self.frame_main.grid(row = 0, column = 0, sticky = NSEW)
        self.frame_main.grid_rowconfigure(0, weight = 1)
        self.frame_main.grid_columnconfigure(0, weight = 0)
        self.frame_main.grid_columnconfigure(1, weight = 1)
        
        self.entry_camera_display = CTkEntry(self.frame_main, corner_radius = 0,
                                             width = self.camera_display_width,
                                             height = self.camera_display_height,
                                             border_color = Color().white,
                                             justify = CENTER,
                                             border_width = 2)
        self.entry_camera_display.grid(row = 0, column = 0, ipadx = 2, ipady = 2)
        
        self.image_camera_display = CTkLabel(self.entry_camera_display, text = "")
        self.image_camera_display.grid(row = 0, column = 0)
        
        self.label_camera_fps = CTkLabel(self.entry_camera_display, text = "FPS:00.00",
                                         fg_color = Color().white,
                                         text_color = Color().black)
        self.label_camera_fps.grid(row = 0, column = 0, ipadx = 2, sticky = NE)
        
        self.btn_camera_snapshot = CTkButton(self.entry_camera_display, text = "📸",
                                            width = 30, height = 30,
                                            corner_radius = 0,
                                            fg_color = Color().white,
                                            text_color = Color().black,
                                            hover_color = Color().green,
                                            command = self.camera.snapshotImage)
        self.btn_camera_snapshot.grid(row = 0, column = 0, ipadx = 2, sticky = SE)
        
        self.frame_right = CTkFrame(self.frame_main, fg_color = Color().transparent)
        self.frame_right.grid(row = 0, column = 1)
        self.frame_right.grid_columnconfigure(0, weight = 1)
        self.frame_right.grid_rowconfigure(0, weight = 1)
        
        self.entry_snapshot_display = CTkEntry(self.frame_right, corner_radius = 0,
                                             width = self.snapshot_display_width,
                                             height = self.snapshot_display_height,
                                             border_color = Color().white,
                                             justify = CENTER,
                                             border_width = 2)
        self.entry_snapshot_display.grid(row = 0, column = 0, ipadx = 2, ipady = 2)
        
        self.image_snapshot_display = CTkLabel(self.entry_snapshot_display, text = "")
        self.image_snapshot_display.grid(row = 0, column = 0)
        
        self.btn_snapshot = CTkButton(self.frame_right, text = "Snapshot Trigger",
                                      command = self.btn_snapshot_callback)
        self.btn_snapshot.grid(row = 1, column = 0)
    
    def FixedUpdate(self):
        self.cameraUpdate()
        self.after(10, self.FixedUpdate)
    
    def cameraUpdate(self):
        try:
            self.processImage = Image.fromarray(self.camera.showImage)
            self.image_camera_display.configure(image = CTkImage(self.processImage, size = (int(self.camera.width/2.5), self.camera.height/2.5)))
            self.label_camera_fps.configure(text = f"FPS:{self.camera.fps}")
        except:
            pass
        
    def btn_snapshot_callback(self):
        self.camera.snapshotImage_trigger()
        image = Image.fromarray(self.camera.buffer_showSnapImage)
        self.image_snapshot_display.configure(image = CTkImage(image, size = (int(self.camera.width/5), self.camera.height/5)))
    
    def exitApplication(self):
        self.camera.videoCapture.release()
        self.camera.stop()
        self.serverModule.stop()
        self.destroy()

app = MainApp()
app.mainloop()