from customtkinter import *
from lib.utils.ui import *

class MainApp(CTk):
    def __init__(self):
        super().__init__()

        """ Variable """
        
        """ Screen Setting """
        screen_width = 1600 
        screen_height = 900
        self.geometry(f"{screen_width}x{screen_height}+{self.winfo_screenwidth()//2 - screen_width//2}+{self.winfo_screenheight()//2 - screen_height//2}")
        self.resizable(False, False)
        
        set_appearance_mode("Light")
        deactivate_automatic_dpi_awareness()

        self.title("Template")
        
        self.bind("<Escape>", lambda event : self.destroy())

        # UI
        self.build_ui()
        self.toplevel_processing = Toplevel_Processing_Status(self, 3)
        
        self.toplevel_alert = Toplevel_Alert(self, AlertType.ERROR)
        self.toplevel_alert.set_header("Not Found")
        self.toplevel_alert.set_detail("Can't find Robot_path_1.rbp file")
        
        # Function
        self.FixedUpdate()
    
    def FixedUpdate(self):
        self.after(10, self.FixedUpdate)
    
    def build_ui(self):
        self.configure(fg_color = Color().background)
        
        self.label_starter = CTkLabel(self, text = "Custom tkinter starter pack",
                                      font = (Font().font_bold, 20),
                                      text_color = Color().black)
        self.label_starter.place(relx = 0.5, rely = 0.5, anchor = CENTER)

app = MainApp()
app.mainloop()