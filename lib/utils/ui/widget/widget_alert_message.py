from customtkinter import *
from lib.utils.ui import Color, Font
from lib.utils.ui import Thread_Client_Socket

class Widget_Alert_Message(CTkFrame):
    def __init__(self, master, mainApp, client_socket : Thread_Client_Socket, aliveTime : int = 5, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
    
        # Variable
        self.mainApp = mainApp
        self.callback = None
        
        self.alive_time = aliveTime
        self.remain_time = 0
        
        # Setting
        self.widget_width = 300
        self.widget_height = 100
        
        # UI
        self.build_ui()
    
    def build_ui(self):
        self.configure(fg_color = Color().transparent)
        self.grid_columnconfigure(0, weight = 1, minsize = self.widget_width)
        self.grid_rowconfigure(0, weight = 1, minsize = self.widget_height)
        
        self.frame_main = CTkFrame(self, fg_color = Color().green,
                                   corner_radius = 0)
        self.frame_main.grid(row = 0, column = 0, sticky = NSEW)
        self.frame_main.grid_columnconfigure(0, weight = 1)
        self.frame_main.grid_rowconfigure(0, weight = 1)
        
        self.frame_message = CTkFrame(self.frame_main, fg_color = Color().green, corner_radius = 0)
        self.frame_message.grid(row = 0, column = 0, sticky = EW)
        self.frame_message.grid_columnconfigure(0, weight = 1)
        self.frame_message.grid_rowconfigure(0, weight = 0)
        self.frame_message.grid_rowconfigure(1, weight = 0)
        
        self.label_message_title = CTkLabel(self.frame_message, text = "Title",
                                    height = 5,
                                    fg_color = Color().transparent,
                                    font = (Font().font_bold, 14),
                                    text_color = Color().white)
        self.label_message_title.grid(row = 0, column = 0, sticky = W, padx = (10,0))
        
        self.label_message = CTkLabel(self.frame_message, text = "Message",
                                    height = 5,
                                    fg_color = Color().transparent,
                                    font = (Font().font, 14),
                                    text_color = Color().white)
        self.label_message.grid(row = 1, column = 0, sticky = W, padx = (10,0))
    
    def set_callback(self, callback):
        self.callback = callback
    
    def animator_slide_out(self):
        pass
    
    def locomotion(self, stopx : int, stopy : int):
        
        step = 1
        
        posx = int(self.place_info()["x"])
        posy = int(self.place_info()["y"])
        anchor = self.place_info()["anchor"]
        
        self.place(x = posx + 1, y = 0, anchor = NW)
        
        if posx == stopx and posy == stopy:
            return
        
        # self.after(100, lambda : self.locomotion(stopx, stopy))