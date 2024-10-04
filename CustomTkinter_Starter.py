from customtkinter import *

class Font:
    def __init__(self):
        self.font = "Franklin Gothic Medium"
        self.font_bold = "Franklin Gothic Heavy"

class Color:
    def __init__(self):
        self.background = "#2A2A2A"
        self.background_frame = "#181717"
        self.white = "#F2F2F2"
        self.red = "#C00000"
        self.green = "#00B050"
        self.blue = "#0078D4"
        self.black = "#0D0D0D"
        self.pink = "#F24171"
        self.gray = "#424242"
        self.yellow = "#FFDE21"
        self.darkblue = "#000080"
        self.orange = "#FFA500"
        
        self.transparent = "transparent"
        self.disable = "#626262"

class MainApp(CTk):
    def __init__(self):
        super().__init__()

        """ Variable """
        
        """ Screen Setting """
        screen_width = 1600 
        screen_height = 900
        self.geometry(f"{screen_width}x{screen_height}+{self.winfo_screenwidth()//2 - screen_width//2}+{self.winfo_screenheight()//2 - screen_height//2}")
        self.resizable(False, False)
        
        set_appearance_mode("Dark")

        self.title("Template")
        
        self.bind("<Escape>", lambda event : self.destroy())

        # UI
        self.build_ui()
        
        # Function
        self.FixedUpdate()
    
    def FixedUpdate(self):
        self.after(10, self.FixedUpdate)
    
    def build_ui(self):
        self.configure(fg_color = Color().background)
        
        self.label_starter = CTkLabel(self, text = "Custom tkinter starter pack",
                                      font = (Font().font_bold, 20))
        self.label_starter.place(relx = 0.5, rely = 0.5, anchor = CENTER)

app = MainApp()
app.mainloop()