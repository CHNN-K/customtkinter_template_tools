from customtkinter import *
from lib.utils.ui import Color, Font, Thread_Camera

from PIL import Image

class Widget_Camera(CTkFrame):
    def __init__(self, master, mainApp, camera : Thread_Camera, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
    
        # Variable
        self.mainApp = mainApp
        self.camera = camera
        self.callback = None
        
        # Setting
        self.widget_width = 1012
        self.widget_height = 760
        
        # UI
        self.build_ui()
        
        # Function
        self.FixedUpdate()
        
    def FixedUpdate(self):
        self.update_camera_frame()
        self.after(10, self.FixedUpdate)
    
    def build_ui(self):
        self.configure(fg_color = Color().transparent)
        self.grid_columnconfigure(0, weight = 1, minsize = self.widget_width)
        self.grid_rowconfigure(0, weight = 1, minsize = self.widget_height)
        
        self.frame_main = CTkFrame(self, fg_color = Color().widget_background, corner_radius = 0)
        self.frame_main.grid(row = 0, column = 0, sticky = NSEW)
        self.frame_main.grid_columnconfigure(0, weight = 1)
        self.frame_main.grid_rowconfigure(0, weight = 1)
        
        self.label_camera = CTkLabel(self.frame_main, text = "Display camera image", 
                                    fg_color = Color().transparent,
                                    font = (Font().font_bold, 32),
                                    text_color = Color().black)
        self.label_camera.grid(row = 0, column = 0)
        
        self.image_camera = CTkLabel(self.frame_main, text = "", 
                                    fg_color = Color().transparent,
                                    corner_radius = 0)
        self.image_camera.grid(row = 0, column = 0)
        
        self.label_fps = CTkLabel(self.frame_main, text = "FPS:0.00", 
                                  fg_color = Color().black,
                                  font = (Font().font, 14),
                                  text_color = Color().white)
        self.label_fps.grid(row = 0, column = 0, ipadx = 5, sticky = NE)
    
    def update_camera_frame(self):
        try:
            self.image_camera.configure(image = CTkImage(Image.fromarray(self.camera.showImage), size = (self.widget_width,self.widget_height)))
            self.label_fps.configure(text = f"FPS:{self.camera.fps}")
        except:
            pass
    
    def set_callback(self, callback):
        self.callback = callback