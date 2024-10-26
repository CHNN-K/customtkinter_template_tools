from customtkinter import *
from lib.utils.ui import Color, Font

class Widget_Part_Detail(CTkFrame):
    def __init__(self, master, mainApp, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
    
        # Variable
        self.mainApp = mainApp
        self.callback = None
        
        # Setting
        self.widget_width = 610
        self.widget_height = 210
        
        # UI
        self.build_ui()
        
    def FixedUpdate(self):
        self.after(50, self.FixedUpdate)
    
    def build_ui(self):
        self.configure(fg_color = Color().transparent)
        self.grid_columnconfigure(0, weight = 1, minsize = self.widget_width)
        self.grid_rowconfigure(0, weight = 1, minsize = self.widget_height)
        
        self.frame_main = CTkFrame(self, fg_color = Color().widget_background)
        self.frame_main.grid(row = 0, column = 0, sticky = NSEW)
        self.frame_main.grid_columnconfigure(0, weight = 1)
        self.frame_main.grid_rowconfigure(0, weight = 1)
        self.frame_main.grid_rowconfigure(1, weight = 1)
        self.frame_main.grid_rowconfigure(2, weight = 0, minsize = 10)
        
        """ Part Number """
        self.frame_part_number = CTkFrame(self.frame_main, fg_color = Color().widget_background, corner_radius = 0)
        self.frame_part_number.grid(row = 0, column = 0, padx = 10, sticky = EW)
        self.frame_part_number.grid_columnconfigure(0, weight = 1)
        self.frame_part_number.grid_rowconfigure(0, weight = 0)
        self.frame_part_number.grid_rowconfigure(1, weight = 1)
        
        self.label_part_number_title = CTkLabel(self.frame_part_number, text = "Part Number",
                                                fg_color = Color().transparent,
                                                font = (Font().font_bold, 36),
                                                text_color = Color().black)
        self.label_part_number_title.grid(row = 0, column = 0, sticky = W)
        
        self.frame_part_number_body = CTkFrame(self.frame_part_number, fg_color = Color().white)
        self.frame_part_number_body.grid(row = 1, column = 0, sticky = EW)
        self.frame_part_number_body.grid_columnconfigure(0, weight = 1)
        self.frame_part_number_body.grid_rowconfigure(0, weight = 1, minsize = 50)
        
        self.label_part_number = CTkLabel(self.frame_part_number_body, text = "XXXXXX-XXXXX-XX",
                                    fg_color = Color().transparent,
                                    font = (Font().font_bold, 40),
                                    text_color = Color().black)
        self.label_part_number.grid(row = 0, column = 0, padx = (10,0), sticky = W)
        
        """ Part XX """
        self.frame_part_xx = CTkFrame(self.frame_main, fg_color = Color().widget_background, corner_radius = 0)
        self.frame_part_xx.grid(row = 1, column = 0, padx = 10, sticky = EW)
        self.frame_part_xx.grid_columnconfigure(0, weight = 1)
        self.frame_part_xx.grid_rowconfigure(0, weight = 0)
        self.frame_part_xx.grid_rowconfigure(1, weight = 1)
        
        self.label_part_xx_title = CTkLabel(self.frame_part_xx, text = "Part XX",
                                                fg_color = Color().transparent,
                                                font = (Font().font_bold, 36),
                                                text_color = Color().black)
        self.label_part_xx_title.grid(row = 0, column = 0, sticky = W)
        
        self.frame_part_xx_body = CTkFrame(self.frame_part_xx, fg_color = Color().white)
        self.frame_part_xx_body.grid(row = 1, column = 0, sticky = EW)
        self.frame_part_xx_body.grid_columnconfigure(0, weight = 1)
        self.frame_part_xx_body.grid_rowconfigure(0, weight = 1, minsize = 50)
        
        self.label_part_xx = CTkLabel(self.frame_part_xx_body, text = "####################",
                                    fg_color = Color().transparent,
                                    font = (Font().font_bold, 40),
                                    text_color = Color().black)
        self.label_part_xx.grid(row = 0, column = 0, padx = (10,0), sticky = W)
    
    def update_label(self, part_number : str, part_xx : str):
        self.label_part_number.configure(text = part_number)
        self.label_part_xx.configure(text = part_xx)
    
    def set_callback(self, callback):
        self.callback = callback