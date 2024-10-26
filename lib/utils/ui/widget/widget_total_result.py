from customtkinter import *
from lib.utils import Result
from lib.utils.ui import Color, Font

class Widget_Total_Result(CTkFrame):
    def __init__(self, master, mainApp, resultType : Result = None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
    
        # Variable
        self.mainApp = mainApp
        self.resultType = resultType
        self.callback = None
        
        # Setting
        self.widget_width = 180
        self.widget_height = 180
        
        # UI
        self.build_ui()
        self.change_widget_color()
        
    def FixedUpdate(self):
        self.after(50, self.FixedUpdate)
    
    def build_ui(self):
        self.configure(fg_color = Color().transparent)
        self.grid_columnconfigure(0, weight = 1, minsize = self.widget_width)
        self.grid_rowconfigure(0, weight = 1, minsize = self.widget_height)
        
        self.frame_main = CTkFrame(self, fg_color = Color().widget_background)
        self.frame_main.grid(row = 0, column = 0, sticky = NSEW)
        self.frame_main.grid_columnconfigure(0, weight = 1)
        self.frame_main.grid_rowconfigure(0, weight = 0)
        self.frame_main.grid_rowconfigure(1, weight = 1)
        
        self.label_title = CTkLabel(self.frame_main, text = "Total",
                              fg_color = Color().transparent,
                              font = (Font().font_bold, 36),
                              text_color = Color().black)
        self.label_title.grid(row = 0, column = 0)
        
        self.frame_body = CTkFrame(self.frame_main, fg_color = Color().white)
        self.frame_body.grid(row = 1, column = 0, padx = 10, pady = (0,10), sticky = NSEW)
        self.frame_body.grid_columnconfigure(0, weight = 1)
        self.frame_body.grid_rowconfigure(0, weight = 1)
        
        self.label_total = CTkLabel(self.frame_body, text = "999",
                                    fg_color = Color().transparent,
                                    font = (Font().font_bold, 64),
                                    text_color = Color().black)
        self.label_total.grid(row = 0, column = 0)
        
        self.label_unit = CTkLabel(self.frame_body, text = "Pcs.",
                                    fg_color = Color().transparent,
                                    font = (Font().font_bold, 20),
                                    text_color = Color().black)
        self.label_unit.grid(row = 0, column = 0, padx = 5, sticky = SE)
    
    def change_widget_color(self):
        def changeColor(color : Color):
            self.frame_main.configure(fg_color = color)
            self.label_title.configure(text_color = Color().white)
            self.label_total.configure(text_color = color)
        
        def changeLabel(text : str):
            self.label_title.configure(text = f"{text}")
            self.label_total.configure(text = f"{0}")
            
        if self.resultType == Result.OK:
            changeLabel(Result.OK.name)
            changeColor(Color().green)
            
        elif self.resultType == Result.NG:
            changeLabel(Result.NG.name)
            changeColor(Color().red)
        
        elif self.resultType == None:
            changeLabel("Total")
        
        else:
            pass
        
    def update_label(self, total : int):
        self.label_total.configure(text = f"{total}")
    
    def set_callback(self, callback):
        self.callback = callback