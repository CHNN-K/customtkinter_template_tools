from customtkinter import *

class Color:
    def __init__(self):
        self.background = "#3A3A3A"
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

class Font:
    def __init__(self):
        self.font = "Kanit light"
        self.font_bold = "Kanit"
        
        # Custom Alert Window
        self.alertWindowLine1 = (self.font_bold, 18)
        self.alertWindowLine2 = (self.font, 18)
        self.alertWindowButton = (self.font_bold, 16)

class MainApp(CTk):
    def __init__(self):
        super().__init__()

        # Variable
        
        # Screen Setting
        screen_width = 300
        screen_height = 800
        self.geometry(f"{screen_width}x{screen_height}+{self.winfo_screenwidth()//2 - screen_width//2}+{self.winfo_screenheight()//2 - screen_height//2}")
        self.resizable(False, False)
        
        set_appearance_mode("Dark")
        # deactivate_automatic_dpi_awareness()

        self.title("Template")
        
        self.bind("<Escape>", lambda event : self.destroy())

        # UI
        self.build_ui()
        
        self.CustomAlertWindow_1_Button_UI()
        self.CustomAlertWindow_2_Button_UI()
        self.CustomTopLevel_UI()
        self.CustomWidget_UI()
        self.AnimatedWidget_UI()
        self.MousePositionToplevel_UI()
        self.AllCursorTopLevel_UI()
        self.orderFunctionToplevel_UI()
        self.processingTopLevel_UI()
        
        # Function
        self.FixedUpdate()
    
    def FixedUpdate(self):
        
        self.after(10, self.FixedUpdate)

    def build_ui(self):
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)
        
        self.frame_main = CTkFrame(self)
        self.frame_main.grid(row = 0, column = 0, sticky = NSEW)
        self.frame_main.grid_rowconfigure(0, weight = 1)
        self.frame_main.grid_columnconfigure(0, weight = 1)
    
    # region Custom Alert Window 1 Button
    def CustomAlertWindow_1_Button_UI(self):
        self.btn_customAlerWindow_1_Button = CTkButton(self, text = "Custom Alert Window 1 Button", 
                                                       command = self.openCustomAlertWindow_1_Button)
        self.btn_customAlerWindow_1_Button.place(relx = 0.5, rely = 0.1, anchor = CENTER)
        
    def openCustomAlertWindow_1_Button(self):
        self.customAlertWindow_1_button = CustomAlertWindow1Button(self)
    # endregion
    
    # region Custom Alert Window 2 Button
    def CustomAlertWindow_2_Button_UI(self):
        self.btn_customAlerWindow_2_Button = CTkButton(self, text = "Custom Alert Window 2 Button", 
                                                       command = self.openCustomAlertWindow_2_Button)
        self.btn_customAlerWindow_2_Button.place(relx = 0.5, rely = 0.15, anchor = CENTER)
    
    def openCustomAlertWindow_2_Button(self):
        self.customAlertWindow_2_button = CustomAlertWindow2Button(self)
        self.customAlertWindow_2_button.btn1.configure(command = self.customAlertWindow_2_Button_Button1Function)
    
    # Edit Function
    def customAlertWindow_2_Button_Button1Function(self):
        print ("Press Button 1")
    # endregion
    
    # region Custom Toplevel
    def CustomTopLevel_UI(self):
        self.btn_customTopLevel = CTkButton(self, text = "Custom Toplevel", 
                                                       command = self.openCustomTopLevel)
        self.btn_customTopLevel.place(relx = 0.5, rely = 0.2, anchor = CENTER)
        
    def openCustomTopLevel(self):
        self.customTopLevel = CustomTopLevel(self, self)
    # endregion
    
    # region Custom Widget
    def CustomWidget_UI(self):
        self.customWidget = CustomWidget(self.frame_main, self)
        self.customWidget.place(relx = 0.5, rely = 0.6, anchor = CENTER)
    # endregion
    
    # region Animated Widget
    def AnimatedWidget_UI(self):
        self.animatedWidget = AnimatedWidget(self.frame_main)
        self.animatedWidget.place(relx = 0.5, rely = 0.7, anchor = CENTER)
        self.animatedWidget.moveStep = 0.001
        
        self.btn_animatedWidget = CTkButton(self.frame_main, text = "Animate", 
                                            command = self.animateWidget)
        self.btn_animatedWidget.place(relx = 0.5, rely = 0.25, anchor = CENTER)
    
    def animateWidget(self):
        self.animatedWidget.place(relx = 0.5, rely = 0.6, anchor = CENTER)
        self.animatedWidget.animator(0.5, 0.9)
    # endregion
    
    def MousePositionToplevel_UI(self):
        self.btn_mousePositionToplevel = CTkButton(self.frame_main, text = "Mouse Position Toplevel",
                                                   command = self.openMousePositionToplevel)
        self.btn_mousePositionToplevel.place(relx = 0.5, rely = 0.3, anchor = CENTER)

    def openMousePositionToplevel(self):
        self.mousePositionToplevel = MousePosition(self)
        
    def AllCursorTopLevel_UI(self):
        self.btn_allCursorTopLevel = CTkButton(self.frame_main, text = "All Cursor Toplevel", 
                                               command = self.openAllCursorToplevel)
        self.btn_allCursorTopLevel.place(relx = 0.5, rely = 0.35, anchor = CENTER)
    
    def openAllCursorToplevel(self):
        self.allCrosshairToplevel = AllCursor(self)
    
    def orderFunctionToplevel_UI(self):
        self.btn_orderFunctionTopLevel = CTkButton(self.frame_main, text = "Order Function Toplevel", 
                                                   command = self.openOrderFUnctionToplevel)
        self.btn_orderFunctionTopLevel.place(relx = 0.5, rely = 0.4, anchor = CENTER)
    
    def openOrderFUnctionToplevel(self):
        self.orderFunctionToplevel = OrderFuntion(self)
        
    def processingTopLevel_UI(self):
        self.btn_processingTopLevel = CTkButton(self.frame_main, text = "Processing Toplevel", 
                                                   command = self.openProcessingToplevel)
        self.btn_processingTopLevel.place(relx = 0.5, rely = 0.45, anchor = CENTER)
    
    def openProcessingToplevel(self):
        self.toplevel_processing = Toplevel_Process_Status(self, 3)
        self.toplevel_processing.processFinish_callback()

class CustomAlertWindow1Button(CTkToplevel):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        # Variable
        
        # Setting
        self.attributes("-topmost", False)  # Always on top
        
        screen_width = 400
        screen_height = 200
        self.geometry(f"{screen_width}x{screen_height}+{self.winfo_screenwidth()//2 - screen_width//2}+{self.winfo_screenheight()//2 - screen_height//2}")
        
        self.title("Custom alert window")
        
        self.resizable(False,False)
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.destroy)
        
        self.build_ui()
        self.bringToTop()

    def build_ui(self):
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        
        self.frame_main = CTkFrame(self, fg_color = Color().transparent)
        self.frame_main.grid_rowconfigure((0,1), weight = 1)
        self.frame_main.grid_columnconfigure(0, weight = 1)
        self.frame_main.grid(row = 0, column = 0)

        self.frame_text = CTkFrame(self.frame_main, fg_color = Color().transparent)
        self.frame_text.grid_rowconfigure((0,1), weight = 1)
        self.frame_text.grid_columnconfigure(0, weight = 1)
        self.frame_text.grid(row = 0, column = 0, sticky = EW)

        self.line1 = CTkLabel(self.frame_text, text = "Line 1 (Bold Text)", 
                              font = Font().alertWindowLine1,
                              text_color = Color().white)
        self.line1.grid(row = 0, column = 0)

        self.line2 = CTkLabel(self.frame_text, text = "Line 2 (Nomal Text)", 
                              font = Font().alertWindowLine2,
                              text_color = Color().white)
        self.line2.grid(row = 1, column = 0)

        self.frame_btn = CTkFrame(self.frame_main, fg_color = Color().transparent)
        self.frame_btn.grid_rowconfigure(0, weight = 1)
        self.frame_btn.grid_columnconfigure(0, weight = 1)
        self.frame_btn.grid(row = 1, column = 0, pady = 20, sticky = EW)

        self.btn1 = CTkButton(self.frame_btn, text = "Button", 
                              fg_color = Color().blue,
                              font = Font().alertWindowButton,
                              height = 30,
                              command = self.btn1Function)
        self.btn1.grid(row = 0, column = 0)

    def btn1Function(self):
        pass
    
    def bringToTop(self):
        self.after(100, lambda: self.attributes("-topmost", True))
        self.after(500, lambda: self.attributes("-topmost", False))

class CustomAlertWindow2Button(CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Variable
        
        # Setting
        self.attributes("-topmost", False)  # Always on top
        
        screen_width = 400
        screen_height = 200
        self.geometry(f"{screen_width}x{screen_height}+{self.winfo_screenwidth()//2 - screen_width//2}+{self.winfo_screenheight()//2 - screen_height//2}")
        
        self.title("Custom alert window")
        
        self.resizable(False,False)
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.destroy)
        
        self.build_ui()
        self.bringToTop()

    def build_ui(self):
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

        self.frame_main = CTkFrame(self, fg_color = Color().transparent)
        self.frame_main.grid_rowconfigure((0,1), weight = 1)
        self.frame_main.grid_columnconfigure(0, weight = 1)
        self.frame_main.grid(row = 0, column = 0)

        self.frame_text = CTkFrame(self.frame_main, fg_color = Color().transparent)
        self.frame_text.grid_rowconfigure((0,1), weight = 1)
        self.frame_text.grid_columnconfigure(0, weight = 1)
        self.frame_text.grid(row = 0, column = 0, sticky = EW)
        
        self.line1 = CTkLabel(self.frame_text, text = "Line 1 (Bold Text)", 
                              font = Font().alertWindowLine1,
                              text_color = Color().white)
        self.line1.grid(row = 0, column = 0)

        self.line2 = CTkLabel(self.frame_text, text = "Line 2 (Nomal Text)", 
                              font = Font().alertWindowLine2,
                              text_color = Color().white)
        self.line2.grid(row = 1, column = 0)

        self.frame_btn = CTkFrame(self.frame_main, fg_color = Color().transparent)
        self.frame_btn.grid_rowconfigure(0, weight = 1)
        self.frame_btn.grid_columnconfigure((1), weight = 0, minsize = 20)
        self.frame_btn.grid_columnconfigure((0,2), weight = 1)
        self.frame_btn.grid(row = 1, column = 0, pady = 20, sticky = EW)

        self.btn1 = CTkButton(self.frame_btn, text = "Button 1", 
                              fg_color = Color().blue,
                              font = Font().alertWindowButton,
                              height = 30,
                              command = self.btn1Function)
        self.btn1.grid(row = 0, column = 0, sticky = W)

        self.btn2 = CTkButton(self.frame_btn, text = "Button 2", 
                              fg_color = Color().red,
                              font = Font().alertWindowButton,
                              height = 30, 
                              command = self.btn2Function)
        self.btn2.grid(row = 0, column = 2, sticky = E)

    def btn1Function(self):
        pass

    def btn2Function(self):
        pass
        
    def bringToTop(self):
        self.after(100, lambda: self.attributes("-topmost", True))
        self.after(500, lambda: self.attributes("-topmost", False))

class CustomTopLevel(CTkToplevel):
    def __init__(self, master, mainApp, *args,**kwargs):
        super().__init__(master, *args, **kwargs)
        
        # Variable
        self.mainApp = mainApp
        
        # Setting
        self.attributes("-topmost", False)  # Always on top
        
        screen_width = 400
        screen_height = 600
        self.geometry(f"{screen_width}x{screen_height}+{self.winfo_screenwidth()//2 - screen_width//2}+{self.winfo_screenheight()//2 - screen_height//2}")
        
        self.title("Toplevel")
        
        self.resizable(False,False)
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.window_exit_btn_callback)
        
        self.build_ui()
        self.bringToTop()

    def build_ui(self):
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        
        self.frame_main = CTkFrame(self, fg_color = Color().transparent)
        self.frame_main.grid_rowconfigure((0,1), weight = 1)
        self.frame_main.grid_columnconfigure(0, weight = 1)
        self.frame_main.grid(row = 0, column = 0)
    
    def bringToTop(self):
        self.after(100, lambda: self.attributes("-topmost", True))
        self.after(500, lambda: self.attributes("-topmost", False))
    
    def window_exit_btn_callback(self):
        print("Destroy Window")
        self.destroy()

class CustomWidget(CTkFrame):
    def __init__(self, master, mainApp, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
    
        # Variable
        self.mainApp = mainApp
        
        self.textBoxValue = ""
        
        # UI
        self.build_ui()
        
        # Function
        self.FixedUpdate()
        
    def FixedUpdate(self):
        self.textBoxLenLabel()
        self.after(50, self.FixedUpdate)
    
    def build_ui(self):
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)
        
        self.frame_main = CTkFrame(self, fg_color = Color().transparent)
        self.frame_main.grid_rowconfigure((0,1,2), weight = 0)
        self.frame_main.grid_columnconfigure(0, weight = 1)
        self.frame_main.grid(row = 0, column = 0, sticky = NSEW)
        
        self.label1 = CTkLabel(self.frame_main, text = "CustomWidget 1")
        self.label1.grid(row = 0, column = 0)
        
        self.textBox = CTkEntry(self.frame_main, placeholder_text = "Entry Box...")
        self.textBox.grid(row = 1, column = 0)
        
        self.label2 = CTkLabel(self.frame_main, text = "Text count : 0")
        self.label2.grid(row = 2, column = 0)
    
    def textBoxLenLabel(self):
        if (self.textBox.get() != self.textBoxValue):
            self.textBoxValue = self.textBox.get()
            self.label2.configure(text = f"Text count : {len(self.textBoxValue)}")

class AnimatedWidget(CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        # Variable
        self.moveStep = 0.001    # percentage (0.0-1.0) = (0-100%)
        self.isAnimate = False

        # UI
        self.build_ui()

    def build_ui(self):
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)
        
        self.frame_main = CTkFrame(self, fg_color = Color().transparent)
        self.frame_main.grid_rowconfigure((0,1), weight = 0)
        self.frame_main.grid_columnconfigure(0, weight = 1)
        self.frame_main.grid(row = 0, column = 0, sticky = NSEW)
        
        self.label1 = CTkLabel(self.frame_main, text = "Animated Widget")
        self.label1.grid(row = 0, column = 0)
        
    def animator(self, stopx, stopy):
        # Learning https://www.youtube.com/watch?v=vVRrOi5LGSo

        self.isAnimate = True

        posx = float(self.place_info()["relx"])
        posy = float(self.place_info()["rely"])
        dirx = 0
        diry = 0
        
        refreshRate = 1    # ms/times
        precision = len(str(self.moveStep).split(".")[1])

        if (posx == stopx and posy == stopy):
            self.isAnimate = False
            return

        if (stopx > posx):
            dirx = 1
            nextPosX = round(posx + self.moveStep, precision)
            if (nextPosX > stopx):
                nextPosX = posx
        else:
            dirx = -1
            nextPosX = round(posx - self.moveStep, precision)
            if (nextPosX < stopx):
                nextPosX = posx

        if (stopy > posy):
            diry = 1
            nextPosY = round(posy + self.moveStep, precision)
            if (nextPosY > stopy):
                nextPosY = posy
        else:
            diry = -1
            nextPosY = round(posy - self.moveStep, precision)
            if (nextPosY < stopy):
                nextPosY = posy

        if (posx == nextPosX and posy == nextPosY):
            self.place(relx = nextPosX, rely = nextPosY, anchor = self.place_info()["anchor"])
            self.isAnimate = False
            return

        self.place(relx = nextPosX, rely = nextPosY, anchor = self.place_info()["anchor"])
        
        if (dirx == 1 and diry == 1):
            if (not posx > stopx or not posy > stopy):
                self.after(refreshRate, lambda : self.animator(stopx, stopy))
        
        elif (dirx == -1 and diry == 1):
            if (not posx < stopx or not posy > stopy):
                self.after(refreshRate, lambda : self.animator(stopx, stopy))
        
        elif (dirx == 1 and diry == -1):
            if (not posx > stopx or not posy < stopy):
                self.after(refreshRate, lambda : self.animator(stopx, stopy))
        
        elif (dirx == -1 and diry == -1):
            if (not posx < stopx or not posy < stopy):
                self.after(refreshRate, lambda : self.animator(stopx, stopy))

        return

class MousePosition(CTkToplevel):
    def __init__(self, master, *args,**kwargs):
        super().__init__(master, *args, **kwargs)
        
        # Variable
        self.isMousePress = False
        self.mouseX = 0
        self.mouseY = 0
        
        # Setting
        self.attributes("-topmost", False)  # Always on top
        
        screen_width = 400
        screen_height = 600
        self.geometry(f"{screen_width}x{screen_height}+{self.winfo_screenwidth()//2 - screen_width//2}+{self.winfo_screenheight()//2 - screen_height//2}")
        
        self.title("Toplevel")
        
        self.resizable(False,False)
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.destroy)
        
        # deactivate_automatic_dpi_awareness()
        
        self.build_ui()
        self.bringToTop()

        self.bind("<Motion>", self.mousePositionCallback)

    def build_ui(self):
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        
        self.frame_main = CTkFrame(self, fg_color = Color().transparent)
        self.frame_main.grid_rowconfigure((0,1), weight = 1)
        self.frame_main.grid_columnconfigure(0, weight = 1)
        self.frame_main.grid(row = 0, column = 0)
        
        self.mousePosition = CTkLabel(self, text = "X:0, Y:0")
        self.mousePosition.place(relx = 1, rely = 1, anchor = SE)
        
        self.dragableBox = CTkLabel(self, text = "Drag Me", 
                                    height = 20, width = 20, 
                                    fg_color = Color().red,
                                    cursor = "fleur")
        self.dragableBox.place(x = self.winfo_width()/2, y = self.winfo_height()/2, anchor = CENTER)
        self.dragableBox.bind("<ButtonPress-1>", self.onMouseClick)
        self.dragableBox.bind('<ButtonRelease-1>', self.onMouseRelease)
    
    def bringToTop(self):
        self.after(100, lambda: self.attributes("-topmost", True))
        self.after(500, lambda: self.attributes("-topmost", False))
        
    def mousePositionCallback(self, event):
        # Get the absolute mouse position on the screen
        abs_x = self.winfo_pointerx()
        abs_y = self.winfo_pointery()
        
        # Get the position of the window on the screen
        win_x = self.winfo_rootx()
        win_y = self.winfo_rooty()
        
        # Calculate the mouse position relative to the window
        rel_x = abs_x - win_x
        rel_y = abs_y - win_y
        
        self.mouseX = rel_x
        self.mouseY = rel_y
        
        self.mousePosition.configure(text = f"X:{self.mouseX}, Y:{self.mouseY}")
    
    def onMouseClick(self, event):
        self.isMousePress = True
        self.moveBox(self.dragableBox)
    
    def onMouseRelease(self, event):
        self.isMousePress = False
        
    def moveBox(self, widget):
        if self.isMousePress:
            widget.place(x = self.mouseX, y = self.mouseY, anchor = CENTER)
            self.after(1, lambda : self.moveBox(widget))
        else:
            pass

class AllCursor(CTkToplevel):
    def __init__(self, master, *args,**kwargs):
        super().__init__(master, *args, **kwargs)
        
        # Variable
        self.cursorList = ["X_cursor","arrow","based_arrow_down","based_arrow_up",
                            "boat","bogosity","bottom_left_corner","bottom_right_corner",
                            "bottom_side","bottom_tee","box_spiral","center_ptr",
                            "circle","clock","coffee_mug","cross",
                            "cross_reverse","crosshair","diamond_cross","dot",
                            "dotbox","double_arrow","draft_large","draft_small",
                            "draped_box","exchange","fleur","gobbler",
                            "gumby","hand1","hand2","heart",
                            "ibeam","icon","iron_cross","left_ptr",
                            "left_side","left_tee","leftbutton","ll_angle",
                            "lr_angle","man","middlebutton","mouse",
                            "none","pencil","pirate","plus",
                            "question_arrow","right_ptr","right_side","right_tee",
                            "rightbutton","rtl_logo","sailboat","sb_down_arrow",
                            "sb_h_double_arrow","sb_left_arrow","sb_right_arrow","sb_up_arrow",
                            "sb_v_double_arrow","shuttle","sizing","spider",
                            "spraycan","star","target","tcross",
                            "top_left_arrow","top_left_corner","top_right_corner","top_side",
                            "top_tee","trek","ul_angle","umbrella",
                            "ur_angle","watch","xterm"]
        self.cursorWidgetList = []
        
        # Setting
        self.attributes("-topmost", False)  # Always on top
        
        screen_width = 800
        screen_height = 800
        self.geometry(f"{screen_width}x{screen_height}+{self.winfo_screenwidth()//2 - screen_width//2}+{self.winfo_screenheight()//2 - screen_height//2}")
        
        self.title("All Cursor")
        
        self.resizable(False,False)
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.closeAndFocus)
        
        self.build_ui()
        self.bringToTop()
    
    def build_ui(self):
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        
        self.frame_main = CTkFrame(self, fg_color = Color().transparent)
        self.frame_main.grid_rowconfigure(0, weight = 0)
        self.frame_main.grid_columnconfigure(0, weight = 0)
        self.frame_main.grid(row = 0, column = 0)
        
        for order, c in enumerate(self.cursorList):
            cursorWidget = CTkLabel(self.frame_main, text = c,
                         width = 175,
                         cursor = c,
                         fg_color = Color().gray,
                         text_color = Color().white)
            cursorWidget.grid(row = order//4, column = order % 4, padx=3, pady=3, sticky = EW)
            self.cursorWidgetList.append(cursorWidget)
            self.cursorWidgetList[order].bind("<Button-1>", self.copyText)
            self.cursorWidgetList[order].bind("<Enter>", self.changeCursor)
            self.cursorWidgetList[order].bind("<Leave>", self.defaultCursor)
            
    def closeAndFocus(self):
        self.master.focus_set()
        self.destroy()
    
    def bringToTop(self):
        self.after(100, lambda: self.attributes("-topmost", True))
        self.after(200, lambda: self.attributes("-topmost", False))
    
    def changeCursor(self, event):
        event.widget.configure(cursor = event.widget.master.cget("text"))
    
    def defaultCursor(self, event):
        event.widget.configure(cursor = "")
    
    def copyText(self, event):
        event.widget.clipboard_clear()
        event.widget.master.clipboard_append(event.widget.master.cget("text"))
        print (f"Copy cursor to clipboard : {event.widget.master.cget("text")}")
      
class OrderFuntion(CTkToplevel):
    def __init__(self, master, *args,**kwargs):
        super().__init__(master, *args, **kwargs)
        
        # Variable
        self.orderFunction = []
        self.orderFunctionName = []
        
        # Setting
        self.attributes("-topmost", False)  # Always on top
        
        screen_width = 400
        screen_height = 600
        self.geometry(f"{screen_width}x{screen_height}+{self.winfo_screenwidth()//2 - screen_width//2}+{self.winfo_screenheight()//2 - screen_height//2}")
        
        self.title("Order Function")
        
        self.resizable(False,False)
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.closeAndFocus)
        
        self.build_ui()
        self.FixedUpdate()
        
        self.bringToTop()

    def build_ui(self):
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        
        self.frame_main = CTkFrame(self, fg_color = Color().transparent)
        self.frame_main.grid(row = 0, column = 0)
        
        self.btn_clearOrder = CTkButton(self.frame_main, text = "Clear order", command = self.clearOrder)
        self.btn_clearOrder.pack()
        
        self.checkbox_A = CTkCheckBox(self.frame_main, text = "Func A : print ('A')", command = self.checkbox_A_callback)
        self.checkbox_A.pack()
        
        self.checkbox_B = CTkCheckBox(self.frame_main, text = "Func B : print ('B')", command = self.checkbox_B_callback)
        self.checkbox_B.pack()
        
        self.checkbox_C = CTkCheckBox(self.frame_main, text = "Func C : print ('C')", command = self.checkbox_C_callback)
        self.checkbox_C.pack()
        
        self.checkbox_D = CTkCheckBox(self.frame_main, text = "Func D : print ('D')", command = self.checkbox_D_callback)
        self.checkbox_D.pack()
        
        self.label_order_title = CTkLabel(self.frame_main, text = "Function Order")
        self.label_order_title.pack()
        
        self.label_order = CTkLabel(self.frame_main, text = "Function", fg_color = Color().gray, text_color = Color().white)
        self.label_order.pack()
        
        self.label_total_order = CTkLabel(self.frame_main, text = "Total Function : 0")
        self.label_total_order.pack()
        
        self.btn_execute = CTkButton(self.frame_main, text = "Execute in-order Function", command = self.executeOrderFunction)
        self.btn_execute.pack()
        
    def FixedUpdate(self):
        self.updateLabel()
        self.after(1, self.FixedUpdate)
    
    def executeOrderFunction(self):
        if len(self.orderFunction) > 0:
            for func in self.orderFunction:
                func()
        else:
            print(f"No Function in order")
    
    def clearOrder(self):
        self.orderFunction.clear()
        self.orderFunctionName.clear()
        self.checkbox_A.deselect()
        self.checkbox_B.deselect()
        self.checkbox_C.deselect()
        self.checkbox_D.deselect()
    
    def checkbox_A_callback(self):
        if self.checkbox_A.get():
            self.orderFunction.append(self.funcA)
            self.orderFunctionName.append(self.funcA.__name__)
        else:
            self.orderFunction.remove(self.funcA)
            self.orderFunctionName.remove(self.funcA.__name__)
    
    def checkbox_B_callback(self):
        if self.checkbox_B.get():
            self.orderFunction.append(self.funcB)
            self.orderFunctionName.append(self.funcB.__name__)
        else:
            self.orderFunction.remove(self.funcB)
            self.orderFunctionName.remove(self.funcB.__name__)
    
    def checkbox_C_callback(self):
        if self.checkbox_C.get():
            self.orderFunction.append(self.funcC)
            self.orderFunctionName.append(self.funcC.__name__)
        else:
            self.orderFunction.remove(self.funcC)
            self.orderFunctionName.remove(self.funcC.__name__)
    
    def checkbox_D_callback(self):
        if self.checkbox_D.get():
            self.orderFunction.append(self.funcD)
            self.orderFunctionName.append(self.funcD.__name__)
        else:
            self.orderFunction.remove(self.funcD)
            self.orderFunctionName.remove(self.funcD.__name__)
    
    def funcA(self):
        print("A")
    
    def funcB(self):
        print("B")
    
    def funcC(self):
        print("C")
    
    def funcD(self):
        print("D")
    
    def updateLabel(self):
        if len(self.orderFunctionName) > 0:
            self.label_order.configure(text = self.orderFunctionName)
        else:
            self.label_order.configure(text = "No Function in order")
            
        self.label_total_order.configure(text = f"Total Function : {len(self.orderFunction)}")
    
    def closeAndFocus(self):
        self.master.focus_set()
        self.destroy()
    
    def bringToTop(self):
        self.after(100, lambda: self.attributes("-topmost", True))
        self.after(200, lambda: self.attributes("-topmost", False))

class Toplevel_Process_Status(CTkToplevel):
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
        self.protocol("WM_DELETE_WINDOW", self.closeAndFocus)
        
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

    def closeAndFocus(self):
        self.grab_release()
        self.destroy()
    
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
            self.closeAndFocus()
            return
        
        self.label_timer.configure(text = f"Close in {self.autoCloseTime}...")
        self.autoCloseTime -= 1
        self.after(1000, lambda : self.autoCloseWindow(aliveTime))

  
app = MainApp()
app.mainloop()