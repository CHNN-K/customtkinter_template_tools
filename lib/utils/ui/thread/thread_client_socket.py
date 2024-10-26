import threading
import socket
import time
import json

from lib.utils import Path, ClientSocketSetting

class Thread_Client_Socket(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.ip = "127.0.0.1"
        self.port = 2001
        self.daemon = True
        self._is_stop = threading.Event()
        
        self.isPause = False
        self.isConnect = False
        
        self.message_recieve_callback = None
        
        self.json_read_setting()
        
    def run(self):
        while not self._is_stop.is_set():
            while not self.isPause:
                if not self.isConnect:
                    try:
                        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        self.client_socket.connect((self.ip, self.port))
                        self.isConnect = True
                        print (f"[Client] Connected to server {self.ip}:{self.port}")
                    except Exception as e:
                        # print("Reconnect to server")
                        time.sleep(1)
                

                while self.isConnect:
                    try:
                        message = self.client_socket.recv(1024).decode('utf-8')
                        if message:
                            print(f"[Client] From Server : {message}")
                            if self.message_recieve_callback:
                                self.message_recieve_callback(message)
                        else:
                            print("[Client] Connection closed by server.")
                            self.isConnect = False
                            self.client_socket.close()
                        
                    except Exception as e:
                        print("[Client] Disconnected from server.")
                        self.isConnect = False
                        self.client_socket.close()
                        
                    time.sleep(0.1)
            time.sleep(0.5)
        print("Stop thread")
    
    def send_message_to_server(self, message : str):
        try:
            self.client_socket.sendall(message.encode('utf-8'))
            print(f"[Client] To Server : {message}")
        except Exception as e:
            print(f"[Client] Error: {e}")
            self.client_socket.close()

    def unpause(self):
        self.isPause = False

    def pasue(self):
        self.isPause = True
        self.isConnect = False
        self.client_socket.close()
        
    def stop(self):
        self.pasue()
        self._is_stop.set()
    
    def set_message_recieve_callback(self, callback):
        self.message_recieve_callback = callback
        
    
    def json_read_setting(self):
        try:
            with open(Path().json_setting_client_socket, 'r') as file:
                json_data = json.load(file)
            
            self.ip = json_data[ClientSocketSetting.ip.name]
            self.port = json_data[ClientSocketSetting.port.name]
        except:
            print ("[Client] Can't find client socket json setting")