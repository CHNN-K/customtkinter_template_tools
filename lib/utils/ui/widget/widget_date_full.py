from customtkinter import *
from lib.utils.ui import Color, Font

from datetime import datetime

class Widget_Date_Full(CTkFrame):
    def __init__(self, master, mainApp, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
    
        # Variable
        self.mainApp = mainApp
        self.callback = None
        
        # UI
        self.build_ui()
        
        # Function
        self.FixedUpdate()
        
    def FixedUpdate(self):
        self.update_label()
        self.after(1800000, self.FixedUpdate)
    
    def build_ui(self):
        self.configure(fg_color = Color().transparent)
        self.grid_columnconfigure(0, weight = 1, minsize = 300)
        self.grid_rowconfigure(0, weight = 1, minsize = 50)
        
        self.frame_main = CTkFrame(self, fg_color = Color().white)
        self.frame_main.grid(row = 0, column = 0, sticky = NSEW)
        self.frame_main.grid_columnconfigure(0, weight = 1)
        self.frame_main.grid_rowconfigure(0, weight = 1)
        
        self.label_weekday = CTkLabel(self.frame_main, text = "DAY",
                              fg_color = Color().transparent,
                              font = (Font().font_bold, 40),
                              text_color = Color().black)
        self.label_weekday.grid(row = 0, column = 1)
        
        self.label_date = CTkLabel(self.frame_main, text = "DD:MM:YYY",
                              fg_color = Color().transparent,
                              font = (Font().font_bold, 40),
                              text_color = Color().black)
        self.label_date.grid(row = 0, column = 0)
    
    def update_label(self):
        weekday_list = [["Mon", "#FFFF00"], ["Tue", "#FFC0CB"], ["Wed", "#008000"], ["Thu", "#FFA500"], ["Fri", "#0000FF"], ["Sat", "#800080"], ["Sun", "#FF0000"]]
        
        weekday = weekday_list[datetime.today().weekday()]
        date = datetime.now().strftime("%d/%m/%Y")
        
        self.label_date.configure(text = f"{date}")
        self.label_weekday.configure(text = f"{weekday[0]}", text_color = weekday[1])
    
    def set_callback(self, callback):
        self.callback = callback