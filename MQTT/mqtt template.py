from customtkinter import *
import paho.mqtt.client as mqtt
import threading
import json

""" As Thread """
class MQTTClient:
    def __init__(self, broker : str, port : int):
        self.mqttBroker = broker
        self.mqttPort = port
        
        self.mqttSubscribeTopic = []
        self.mqttMessage = []
        self.isSubscribe = False
        self.showMessageBox = True

    def connect(self):
        self.mqttClient = mqtt.Client()
        self.mqttClient.on_connect = self.on_connect
        self.mqttClient.on_message = self.on_message
        self.mqttClient.connect(self.mqttBroker, self.mqttPort)
        self.mqttClient.loop_forever()
        # print("Connecting to MQTT broker...")
    
    def disconnect(self):
        self.mqttClient.loop_stop()
        self.mqttClient.disconnect()
        print("Disconnected")

    def on_connect(self, client, userdata, flags, rc):
        if (rc == 0):
            print("MQTT Connected.")
            self.subscribeTopic(["test","test2","test3"])
        else:
            print("MQTT Connecting Fail")

    def on_message(self, client, userdata, msg):
        topic = msg.topic
        message = msg.payload.decode("utf-8", "strict")
        self.mqttMessage[self.mqttSubscribeTopic.index(topic)] = message
        
        # Print Message Box
        if (self.showMessageBox):
            print (f"\n*** Message Box ***")
            for order,i in enumerate(self.mqttMessage):
                print (f"Topic {order} : {self.mqttSubscribeTopic[order]} | Last Message : {i}")
    
    def subscribeTopic(self, topic):
        if (self.isSubscribe):
            if (type(topic) == str or type(topic) == list):
                print(f"Can't subscribe to topic {topic}")
            print(f"Already subscribe to topic {self.mqttSubscribeTopic}")
            return
        
        print("*** Subscribe Topic List ***")
        for order,i in enumerate(topic):
            self.mqttClient.subscribe(i)
            self.mqttSubscribeTopic.append(i)
            self.mqttMessage.append("")
            print(f"{order} | Subscribe topic : {i}")
        self.isSubscribe = True
        
    def publishMessage(self, topic, msg):
        if (self.mqttClient.is_connected() == False):
            print("MQTT Client is Disconnected")
            return
        
        self.mqttClient.publish(topic, msg)
        print(f"\nPublish message : {msg} | To topic : {topic}")
        
    def publishRetainMessage(self, topic, msg):
        if (self.mqttClient.is_connected() == False):
            print("MQTT Client is Disconnected")
            return
            
        self.mqttClient.publish(topic, msg, retain = True)
        print(f"\nPublish retain message : {msg} | To topic : {topic}")
        
mqttClient = MQTTClient("test.mosquitto.org", 1883)
mqttThread = threading.Thread(target = mqttClient.connect)
# mqttThread.start()

""" As Function in CTk"""
class MainApp(CTk):
    def __init__(self):
        super().__init__()

        # Variable
        self.batch_number = "0002259295"
        
        # MQTT
        self.mqttBroker = "test.mosquitto.org"
        self.mqttPort = 1883
        
        self.mqttSubscribeTopic = []
        self.mqttMessage = []
        self.isSubscribe = False
        
        # Setting
        self.showMessageBox = True
        
        # Screen Setting
        screen_width = 600
        screen_height = 600
        self.geometry(f"{screen_width}x{screen_height}+{self.winfo_screenwidth() - screen_width}+{self.winfo_screenheight() - screen_height}")
        self.resizable(True, True)
        
        set_appearance_mode("Dark")

        self.title("Template")
        
        self.bind("<Escape>", sys.exit)

        # .=============.
        # |    Main     |
        # .=============.
        
        # UI
        self.build_ui()
        
        # Function
        self.connect_mqtt() # MQTT Client
        self.FixedUpdate()
        
        # .=============.
        # |  End Main   |
        # .=============.
    
    def FixedUpdate(self):
        if (self.mqttMessage != []):
            self.showText.configure(text = self.mqttMessage[0])
        self.after(50, self.FixedUpdate)

    def build_ui(self):
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)
        
        self.frame_main = CTkFrame(self)
        self.frame_main.grid(row = 0, column = 0, sticky = NSEW)
        self.frame_main.grid_rowconfigure(0, weight = 1)
        self.frame_main.grid_columnconfigure(0, weight = 1)
        
        self.showText = CTkLabel(self, text = "MQTT Text Show", font = ("Consolas", 24))
        self.showText.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        
        self.btn_publish = CTkButton(self, text = "Publish MQTT Message", font = ("Consolas", 20), command = lambda : self.mqttPublishMessage("test", "Test Publish"))
        self.btn_publish.place(relx = 0.5, rely = 0.6, anchor = CENTER)
        
        self.btn_postToPCB = CTkButton(self, text = "Post to PCB", font = ("Consolas", 20), command = lambda : self.PostToPCB(1))
        self.btn_postToPCB.place(relx = 0.5, rely = 0.7, anchor = CENTER)
        
        self.btn_disconnect = CTkButton(self, text = "Disconnect", font = ("Consolas", 20), command = self.mqttDisconnect)
        self.btn_disconnect.place(relx = 0.5, rely = 0.8, anchor = CENTER)
 
    # MQTT Post
    def PostToPCB(self, status : int):
        # jsonFormat :    {
        #                 "BATCH_NO": "0002179222", 
        #                 "STATUS": "1"
        #                 }
        message = {"BATCH_NO" : str(self.batch_number), "STATUS" : str(status)}
        jsonMsg = json.dumps(message)
        self.mqttPublishMessage("test", jsonMsg)
        return
 
    # MQTT Function
    def on_connect(self, client, userdata, flags, rc):
        if (rc == 0):
            print("MQTT Connected.")
            self.subscribeTopic(["test","test2","test3"])
        else:
            print("MQTT Connecting Fail")

    def on_message(self, client, userdata, msg):
        topic = msg.topic
        message = msg.payload.decode("utf-8", "strict")
        self.mqttMessage[self.mqttSubscribeTopic.index(topic)] = message
        
        # Print Message Box
        if (self.showMessageBox):
            print (f"\n*** Message Box ***")
            for order,i in enumerate(self.mqttMessage):
                print (f"Topic : {self.mqttSubscribeTopic[order]} | Last Message : {i}")
    
    def subscribeTopic(self, topic):
        if (self.isSubscribe):
            if (type(topic) == str or type(topic) == list):
                print (f"Can't subscribe to topic {topic}")
            print (f"Already subscribe to topic {self.mqttSubscribeTopic}")
            return
        
        print ("*** Subscribe Topic List ***")
        for order,i in enumerate(topic):
            self.mqttClient.subscribe(i)
            self.mqttSubscribeTopic.append(i)
            self.mqttMessage.append("")
            print(f"{order} | Subscribe topic : {i}")
        self.isSubscribe = True
    
    def connect_mqtt(self):
        self.mqttClient = mqtt.Client()
        self.mqttClient.on_connect = self.on_connect
        self.mqttClient.on_message = self.on_message
        self.mqttClient.connect(self.mqttBroker, self.mqttPort)
        self.mqttClient.loop_start()
        print("Connecting to MQTT broker...")
        
    def mqttPublishMessage(self, topic, msg):
        if (self.mqttClient.is_connected() == False):
            print("MQTT Client is Disconnected")
            return
        
        self.mqttClient.publish(topic, msg)
        print(f"\nPublish message : {msg} | To topic : {topic}")
        
    def mqttPublishRetainMessage(self, topic, msg):
        if (self.mqttClient.is_connected() == False):
            print("MQTT Client is Disconnected")
            return
            
        self.mqttClient.publish(topic, msg, retain = True)
        print(f"\nPublish retain message : {msg} | To topic : {topic}")
    
    def mqttDisconnect(self):
        self.mqttClient.loop_stop()
        self.mqttClient.disconnect()
        print("Disconnected")
        
# app = MainApp()
# app.mainloop()