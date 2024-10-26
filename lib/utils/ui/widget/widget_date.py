from customtkinter import *
from lib.utils.ui import Color, Font

from datetime import datetime

class Widget_Date(CTkFrame):
    def __init__(self, master, mainApp, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
    
        # Variable
        self.mainApp = mainApp
        self.callback = None
        
        # Setting
        self.widget_width = 300
        self.widget_height = 50
        
        # UI
        self.build_ui()
        
        # Function
        self.FixedUpdate()
        
    def FixedUpdate(self):
        self.update_label()
        self.after(1800000, self.FixedUpdate)
    
    def build_ui(self):
        self.configure(fg_color = Color().transparent)
        self.grid_columnconfigure(0, weight = 1, minsize = self.widget_width)
        self.grid_rowconfigure(0, weight = 1, minsize = self.widget_height)
        
        self.frame_main = CTkFrame(self, fg_color = Color().white)
        self.frame_main.grid(row = 0, column = 0, sticky = NSEW)
        self.frame_main.grid_columnconfigure(0, weight = 1)
        self.frame_main.grid_rowconfigure(0, weight = 1)
        
        self.label_date = CTkLabel(self.frame_main, text = "DD:MM:YYY",
                              fg_color = Color().transparent,
                              font = (Font().font_bold, 40),
                              text_color = Color().black)
        self.label_date.grid(row = 0, column = 0)
    
    def update_label(self):
        date = datetime.now().strftime("%d/%m/%Y")
        self.label_date.configure(text = f"{date}")
    
    def set_callback(self, callback):
        self.callback = callback