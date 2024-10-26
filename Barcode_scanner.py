from customtkinter import *
from lib.utils.ui import Color, Font

class MainApp(CTk):
    def __init__(self):
        super().__init__()

        """ Variable """
        self.barcode_text = ""
        self.lastest_barcode_text = ""
        
        """ Screen Setting """
        screen_width = 900 
        screen_height = 900
        self.geometry(f"{screen_width}x{screen_height}+{self.winfo_screenwidth()//2 - screen_width//2}+{self.winfo_screenheight()//2 - screen_height//2}")
        self.resizable(False, False)
        
        set_appearance_mode("Dark")

        self.title("Template")
        
        # UI
        self.build_ui()
        
        self.bind("<Escape>", lambda event : self.exit_application())
        self.bind("<Key>", self.read_barcode_scanner)
    
    def build_ui(self):
        self.configure(fg_color = Color().background)
        
        self.test_frame_barcode = CTkFrame(self, fg_color = Color().transparent)
        self.test_frame_barcode.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        self.test_frame_barcode.grid_rowconfigure((0,1), weight = 0)
        self.test_frame_barcode.grid_columnconfigure(0, weight = 1)
        
        self.label_title = CTkLabel(self.test_frame_barcode, text = "Barcode reader",
                                    fg_color = Color().transparent,
                                    font = (Font().font_bold, 16),)
        self.label_title.grid(row = 0, column = 0, sticky = W)
        
        self.entry_barcode = CTkEntry(self.test_frame_barcode,
                                                width = 400,
                                                corner_radius = 0,
                                                font = (Font().font, 16),
                                                state = "readonly")
        self.entry_barcode.grid(row = 1, column = 0, sticky = EW)

    """ Barcode Scanner"""
    def read_barcode_scanner(self, event):
        if event.keysym != "Return":
            self.barcode_text += event.char
        if event.keysym == "Return":
            # Print scanner text
            self.lastest_barcode_text = self.barcode_text
            
            self.fill_barcode_to_entry(self.barcode_text)
            
            # Command
            if self.barcode_text == "Test":
                # Call function that trigger by TPC/IP Message "test"
                pass
            else:
                # Do nothing or something
                pass
            
            self.barcode_text = ""
    
    def fill_barcode_to_entry(self, text:str):
        self.entry_barcode.configure(state = "normal")
        self.entry_barcode.delete(0, END)
        self.entry_barcode.insert(0, text)
        self.entry_barcode.configure(state = "readonly")

    def exit_application(self):
        self.destroy()

app = MainApp()
app.mainloop()