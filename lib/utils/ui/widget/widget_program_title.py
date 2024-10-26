from customtkinter import *
from lib.utils.ui import Color, Font

class Widget_Program_Title(CTkFrame):
    def __init__(self, master, mainApp, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
    
        # Variable
        self.mainApp = mainApp
        self.callback = None
        
        # Setting
        self.widget_width = 490
        self.widget_height = 50
        
        # UI
        self.build_ui()
    
    def build_ui(self):
        self.configure(fg_color = Color().transparent)
        self.grid_columnconfigure(0, weight = 1, minsize = self.widget_width)
        self.grid_rowconfigure(0, weight = 1, minsize = self.widget_height)
        
        self.frame_main = CTkFrame(self, fg_color = Color().white)
        self.frame_main.grid(row = 0, column = 0, sticky = NSEW)
        self.frame_main.grid_rowconfigure(0, weight = 1)
        self.frame_main.grid_columnconfigure(0, weight = 1)
        self.frame_main.grid_columnconfigure(1, weight = 0)
        
        self.label_title = CTkLabel(self.frame_main, text = "Program Title",
                                    fg_color = Color().transparent,
                                    font = (Font().font_bold, 40),
                                    text_color = Color().black)
        self.label_title.grid(row = 0, column = 0)
        
        self.label_version = CTkLabel(self.frame_main, text = "v0.0.0",
                                    fg_color = Color().black,
                                    corner_radius = 5,
                                    font = (Font().font_bold, 16),
                                    text_color = Color().white)
        self.label_version.grid(row = 0, column = 1, sticky = E)
    
    def set_label(self, title : str, version : str):
        self.label_title.configure(text = f"{title}")
        self.label_version.configure(text = f"v{version}")
    
    def set_callback(self, callback):
        self.callback = callback