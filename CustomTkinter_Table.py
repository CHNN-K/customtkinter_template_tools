from customtkinter import *
from enum import Enum

class Row_Type(Enum):
    Header = 1,
    Body = 2

class Font:
    def __init__(self):
        self.font = "Franklin Gothic Medium"
        self.font_bold = "Franklin Gothic Heavy"

class Color:
    def __init__(self):
        self.background = "#D9D9D9"
        self.background_frame = "#909090"
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
        deactivate_automatic_dpi_awareness()

        self.title("Template")
        
        self.bind("<Escape>", lambda event : self.destroy())

        # UI
        self.build_ui()
        
        # Function
        self.FixedUpdate()
    
    def FixedUpdate(self):
        self.after(10, self.FixedUpdate)
    
    def build_ui(self):
        self.configure(fg_color = Color().black)
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)
        
        self.frame_center = CTkFrame(self, fg_color = Color().transparent)
        self.frame_center.grid(row = 0, column = 0)
        self.frame_center.grid_columnconfigure(0, weight = 1)
        
        self.label_starter = CTkLabel(self.frame_center, text = "Custom tkinter Table",
                                      font = (Font().font_bold, 20))
        self.label_starter.grid(row = 0, column = 0)
        
        self.btn_open_toplevel_table = CTkButton(self.frame_center, text = "Table", command = self.btn_open_toplevel_table_callback)
        self.btn_open_toplevel_table.grid(row = 1, column = 0)
    
    def btn_open_toplevel_table_callback(self):
        self.toplevel_table = Toplevel_Table(self, self)

class Toplevel_Table(CTkToplevel):
    def __init__(self, master, mainApp : MainApp, *args,**kwargs):
        super().__init__(master, *args, **kwargs)
        
        """ Variable """
        self.mainApp = mainApp
        
        """ Setting """
        self.attributes("-topmost", False)  # Always on top
        
        screen_width = 1090
        screen_height = 560
        self.geometry(f"{screen_width}x{screen_height}+{self.winfo_screenwidth()//2 - screen_width//2}+{self.winfo_screenheight()//2 - screen_height//2}")
        
        self.title("History")
        
        self.resizable(False, False)
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.window_exit_btn_callback)
        
        self.build_ui()
        self.bringToTop()

    def build_ui(self):
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        self.configure(fg_color = Color().background)
        
        self.frame_main = CTkFrame(self, fg_color = Color().background)
        self.frame_main.grid_rowconfigure(0, weight = 0)
        self.frame_main.grid_rowconfigure(1, weight = 1)
        self.frame_main.grid_columnconfigure(0, weight = 1)
        self.frame_main.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = NSEW)
        
        self.label_title = CTkLabel(self.frame_main, text = "Inspection History",
                                    fg_color = Color().background,
                                    font = (Font().font_bold, 28),
                                    text_color = Color().black)
        self.label_title.grid(row = 0, column = 0, sticky = EW)
        
        self.frame_table = CTkFrame(self.frame_main, fg_color = Color().background)
        self.frame_table.grid(row = 1, column = 0, sticky = NSEW)
        self.frame_table.grid_columnconfigure(0, weight = 1)
        self.frame_table.grid_rowconfigure(0, weight = 0)
        self.frame_table.grid_rowconfigure(1, weight = 1)
        
        self.frame_table_header = CTkFrame(self.frame_table, fg_color = Color().background)
        self.frame_table_header.grid(row = 0, column = 0, sticky = EW)
        self.frame_table_header.grid_columnconfigure(0, weight = 1)
        
        self.table_header = Table_Row_History(self.frame_table_header, Row_Type.Header)
        self.table_header.grid(row = 0, column = 0, sticky = EW)
        
        self.frame_table_body = CTkScrollableFrame(self.frame_table, fg_color = Color().background_frame,
                                                   corner_radius = 0)
        self.frame_table_body._scrollbar.grid_remove()
        self.frame_table_body.grid(row = 1, column = 0, sticky = NSEW)
        self.frame_table_body.grid_columnconfigure(0, weight = 1)
        
        for i in range(0, 30):
            row = Table_Row_History(self.frame_table_body)
            row.grid(row = i, column = 0, sticky = EW)
    
    def bringToTop(self):
        self.after(100, lambda: self.attributes("-topmost", True))
        self.after(500, lambda: self.attributes("-topmost", False))
    
    def window_exit_btn_callback(self):
        self.destroy()

class Table_Row_History(CTkFrame):
    def __init__(self, master, rowType : Row_Type = Row_Type.Body, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.rowType = rowType
        
        self.tableColor = Color().white
        self.borderColor = Color().black
        self.borderWidth = 2
        self.textColor = Color().black
        self.cellHeight = 40
        
        self.font = (Font().font_bold, 20) if self.rowType == Row_Type.Header else (Font().font, 20)
        
        self.build_ui()
        self.setup_header()
        self.insert_body()
        
    def build_ui(self):
        self.configure(fg_color = Color().transparent)
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        self.grid_configure(sticky = EW)
        
        self.frame_main = CTkFrame(self, fg_color = Color().transparent)
        self.frame_main.grid(row = 0, column = 0, sticky = EW)
        self.frame_main.grid_columnconfigure(0, weight = 0, minsize = 75)
        self.frame_main.grid_columnconfigure(1, weight = 1)
        self.frame_main.grid_columnconfigure(2, weight = 0, minsize = 150)
        self.frame_main.grid_columnconfigure(3, weight = 0, minsize = 150)
        self.frame_main.grid_columnconfigure(4, weight = 0, minsize = 150)
        self.frame_main.grid_columnconfigure(5, weight = 0, minsize = 75)
        self.frame_main.grid_columnconfigure(6, weight = 0, minsize = 75)
        self.frame_main.grid_rowconfigure(0, weight = 1)
        
        self.frame_cell_number = CTkFrame(self.frame_main, fg_color = self.tableColor,
                                          border_color = self.borderColor,
                                          border_width = self.borderWidth,
                                          corner_radius = 0)
        self.frame_cell_number.grid(row = 0, column = 0, ipadx = self.borderWidth, ipady = self.borderWidth * 2, sticky = EW)
        self.frame_cell_number.grid_columnconfigure(0, weight = 1)
        self.frame_cell_number.grid_rowconfigure(0, weight = 1)
        self.frame_cell_number.bind("<Enter>", self.event_highlight_row)
        self.frame_cell_number.bind("<Leave>", self.event_unhighlight_row)
        
        self.cell_number = CTkLabel(self.frame_cell_number, text = "No.",
                                fg_color = self.tableColor,
                                height = self.cellHeight,
                                corner_radius = 0,
                                font = self.font,
                                text_color = self.textColor,
                                justify = CENTER)
        self.cell_number.grid(row = 0, column = 0, padx = self.borderWidth, sticky = EW)
        self.cell_number.bind("<Enter>", self.event_highlight_row)
        self.cell_number.bind("<Leave>", self.event_unhighlight_row)
        
        self.frame_cell_partNumber = CTkFrame(self.frame_main, fg_color = self.tableColor,
                                          border_color = self.borderColor,
                                          border_width = 2,
                                          corner_radius = 0)
        self.frame_cell_partNumber.grid(row = 0, column = 1, ipadx = self.borderWidth, ipady = self.borderWidth * 2, sticky = EW)
        self.frame_cell_partNumber.grid_columnconfigure(0, weight = 1)
        self.frame_cell_partNumber.grid_rowconfigure(0, weight = 1)
        self.frame_cell_partNumber.bind("<Enter>", self.event_highlight_row)
        self.frame_cell_partNumber.bind("<Leave>", self.event_unhighlight_row)
        
        self.cell_partNumber = CTkLabel(self.frame_cell_partNumber, text = "Part Number",
                                fg_color = self.tableColor,
                                height = self.cellHeight,
                                corner_radius = 0,
                                font = self.font,
                                text_color = self.textColor,
                                justify = CENTER)
        self.cell_partNumber.grid(row = 0, column = 0, padx = self.borderWidth)
        self.cell_partNumber.bind("<Enter>", self.event_highlight_row)
        self.cell_partNumber.bind("<Leave>", self.event_unhighlight_row)
        
        self.frame_cell_partID = CTkFrame(self.frame_main, fg_color = self.tableColor,
                                          border_color = self.borderColor,
                                          border_width = 2,
                                          corner_radius = 0)
        self.frame_cell_partID.grid(row = 0, column = 2, ipadx = self.borderWidth, ipady = self.borderWidth * 2, sticky = EW)
        self.frame_cell_partID.grid_columnconfigure(0, weight = 1)
        self.frame_cell_partID.grid_rowconfigure(0, weight = 1)
        self.frame_cell_partID.bind("<Enter>", self.event_highlight_row)
        self.frame_cell_partID.bind("<Leave>", self.event_unhighlight_row)
        
        
        self.cell_partID = CTkLabel(self.frame_cell_partID, text = "Part ID",
                                fg_color = self.tableColor,
                                height = self.cellHeight,
                                corner_radius = 0,
                                font = self.font,
                                text_color = self.textColor,
                                justify = CENTER)
        self.cell_partID.grid(row = 0, column = 0)
        self.cell_partID.bind("<Enter>", self.event_highlight_row)
        self.cell_partID.bind("<Leave>", self.event_unhighlight_row)
        
        self.frame_cell_side = CTkFrame(self.frame_main, fg_color = self.tableColor,
                                          border_color = self.borderColor,
                                          border_width = 2,
                                          corner_radius = 0)
        self.frame_cell_side.grid(row = 0, column = 3, ipadx = self.borderWidth, ipady = self.borderWidth * 2, sticky = EW)
        self.frame_cell_side.grid_columnconfigure(0, weight = 1)
        self.frame_cell_side.grid_rowconfigure(0, weight = 1)
        self.frame_cell_side.bind("<Enter>", self.event_highlight_row)
        self.frame_cell_side.bind("<Leave>", self.event_unhighlight_row)
        
        self.cell_side = CTkLabel(self.frame_cell_side, text = "Part Side",
                                fg_color = self.tableColor,
                                height = self.cellHeight,
                                corner_radius = 0,
                                font = self.font,
                                text_color = self.textColor,
                                justify = CENTER)
        self.cell_side.grid(row = 0, column = 0)
        self.cell_side.bind("<Enter>", self.event_highlight_row)
        self.cell_side.bind("<Leave>", self.event_unhighlight_row)
        
        self.frame_cell_time = CTkFrame(self.frame_main, fg_color = self.tableColor,
                                          border_color = self.borderColor,
                                          border_width = 2,
                                          corner_radius = 0)
        self.frame_cell_time.grid(row = 0, column = 4, ipadx = self.borderWidth, ipady = self.borderWidth * 2, sticky = EW)
        self.frame_cell_time.grid_columnconfigure(0, weight = 1)
        self.frame_cell_time.grid_rowconfigure(0, weight = 1)
        self.frame_cell_time.bind("<Enter>", self.event_highlight_row)
        self.frame_cell_time.bind("<Leave>", self.event_unhighlight_row)
        
        self.cell_time = CTkLabel(self.frame_cell_time, text = "Time",
                                fg_color = self.tableColor,
                                height = self.cellHeight,
                                corner_radius = 0,
                                font = self.font,
                                text_color = self.textColor,
                                justify = CENTER)
        self.cell_time.grid(row = 0, column = 0)
        self.cell_time.bind("<Enter>", self.event_highlight_row)
        self.cell_time.bind("<Leave>", self.event_unhighlight_row)
        
        self.frame_cell_result = CTkFrame(self.frame_main, fg_color = self.tableColor,
                                          border_color = self.borderColor,
                                          border_width = 2,
                                          corner_radius = 0)
        self.frame_cell_result.grid(row = 0, column = 5, ipadx = self.borderWidth, ipady = self.borderWidth * 2, sticky = EW)
        self.frame_cell_result.grid_columnconfigure(0, weight = 1)
        self.frame_cell_result.grid_rowconfigure(0, weight = 1)
        self.frame_cell_result.bind("<Enter>", self.event_highlight_row)
        self.frame_cell_result.bind("<Leave>", self.event_unhighlight_row)
        
        self.cell_result = CTkLabel(self.frame_cell_result, text = "Result",
                                fg_color = self.tableColor,
                                height = self.cellHeight,
                                corner_radius = 0,
                                font = self.font,
                                text_color = self.textColor,
                                justify = CENTER)
        self.cell_result.grid(row = 0, column = 0)
        self.cell_result.bind("<Enter>", self.event_highlight_row)
        self.cell_result.bind("<Leave>", self.event_unhighlight_row)
        
        self.frame_cell_view = CTkFrame(self.frame_main, fg_color = self.tableColor,
                                          border_color = self.borderColor,
                                          border_width = 2,
                                          corner_radius = 0)
        self.frame_cell_view.grid(row = 0, column = 6, ipadx = self.borderWidth, ipady = self.borderWidth * 2, sticky = EW)
        self.frame_cell_view.grid_columnconfigure(0, weight = 1)
        self.frame_cell_view.grid_rowconfigure(0, weight = 1)
        self.frame_cell_view.bind("<Enter>", self.event_highlight_row)
        self.frame_cell_view.bind("<Leave>", self.event_unhighlight_row)
        
        self.cell_view = CTkLabel(self.frame_cell_view, text = "🧾",
                                fg_color = self.tableColor,
                                height = self.cellHeight,
                                corner_radius = 0,
                                font = self.font,
                                text_color = self.textColor,
                                cursor = "hand2",
                                justify = CENTER)
        self.cell_view.grid(row = 0, column = 0)
        self.cell_view.bind("<Button-1>", self.event_view_detail)
        self.cell_view.bind("<Enter>", self.event_highlight_row)
        self.cell_view.bind("<Leave>", self.event_unhighlight_row)
    
    def event_highlight_row(self, event):
        self.frame_cell_number.configure(fg_color = Color().yellow)
        self.frame_cell_partNumber.configure(fg_color = Color().yellow)
        self.frame_cell_partID.configure(fg_color = Color().yellow)
        self.frame_cell_side.configure(fg_color = Color().yellow)
        self.frame_cell_time.configure(fg_color = Color().yellow)
        
        self.cell_number.configure(fg_color = Color().yellow)
        self.cell_partNumber.configure(fg_color = Color().yellow)
        self.cell_partID.configure(fg_color = Color().yellow)
        self.cell_side.configure(fg_color = Color().yellow)
        self.cell_time.configure(fg_color = Color().yellow)
        
    def event_unhighlight_row(self, event):
        self.frame_cell_number.configure(fg_color = Color().white)
        self.frame_cell_partNumber.configure(fg_color = Color().white)
        self.frame_cell_partID.configure(fg_color = Color().white)
        self.frame_cell_side.configure(fg_color = Color().white)
        self.frame_cell_time.configure(fg_color = Color().white)
        
        self.cell_number.configure(fg_color = Color().white)
        self.cell_partNumber.configure(fg_color = Color().white)
        self.cell_partID.configure(fg_color = Color().white)
        self.cell_side.configure(fg_color = Color().white)
        self.cell_time.configure(fg_color = Color().white)
    
    def event_view_detail(self, event):
        print("View Detail")
    
    def setup_header(self):
        if not self.rowType == Row_Type.Header:
            return
        
        self.cell_view.configure(text = "View")
        
        self.cell_view.unbind("<Button-1>")
        self.cell_view.configure(cursor = "arrow")
        
        self.frame_cell_number.unbind("<Enter>")
        self.frame_cell_number.unbind("<Leave>")
        self.cell_number.unbind("<Enter>")
        self.cell_number.unbind("<Leave>")
        self.frame_cell_partNumber.unbind("<Enter>")
        self.frame_cell_partNumber.unbind("<Leave>")
        self.cell_partNumber.unbind("<Enter>")
        self.cell_partNumber.unbind("<Leave>")
        self.frame_cell_partID.unbind("<Enter>")
        self.frame_cell_partID.unbind("<Leave>")
        self.cell_partID.unbind("<Enter>")
        self.cell_partID.unbind("<Leave>")
        self.frame_cell_side.unbind("<Enter>")
        self.frame_cell_side.unbind("<Leave>")
        self.cell_side.unbind("<Enter>")
        self.cell_side.unbind("<Leave>")
        self.frame_cell_time.unbind("<Enter>")
        self.frame_cell_time.unbind("<Leave>")
        self.cell_time.unbind("<Enter>")
        self.cell_time.unbind("<Leave>")
    
    def insert_body(self):
        if not self.rowType == Row_Type.Body:
            return
        
        print("Insert Body")

app = MainApp()
app.mainloop()