from customtkinter import *
from lib.utils.ui import Color, Font

class Animate_Processing(CTkFrame):
    def __init__(self, master, mainApp, aliveTime : int, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
    
        # Variable
        self.mainApp = mainApp
        self.callback = None
        
        self.autoCloseTime = aliveTime  # Second
        
        # Setting
        self.widget_width = 400
        self.widget_height = 250
        
        # UI
        self.build_ui()
        self.animateProcessText()
        self.grab_set()
    
    def build_ui(self):
        self.grid_columnconfigure(0, weight = 1, minsize = self.widget_width)
        self.grid_rowconfigure(0, weight = 1, minsize = self.widget_height)
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
            self.close_widget()
            return
        
        self.label_timer.configure(text = f"Close in {self.autoCloseTime}...")
        self.autoCloseTime -= 1
        self.after(1000, lambda : self.autoCloseWindow(aliveTime))
    
    def set_callback(self, callback):
        self.callback = callback
    
    def close_widget(self):
        self.grab_release()
        self.destroy()