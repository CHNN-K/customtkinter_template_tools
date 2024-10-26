from customtkinter import *
from lib.utils import ApplicationConfiguration
from lib.utils.ui import Color, Font, Thread_Client_Socket
from lib.utils.ui import Widget_Alert_Message

class MainApp(CTk):
    def __init__(self):
        super().__init__()

        """ Variable """
        
        """ Screen Setting """
        self.screen_width = 900 
        self.screen_height = 900
        self.geometry(f"{self.screen_width}x{self.screen_height}+{self.winfo_screenwidth()//2 - self.screen_width//2}+{self.winfo_screenheight()//2 - self.screen_height//2}")
        self.resizable(False, False)
        
        set_appearance_mode("Dark")

        self.title("Template")

        # Client Socket
        ApplicationConfiguration().createClientSocketSetting()
        self.client_socket = Thread_Client_Socket()
        self.client_socket.start()
        self.client_socket.set_message_recieve_callback(self.client_socket_message_recieve_callback)

        # UI
        self.build_ui()
        self.alert_message_ui()
        
        self.bind("<Escape>", lambda event : self.exit_application())
    
    def build_ui(self):
        self.configure(fg_color = Color().background)
        
        self.frame_client_sent_message = CTkFrame(self, fg_color = Color().transparent)
        self.frame_client_sent_message.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        self.frame_client_sent_message.grid_rowconfigure(0, weight = 1)
        self.frame_client_sent_message.grid_columnconfigure(0, weight = 1)
        
        self.entry_send_message = CTkEntry(self.frame_client_sent_message,
                                                width = 400,
                                                placeholder_text = "Send message to server",
                                                corner_radius = 0,
                                                font = (Font().font, 16))
        self.entry_send_message.grid(row = 0, column = 0, sticky = EW)
        self.entry_send_message.bind("<Return>", lambda event : self.bind_send_message_entry())
        
        self.test_btn_send_message = CTkButton(self.frame_client_sent_message, text = "«",
                                            width = 25, height = 5,
                                            fg_color = Color().green,
                                            font = (Font().font_bold, 16),
                                            corner_radius = 0,
                                            command = self.send_message)
        self.test_btn_send_message.grid(row = 0, column = 1)
    
    def alert_message_ui(self):
        self.widget_alert_message = Widget_Alert_Message(self,self, self.client_socket)
        self.widget_alert_message.place(x = 0, y = 0, anchor = NW)
        self.widget_alert_message.locomotion(self.screen_width, 0)
    
    """ Socket Client Function """
    def client_socket_message_recieve_callback(self, message):
        print(f"[MainApp] Recieve Message : {message}")
        if message == "Exit":
            self.exit_application()
            
    def bind_send_message_entry(self):
        if self.entry_send_message.focus_get(): 
            self.send_message()
    
    def send_message(self):
        if self.client_socket.isConnect and self.entry_send_message.get() != "":
            self.client_socket.send_message_to_server(self.entry_send_message.get())
            self.entry_send_message.delete(0, END)
            self.focus() # Unfocus entry if sent message successful

    def exit_application(self):
        self.destroy()

app = MainApp()
app.mainloop()