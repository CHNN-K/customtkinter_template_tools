from customtkinter import *
import cv2
import multiprocessing
from PIL import Image
import time

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

class Camera:
    def __init__(self):
        self.frame_queue = multiprocessing.Queue()
        self.process = None
        
        self.fps = 0
        self.start_time = time.time()
        self.frameCount = 0
        
    def start(self):
        self.process = multiprocessing.Process(target=self._capture_frames, args=(self.frame_queue,))
        self.process.start()
    
    def _capture_frames(self, frame_queue):
        cap = cv2.VideoCapture(0)
        while True:
            self.calculateFPS()
            ret, frame = cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                if not frame_queue.full():
                    frame_queue.put(frame)
            time.sleep(0.03)  # Limit the frame rate to prevent excessive CPU usage
        cap.release()
    
    def get_frame(self):
        if not self.frame_queue.empty():
            return self.frame_queue.get()
        return None
    
    def stop(self):
        if self.process is not None:
            self.process.terminate()
            self.process.join()
    
    def calculateFPS(self):
        current_time = time.time()
        self.frameCount += 1
        
        elapsed_time = current_time - self.start_time
        if elapsed_time > 1:
            fps = self.frameCount / elapsed_time
            self.fps = f"{fps:.2f}"
            self.frameCount = 0
            self.start_time = current_time

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
        
        self.bind("<Escape>", lambda event : self.on_closing())
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.camera = Camera()
        self.camera.start()

        # UI
        self.build_ui()
        
        # Function
        self.FixedUpdate()
    
    def FixedUpdate(self):
        self.update_camera_frame()
        self.after(10, self.FixedUpdate)
    
    def build_ui(self):
        self.configure(fg_color = Color().background)
        self.grid_columnconfigure(0, weight = 0)
        self.grid_rowconfigure(0, weight = 0)
        
        self.frame_main = CTkFrame(self, fg_color = Color().red, corner_radius = 0)
        self.frame_main.grid(row = 0, column = 0, sticky = NSEW)
        self.frame_main.grid_columnconfigure(0, weight = 0, minsize = 1012)
        self.frame_main.grid_rowconfigure(0, weight = 0, minsize = 760)
        
        self.label_camera = CTkLabel(self.frame_main, text = "Display camera image", 
                                    fg_color = Color().transparent,
                                    font = (Font().font_bold, 32),
                                    text_color = Color().black)
        self.label_camera.grid(row = 0, column = 0)
        
        self.image_camera = CTkLabel(self.frame_main, text = "", 
                                    fg_color = Color().transparent,
                                    corner_radius = 0)
        self.image_camera.grid(row = 0, column = 0)
        
        self.label_fps = CTkLabel(self.frame_main, text = "FPS:0.00", 
                                  fg_color = Color().black,
                                  font = (Font().font, 14),
                                  text_color = Color().white)
        self.label_fps.grid(row = 0, column = 0, ipadx = 5, sticky = NE)
    
    def update_camera_frame(self):
        try:
            self.image_camera.configure(image = CTkImage(Image.fromarray(self.camera.get_frame()), size = (1012, 760)))
            
            self.label_fps.configure(text = f"FPS:{self.camera.get_framerate()}")
        except:
            pass
    
    def on_closing(self):
        self.camera.stop()  # Stop the video capture process
        self.destroy()

if __name__ == "__main__":
    multiprocessing.freeze_support()
    app = MainApp()
    app.mainloop()