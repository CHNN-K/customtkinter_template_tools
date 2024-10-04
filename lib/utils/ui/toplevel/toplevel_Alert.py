from customtkinter import *
from lib.utils.ui import Color, Font

from PIL import Image
from enum import Enum

class AlertType(Enum):
    NONE = 0,
    OK = 1,
    WARNING = 2,
    ERROR = 3,
    INFO = 4,
    QUESTION = 5,

class Path_Image:
    def __init__(self):
        self.check = "bin/images/check.png"
        self.question = "bin/images/question.png"
        self.alert_1 = "bin/images/alert_1.png"
        self.alert_2 = "bin/images/alert_2.png"
        self.error_1 = "bin/images/error_1.png"
        self.error_2 = "bin/images/error_2.png"

class Toplevel_Alert(CTkToplevel):
    def __init__(self, master, type : AlertType = AlertType.NONE, aliveTime : int = 3, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        # Variable
        self.alertType = type
        self.autoCloseTime = aliveTime  # Second
        
        # Setting
        self.attributes("-topmost", True)  # Always on top
        
        screen_width = 400
        screen_height = 200
        self.geometry(f"{screen_width}x{screen_height}+{960-int(screen_width/2)}+{540-int(screen_height/2)}")
        
        self.title("Alert")
        
        self.resizable(False,False)
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.window_exit_btn_callback)
        
        """ Main """
        self.build_ui()
        self.insertImage()

    def build_ui(self):
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        self.configure(fg_color = Color().background)
        
        self.frame_main = CTkFrame(self, fg_color = Color().transparent)
        self.frame_main.grid_rowconfigure(0, weight = 3)
        self.frame_main.grid_rowconfigure(1, weight = 1)
        self.frame_main.grid_columnconfigure(0, weight = 1)
        self.frame_main.grid(row = 0, column = 0, sticky = NSEW)

        self.frame_text = CTkFrame(self.frame_main, fg_color = Color().background,
                                  corner_radius = 0)
        self.frame_text.grid_rowconfigure(0, weight = 1)
        self.frame_text.grid_columnconfigure(0, weight = 0)
        self.frame_text.grid_columnconfigure(1, weight = 0, minsize = 20)
        self.frame_text.grid_columnconfigure(2, weight = 1)
        self.frame_text.grid(row = 0, column = 0)

        self.image_alert = CTkLabel(self.frame_text, text = "",
                                    font = (Font().font_bold, 14),
                                    text_color = Color().black)
        self.image_alert.grid(row = 0, column = 0)
        
        self.frame_alert_status = CTkFrame(self.frame_text, fg_color = Color().transparent,
                                    corner_radius = 0)
        self.frame_alert_status.grid_rowconfigure(0, weight = 0)
        self.frame_alert_status.grid_rowconfigure(1, weight = 1)
        self.frame_alert_status.grid_columnconfigure(0, weight = 1)
        self.frame_alert_status.grid(row = 0, column = 2, sticky = W)
        
        self.label_alert_status = CTkLabel(self.frame_alert_status, text = "Status",
                                        height = 0,
                                        font = (Font().font_bold, 16),
                                        text_color = Color().black)
        self.label_alert_status.grid(row = 0, column = 0, sticky = W)
        
        self.label_alert_detail = CTkLabel(self.frame_alert_status, text =  "Detail",
                                        height = 0,
                                        font = (Font().font, 16),
                                        text_color = Color().black,
                                        wraplength = 250)
        self.label_alert_detail.grid(row = 1, column = 0, sticky = W)
        
        self.frame_btn = CTkFrame(self.frame_main, fg_color = Color().background_body,
                                  corner_radius = 0)
        self.frame_btn.grid_rowconfigure(0, weight = 1)
        self.frame_btn.grid_columnconfigure(0, weight = 1)
        self.frame_btn.grid(row = 1, column = 0, sticky = NSEW)
        
        self.btn_1 = CTkButton(self.frame_btn, text = "Button 1",
                            fg_color = Color().white,
                            hover_color = Color().darker_color(Color().white, 20),
                            corner_radius = 0,
                            font = (Font().font_bold, 18),
                            text_color = Color().black)
        self.btn_1.grid(row = 0, column = 0)
        
        self.label_timer = CTkLabel(self, text = "Close in 3...", 
                              font = (Font().font, 16),
                              text_color = Color().yellow)
        self.label_timer.grid(row = 0, column = 0, sticky = S)
        self.label_timer.grid_remove()
    
    def set_header(self, text : str):
        self.label_alert_status.configure(text = text)
    
    def set_detail(self, text : str):
        self.label_alert_detail.configure(text = text)
        
    def insertImage(self):
        if self.alertType == AlertType.NONE:
            image_path = Path_Image().question
        elif self.alertType == AlertType.OK:
            image_path = Path_Image().check
        elif self.alertType == AlertType.ERROR:
            image_path = Path_Image().error_1
        elif self.alertType == AlertType.WARNING:
            image_path = Path_Image().alert_2
            
        try:
            self.image_alert.configure(image = CTkImage(Image.open(image_path), size = (64, 64)))
        except:
            self.image_alert.configure(text = "Image")
    
    def bringToTop(self):
        self.after(100, lambda: self.attributes("-topmost", True))
        self.after(400, lambda: self.attributes("-topmost", False))
    
    def autoCloseWindow(self, aliveTime):
        if (aliveTime == -1):
            self.label_timer.grid_remove()
            return
        
        if (self.autoCloseTime <= 0):
            self.close_toplevel()
            return
        
        self.label_timer.configure(text = f"Close in {self.autoCloseTime}...")
        self.autoCloseTime -= 1
        self.after(1000, lambda : self.autoCloseWindow(aliveTime))

    def close_toplevel(self):
        self.destroy()

    def window_exit_btn_callback(self):
        self.destroy()