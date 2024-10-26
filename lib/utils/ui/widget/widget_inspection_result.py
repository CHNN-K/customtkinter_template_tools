from customtkinter import *
from lib.utils import Result
from lib.utils.ui import Color, Font

class Widget_Insepction_Result(CTkFrame):
    def __init__(self, master, mainApp, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
    
        # Variable
        self.mainApp = mainApp
        self.callback = None
        
        # Setting
        self.widget_width = 380
        self.widget_height = 210
        
        # UI
        self.build_ui()
        
    def FixedUpdate(self):
        self.after(50, self.FixedUpdate)
    
    def build_ui(self):
        self.configure(fg_color = Color().transparent)
        self.grid_columnconfigure(0, weight = 1, minsize = self.widget_width )
        self.grid_rowconfigure(0, weight = 1, minsize = self.widget_height)
        
        self.frame_main = CTkFrame(self, fg_color = Color().widget_background)
        self.frame_main.grid(row = 0, column = 0, sticky = NSEW)
        self.frame_main.grid_columnconfigure(0, weight = 1)
        self.frame_main.grid_rowconfigure(0, weight = 0)
        self.frame_main.grid_rowconfigure(1, weight = 1)
        
        self.label_title = CTkLabel(self.frame_main, text = "Inspection Result",
                              fg_color = Color().transparent,
                              font = (Font().font_bold, 36),
                              text_color = Color().black)
        self.label_title.grid(row = 0, column = 0)
        
        self.frame_body = CTkFrame(self.frame_main, fg_color = Color().white)
        self.frame_body.grid(row = 1, column = 0, padx = 10, pady = (0,10), sticky = NSEW)
        self.frame_body.grid_columnconfigure(0, weight = 1)
        self.frame_body.grid_rowconfigure(0, weight = 1)
        
        self.label_inspection_result = CTkLabel(self.frame_body, text = "Result",
                                    fg_color = Color().transparent,
                                    font = (Font().font_bold, 96),
                                    text_color = Color().black)
        self.label_inspection_result.grid(row = 0, column = 0)
    
    def update_label(self, result : Result):
        
        def changeColor(color : Color):
            self.frame_main.configure(fg_color = color)
            self.label_title.configure(text_color = Color().white)
            self.label_inspection_result.configure(text_color = color)
        
        if result == Result.OK:
            changeColor(Color().green)
        
        elif result == Result.NG:
            changeColor(Color().red)
        
        elif result == Result.ERROR:
            changeColor(Color().orange)
        
        else:
            self.frame_main.configure(fg_color = Color().widget_background)
            self.label_title.configure(text_color = Color().black)
            self.label_inspection_result.configure(text_color = Color().black)
            pass
        
        self.label_inspection_result.configure(text = result.name)
    
    def set_callback(self, callback):
        self.callback = callback