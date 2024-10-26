from customtkinter import *
from lib.utils import Result
from lib.utils.ui import Color, Font

class Toplevel_Inspection_History(CTkToplevel):
    def __init__(self, master, mainApp, *args,**kwargs):
        super().__init__(master, *args, **kwargs)
        
        # Variable
        self.mainApp = mainApp
        self.callback = None
        
        self.total_table_row = 0
        self.list_table_row = []
        
        # Setting
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
        self.configure(fg_color = Color().toplevel_background)
        
        self.frame_main = CTkFrame(self, fg_color = Color().toplevel_background)
        self.frame_main.grid_rowconfigure(0, weight = 0)
        self.frame_main.grid_rowconfigure(1, weight = 1)
        self.frame_main.grid_columnconfigure(0, weight = 1)
        self.frame_main.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = NSEW)
        
        self.label_title = CTkLabel(self.frame_main, text = "Inspection History",
                                    fg_color = Color().toplevel_background,
                                    font = (Font().font_bold, 28),
                                    text_color = Color().black)
        self.label_title.grid(row = 0, column = 0, sticky = EW)
        
        self.frame_table = CTkFrame(self.frame_main, fg_color = Color().table_background)
        self.frame_table.grid(row = 1, column = 0, sticky = NSEW)
        self.frame_table.grid_columnconfigure(0, weight = 1)
        self.frame_table.grid_rowconfigure(0, weight = 0)
        self.frame_table.grid_rowconfigure(1, weight = 1)
        
        self.frame_table_header = CTkFrame(self.frame_table, fg_color = Color().transparent)
        self.frame_table_header.grid(row = 0, column = 0, sticky = EW)
        self.frame_table_header.grid_columnconfigure(0, weight = 1)
        
        self.table_header = Table_Row(self.frame_table_header)
        self.table_header.build_header()
        self.table_header.insert_row_value("No.", "Part Number", "Part ID", "Side", "Time", "Result")
        self.table_header.grid(row = 0, column = 0, sticky = EW)
        
        self.frame_table_body = CTkScrollableFrame(self.frame_table, fg_color = Color().table_background,
                                                   corner_radius = 0)
        self.frame_table_body._scrollbar.grid_remove()
        self.frame_table_body.grid(row = 1, column = 0, sticky = NSEW)
        self.frame_table_body.grid_columnconfigure(0, weight = 1)
    
    def insert_row(self, partnumber : str, partid : str,  side : str, time : float, result : Result):
        row = Table_Row(self.frame_table_body)
        row.build_body()
        row.insert_row_value(f"{self.total_table_row + 1}", partnumber, partid, side, f"{time:.2f}", result.name)
        row.change_result_cell_color(result)
        
        row.grid()
        self.list_table_row.append(row)
        
        self.total_table_row += 1
    
    def delete_row(self, index : int):
        index = index - 1
        try:
            self.list_table_row[index].destroy()
            del self.list_table_row[index]
            
            self.total_table_row -= 1
        except:
            print("Can't delete row")
    
    def clear_table(self):
        for row in self.list_table_row:
            row.destroy()
        self.list_table_row = []
        self.total_table_row = 0
        self.scroll_to_top()
    
    def scroll_to_top(self):
        self.frame_table_body._parent_canvas.yview_moveto(0)
        
    def scroll_to_bottom(self):
        self.frame_table_body._parent_canvas.yview_moveto(1)
    
    def bringToTop(self):
        self.after(100, lambda: self.attributes("-topmost", True))
        self.after(500, lambda: self.attributes("-topmost", False))
    
    def window_exit_btn_callback(self):
        self.destroy()

class Table_Row(CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        self.cell_color = Color().white
        self.cell_height = 50
        self.cell_border_width = 1
        self.cell_border_color = Color().black
        self.cell_font = (Font().font, 36)
        self.cell_font_color = Color().black
        self.cell_highlight_color = Color().yellow

        self.cell_header_color = Color().white
        self.cell_header_height = 50
        self.cell_header_border_width = 1
        self.cell_header_border_color = Color().black
        self.cell_header_font = (Font().font_bold, 36)
        self.cell_header_font_color = Color().black
        
        self.configure(fg_color = Color().transparent)
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        self.grid_configure(sticky = EW)
        
        self.frame_main = CTkFrame(self, fg_color = Color().transparent)
        self.frame_main.grid(row = 0, column = 0, sticky = EW)
        self.frame_main.grid_columnconfigure(0, weight = 1)
        self.frame_main.grid_columnconfigure(1, weight = 1, minsize = 430)
        self.frame_main.grid_columnconfigure(2, weight = 1)
        self.frame_main.grid_columnconfigure(3, weight = 1)
        self.frame_main.grid_columnconfigure(4, weight = 1)
        self.frame_main.grid_columnconfigure(5, weight = 1)
        self.frame_main.grid_rowconfigure(0, weight = 1)
        
    def build_body(self):
        self.cell_0 = CTkEntry(self.frame_main, fg_color = self.cell_color,
                                height = self.cell_height,
                                corner_radius = 0,
                                border_color = self.cell_border_color,
                                border_width = self.cell_border_width,
                                font = self.cell_font,
                                text_color = self.cell_font_color,
                                justify = CENTER)
        self.cell_0.grid(row = 0, column = 0, sticky = EW)
        self.cell_0.bind("<Enter>", self.event_highlight_row)
        self.cell_0.bind("<Leave>", self.event_unhighlight_row)
        
        self.cell_1 = CTkEntry(self.frame_main, fg_color = self.cell_color,
                                height = self.cell_height,
                                corner_radius = 0,
                                border_color = self.cell_border_color,
                                border_width = self.cell_border_width,
                                font = self.cell_font,
                                text_color = self.cell_font_color,
                                justify = CENTER)
        self.cell_1.grid(row = 0, column = 1, sticky = EW)
        self.cell_1.bind("<Enter>", self.event_highlight_row)
        self.cell_1.bind("<Leave>", self.event_unhighlight_row)
        
        self.cell_2 = CTkEntry(self.frame_main, fg_color = self.cell_color,
                                height = self.cell_height,
                                corner_radius = 0,
                                border_color = self.cell_border_color,
                                border_width = self.cell_border_width,
                                font = self.cell_font,
                                text_color = self.cell_font_color,
                                justify = CENTER)
        self.cell_2.grid(row = 0, column = 2, sticky = EW)
        self.cell_2.bind("<Enter>", self.event_highlight_row)
        self.cell_2.bind("<Leave>", self.event_unhighlight_row)
        
        self.cell_3 = CTkEntry(self.frame_main, fg_color = self.cell_color,
                                height = self.cell_height,
                                corner_radius = 0,
                                border_color = self.cell_border_color,
                                border_width = self.cell_border_width,
                                font = self.cell_font,
                                text_color = self.cell_font_color,
                                justify = CENTER)
        self.cell_3.grid(row = 0, column = 3, sticky = EW)
        self.cell_3.bind("<Enter>", self.event_highlight_row)
        self.cell_3.bind("<Leave>", self.event_unhighlight_row)
        
        self.cell_4 = CTkEntry(self.frame_main, fg_color = self.cell_color,
                                height = self.cell_height,
                                corner_radius = 0,
                                border_color = self.cell_border_color,
                                border_width = self.cell_border_width,
                                font = self.cell_font,
                                text_color = self.cell_font_color,
                                justify = CENTER)
        self.cell_4.grid(row = 0, column = 4, sticky = EW)
        self.cell_4.bind("<Enter>", self.event_highlight_row)
        self.cell_4.bind("<Leave>", self.event_unhighlight_row)
        
        self.cell_5 = CTkEntry(self.frame_main, fg_color = self.cell_color,
                                height = self.cell_height,
                                corner_radius = 0,
                                border_color = self.cell_border_color,
                                border_width = self.cell_border_width,
                                font = self.cell_font,
                                text_color = self.cell_font_color,
                                justify = CENTER)
        self.cell_5.grid(row = 0, column = 5, sticky = EW)
        self.cell_5.bind("<Enter>", self.event_highlight_row)
        self.cell_5.bind("<Leave>", self.event_unhighlight_row)
    
    def build_header(self):
        self.cell_0 = CTkEntry(self.frame_main, fg_color = self.cell_header_color,
                                height = self.cell_header_height,
                                corner_radius = 0,
                                border_color = self.cell_header_border_color,
                                border_width = self.cell_header_border_width,
                                font = self.cell_header_font,
                                text_color = self.cell_header_font_color,
                                justify = CENTER)
        self.cell_0.grid(row = 0, column = 0, sticky = EW)
        
        self.cell_1 = CTkEntry(self.frame_main, fg_color = self.cell_header_color,
                                height = self.cell_header_height,
                                corner_radius = 0,
                                border_color = self.cell_header_border_color,
                                border_width = self.cell_header_border_width,
                                font = self.cell_header_font,
                                text_color = self.cell_header_font_color,
                                justify = CENTER)
        self.cell_1.grid(row = 0, column = 1, sticky = EW)
        
        self.cell_2 = CTkEntry(self.frame_main, fg_color = self.cell_header_color,
                                height = self.cell_header_height,
                                corner_radius = 0,
                                border_color = self.cell_header_border_color,
                                border_width = self.cell_header_border_width,
                                font = self.cell_header_font,
                                text_color = self.cell_header_font_color,
                                justify = CENTER)
        self.cell_2.grid(row = 0, column = 2, sticky = EW)
        
        self.cell_3 = CTkEntry(self.frame_main, fg_color = self.cell_header_color,
                                height = self.cell_header_height,
                                corner_radius = 0,
                                border_color = self.cell_header_border_color,
                                border_width = self.cell_header_border_width,
                                font = self.cell_header_font,
                                text_color = self.cell_header_font_color,
                                justify = CENTER)
        self.cell_3.grid(row = 0, column = 3, sticky = EW)
        
        self.cell_4 = CTkEntry(self.frame_main, fg_color = self.cell_header_color,
                                height = self.cell_header_height,
                                corner_radius = 0,
                                border_color = self.cell_header_border_color,
                                border_width = self.cell_header_border_width,
                                font = self.cell_header_font,
                                text_color = self.cell_header_font_color,
                                justify = CENTER)
        self.cell_4.grid(row = 0, column = 4, sticky = EW)
        
        self.cell_5 = CTkEntry(self.frame_main, fg_color = self.cell_header_color,
                                height = self.cell_header_height,
                                corner_radius = 0,
                                border_color = self.cell_header_border_color,
                                border_width = self.cell_header_border_width,
                                font = self.cell_header_font,
                                text_color = self.cell_header_font_color,
                                justify = CENTER)
        self.cell_5.grid(row = 0, column = 5, sticky = EW)
    
    def event_highlight_row(self, event):
        self.cell_0.configure(fg_color = self.cell_highlight_color)
        self.cell_1.configure(fg_color = self.cell_highlight_color)
        self.cell_2.configure(fg_color = self.cell_highlight_color)
        self.cell_3.configure(fg_color = self.cell_highlight_color)
        self.cell_4.configure(fg_color = self.cell_highlight_color)
        
    def event_unhighlight_row(self, event):
        self.cell_0.configure(fg_color = self.cell_color)
        self.cell_1.configure(fg_color = self.cell_color)
        self.cell_2.configure(fg_color = self.cell_color)
        self.cell_3.configure(fg_color = self.cell_color)
        self.cell_4.configure(fg_color = self.cell_color)
    
    def insert_row_value(self, cell0, cell1, cell2, cell3, cell4, cell5):
        if self.cell_0.winfo_exists():
            self.insertEntry(self.cell_0, cell0)
        if self.cell_1.winfo_exists():
            self.insertEntry(self.cell_1, cell1)
        if self.cell_2.winfo_exists():
            self.insertEntry(self.cell_2, cell2)
        if self.cell_3.winfo_exists():
            self.insertEntry(self.cell_3, cell3)
        if self.cell_4.winfo_exists():
            self.insertEntry(self.cell_4, cell4)
        if self.cell_5.winfo_exists():
            self.insertEntry(self.cell_5, cell5)
    
    def insertEntry(self, entry, text):
        entry.configure(state = "normal")
        entry.delete(0, END)
        entry.insert(END, text)
        entry.configure(state = "readonly")
    
    def change_result_cell_color(self, result : Result):
        self.cell_5.configure(text_color = Color().white)
        
        if result == Result.OK:
            self.cell_5.configure(fg_color = Color().green)
        elif result == Result.NG:
            self.cell_5.configure(fg_color = Color().red)
        elif result == Result.ERROR:
            self.cell_5.configure(fg_color = Color().orange)
        elif result == Result.RESULT:
            self.cell_5.configure(fg_color = Color().darkblue)