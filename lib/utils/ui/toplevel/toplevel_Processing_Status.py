from customtkinter import *
from lib.utils.ui import Color, Font

class Toplevel_Processing_Status(CTkToplevel):
    def __init__(self, master, aliveTime : int, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        # Variable
        self.autoCloseTime = aliveTime  # Second
        
        # Setting
        self.attributes("-topmost", True)  # Always on top
        
        screen_width = 400
        screen_height = 250
        self.geometry(f"{screen_width}x{screen_height}+{960-int(screen_width/2)}+{540-int(screen_height/2)}")
        
        self.title("Process Status")
        
        self.resizable(False,False)
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.window_exit_btn_callback)
        
        """ Main """
        self.build_ui()
        self.animateProcessText()

    def build_ui(self):
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        self.configure(fg_color = Color().yellow)
        
        self.frame_main = CTkFrame(self, fg_color = Color().transparent)
        self.frame_main.grid_rowconfigure((0,1), weight = 1)
        self.frame_main.grid_columnconfigure(0, weight = 1)
        self.frame_main.grid(row = 0, column = 0)

        self.frame_text = CTkFrame(self.frame_main, fg_color = Color().transparent)
        self.frame_text.grid_rowconfigure((0,1), weight = 0)
        self.frame_text.grid_columnconfigure(0, weight = 1)
        self.frame_text.grid(row = 0, column = 0)

        self.label_status = CTkLabel(self.frame_text, text = "Processing...", 
                              font = (Font().font_bold, 36),
                              text_color = Color().black)
        self.label_status.grid(row = 0, column = 0)
        
        self.label_timer = CTkLabel(self.frame_text, text = "Close in 3...", 
                              font = (Font().font, 16),
                              text_color = Color().yellow)
        self.label_timer.grid(row = 1, column = 0)
        self.label_timer.grid_remove()
    
    def bringToTop(self):
        self.after(100, lambda: self.attributes("-topmost", True))
        self.after(400, lambda: self.attributes("-topmost", False))
    
    def processFinish_callback(self):
        self.after_cancel(self.process_animation_text)
        
        self.configure(fg_color = Color().green)
        self.label_status.configure(text = "Finish", text_color = Color().white)
        self.label_timer.grid()
        self.autoCloseWindow(self.autoCloseTime)
        
    def animateProcessText(self):
        if self.label_status.cget("text") == "Processing":
            self.label_status.configure(text = "Processing.")
        elif self.label_status.cget("text") == "Processing.":
            self.label_status.configure(text = "Processing..")
        elif self.label_status.cget("text") == "Processing..":
            self.label_status.configure(text = "Processing...")
        elif self.label_status.cget("text") == "Processing...":
            self.label_status.configure(text = "Processing")
        self.process_animation_text = self.after(500, self.animateProcessText)
    
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