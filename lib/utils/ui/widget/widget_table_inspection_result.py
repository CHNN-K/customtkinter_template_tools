from customtkinter import *
from lib.utils import Result
from lib.utils.ui import Color, Font

class Widget_Table_Inspection_Result(CTkFrame):
    def __init__(self, master, mainApp, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
    
        # Variable
        self.mainApp = mainApp
        self.callback = None
        
        self.total_table_row = 0
        self.list_table_row = []
        
        # Setting
        self.widget_width = 667
        self.widget_height = 820
        
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
        self.frame_main.grid_rowconfigure(0, weight = 0)
        self.frame_main.grid_rowconfigure(1, weight = 1)
        
        self.frame_table_header = CTkFrame(self.frame_main, fg_color = Color().transparent)
        self.frame_table_header.grid(row = 0, column = 0, sticky = EW)
        self.frame_table_header.grid_columnconfigure(0, weight = 1)
        self.frame_table_header.grid_rowconfigure(0, weight = 1)
        
        self.table_header = Table_Row(self.frame_table_header)
        self.table_header.build_header()
        self.table_header.insert_row_value("Point", "Component", "Result")
        self.table_header.grid(row = 0, column = 0, sticky = EW)
        
        self.frame_table_body = CTkScrollableFrame(self.frame_main, fg_color = Color().table_background, 
                                                   corner_radius = 0)
        self.frame_table_body._scrollbar.grid_remove()
        self.frame_table_body.grid(row = 1, column = 0, sticky = NSEW)
        self.frame_table_body.grid_columnconfigure(0, weight = 1)
    
    def insert_row(self, component : str, result : Result):
        row = Table_Row(self.frame_table_body)
        row.build_body()
        row.insert_row_value(f"{self.total_table_row + 1}", component, result.name)
        row.change_result_cell_color(result)
        
        row.grid(sticky = EW)
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
    
    def set_callback(self, callback):
        self.callback = callback

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
        self.frame_main.grid_columnconfigure(1, weight = 1, minsize = 350)
        self.frame_main.grid_columnconfigure(2, weight = 1)
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
    
    def event_highlight_row(self, event):
        self.cell_0.configure(fg_color = self.cell_highlight_color)
        self.cell_1.configure(fg_color = self.cell_highlight_color)
        
    def event_unhighlight_row(self, event):
        self.cell_0.configure(fg_color = self.cell_color)
        self.cell_1.configure(fg_color = self.cell_color)
    
    def insert_row_value(self, cell0, cell1, cell2):
        if self.cell_0.winfo_exists():
            self.insertEntry(self.cell_0, cell0)
        if self.cell_1.winfo_exists():
            self.insertEntry(self.cell_1, cell1)
        if self.cell_2.winfo_exists():
            self.insertEntry(self.cell_2, cell2)
    
    def insertEntry(self, entry, text):
        entry.configure(state = "normal")
        entry.delete(0, END)
        entry.insert(END, text)
        entry.configure(state = "readonly")
    
    def change_result_cell_color(self, result : Result):
        self.cell_2.configure(text_color = Color().white)
        
        if result == Result.OK:
            self.cell_2.configure(fg_color = Color().green)
        elif result == Result.NG:
            self.cell_2.configure(fg_color = Color().red)
        elif result == Result.ERROR:
            self.cell_2.configure(fg_color = Color().orange)
        elif result == Result.RESULT:
            self.cell_2.configure(fg_color = Color().darkblue)